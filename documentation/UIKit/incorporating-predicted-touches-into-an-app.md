# Incorporating predicted touches into an app

**Framework**: UIKit

Learn how to create a simple app that incorporates predicted touches into its drawing code.

#### Overview

The sample app Speed Sketch (see [`Leveraging touch input for drawing apps`](leveraging-touch-input-for-drawing-apps.md)) uses predicted touches to minimize latency when drawing using either Apple Pencil or a finger. The key class for gathering touches is the `StrokeGestureRecognizer` class. Each new sequence of touch events results in the creation of a `Stroke` object to the app’s drawing canvas. Stroke objects store the touch data needed to do stylized line drawing and can render that data using a calligraphy pen or a regular pen, or in a special debug mode that draws line segments for each distinct touch event.

![An illustration of the calligraphy, pen, and debug drawing modes in Speed Sketch.](https://docs-assets.developer.apple.com/published/281d5cfcb5400af752fb3f0a0d60e69f/media-3004387%402x.png)

##### Collect the Touch Input

The `StrokeGestureRecognizer` class collects drawing-related touch input and uses it to create a `Stroke` object representing the path to render. In addition to the touches that actually occurred, the class also gathers any predicted touches. The following code shows the portion of the gesture recognizer’s `append` method that’s responsible for gathering the predicted touches. The `collector` block called by this code processes each touch event. The parameters to that block indicate whether the touch is an actual touch or a predicted touch.

```swift
// Collect predicted touches only while the gesture is ongoing. 
if (usesPredictedSamples && stroke.state == .active) {
   if let predictedTouches = event?.predictedTouches(for: touchToAppend) {
      for touch in predictedTouches {
         collector(stroke, touch, view, false, true)
      }
   }
}
```

The collection of touch input results in the creation of `StrokeSample` objects, which are then added to the current `Stroke` object. Stroke objects store predicted touches separately from other touches. Keeping them separate makes it easier to remove them later, and keeps them from being accidentally confused with the real touch input. Each time the app adds a new set of actual touches, it discards the preceding set of predicted samples.

The following code shows a portion of the `Stroke` class, which represents the touches associated with a single drawn line. For each new set of touches, the class adds the actual touches to its primary list of samples. Any predicted touches are then stored in the `predictedSamples` property. Each time `StrokeGestureRecognizer` calls the `Stroke` method `add`, the method moves the last set of predicted touches to the `previousPredictedSamples` property and are ultimately discarded. Thus, `Stroke` maintains only the last set of predicted touches.

```swift
class Stroke {
    static let calligraphyFallbackAzimuthUnitVector = CGVector(dx: 1.0, dy:1.0).normalize! 
    var samples: [StrokeSample] = []
    var predictedSamples: [StrokeSample] = []
    var previousPredictedSamples: [StrokeSample]?
    var state: StrokeState = .active
    var sampleIndicesExpectingUpdates = Set<Int>()
    var expectsAltitudeAzimuthBackfill = false
    var hasUpdatesFromStartTo: Int?
    var hasUpdatesAtEndFrom: Int? 
    var receivedAllNeededUpdatesBlock: (() -> ())?
 
    func add(sample: StrokeSample) -> Int {
        let resultIndex = samples.count
        if hasUpdatesAtEndFrom == nil {
            hasUpdatesAtEndFrom = resultIndex
        }
 
        samples.append(sample)
        if previousPredictedSamples == nil {
            previousPredictedSamples = predictedSamples
        }
 
        if sample.estimatedPropertiesExpectingUpdates != [] {
            sampleIndicesExpectingUpdates.insert(resultIndex)
        }
 
        predictedSamples.removeAll()
        return resultIndex
    } 
 
    func addPredicted(sample: StrokeSample) {
        predictedSamples.append(sample)
    } 
 
    func clearUpdateInfo() {
        hasUpdatesFromStartTo = nil
        hasUpdatesAtEndFrom = nil
        previousPredictedSamples = nil
    } 
 
    // Other methods...
}
```

##### Render the Predicted Touches

During rendering, the app treats predicted touches like actual touches. It breaks down the contents of each `Stroke` object into one or more `StrokeSegment` objects, which the drawing code fetches using a `StrokeSegmentIterator` object. The following code shows the implementation of this class. As the drawing code iterates over the stroke samples, the `sampleAt` method returns the samples for the actual touches first. Only after the method returns all of the actual touch samples does the iterator return the samples for any predicted touches. Thus, the predicted touches are always located at the end of the stroked line.

```swift
class StrokeSegmentIterator: IteratorProtocol {
    private let stroke: Stroke
    private var nextIndex: Int
    private let sampleCount: Int
    private let predictedSampleCount: Int
    private var segment: StrokeSegment!
 
    init(stroke: Stroke) {
        self.stroke = stroke
        nextIndex = 1
        sampleCount = stroke.samples.count
        predictedSampleCount = stroke.predictedSamples.count
        if (predictedSampleCount + sampleCount > 1) {
            segment = StrokeSegment(sample: sampleAt(0)!)
            segment.advanceWithSample(incomingSample: sampleAt(1))
        }
    } 
 
    func sampleAt(_ index: Int) -> StrokeSample? {
        if (index < sampleCount) {
            return stroke.samples[index]
        }
        let predictedIndex = index - sampleCount
        if predictedIndex < predictedSampleCount {
            return stroke.predictedSamples[predictedIndex]
        } else {
            return nil
        }
    }
 
    func next() -> StrokeSegment? {
        nextIndex += 1
        if let segment = self.segment {
            if segment.advanceWithSample(incomingSample: sampleAt(nextIndex)) {
                return segment
            }
        }
        return nil
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/incorporating-predicted-touches-into-an-app)*