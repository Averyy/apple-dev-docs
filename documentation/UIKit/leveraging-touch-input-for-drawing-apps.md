# Leveraging touch input for drawing apps

**Framework**: UIKit

Capture touches as a series of strokes and render them efficiently on a drawing canvas.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Xcode 11.3+

#### Overview

This sample project, Speed Sketch, shows how to render a series of strokes a user makes by moving their finger or Apple Pencil across the screen. The project also demonstrates how to:

- Distinguish between finger and Apple Pencil touches.
- Improve drawing performance.
- Enhance the app for Apple Pencil.

##### Distinguish Between Finger and Apple Pencil Touches

With Speed Sketch, users can draw by moving their finger or Apple Pencil across the screen, and the system reports the touches to the app. Speed Sketch captures these touches using the custom gesture recognizer, `StrokeGestureRecognizer`.

The stroke gesture recognizer receives each touch event, and appends data from the touches to an array of data samples.

```swift
override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
    if trackedTouch == nil {
        trackedTouch = touches.first
        initialTimestamp = trackedTouch?.timestamp
        collectForce = trackedTouch!.type == .pencil || view?.traitCollection.forceTouchCapability == .available
        if !isForPencil {
            // Give other gestures, such as pan and pinch, a chance by
            // slightly delaying the .began state.
            fingerStartTimer = Timer.scheduledTimer(
                withTimeInterval: cancellationTimeInterval,
                repeats: false,
                block: { [weak self] (timer) in
                    guard let strongSelf = self else { return }
                    if strongSelf.state == .possible {
                        strongSelf.state = .began
                    }
                }
            )
        }
    }
    if append(touches: touches, event: event) {
        if isForPencil {
            state = .began
        }
    }
}

override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
    if append(touches: touches, event: event) {
        if state == .began {
            state = .changed
        }
    }
}

override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
    if append(touches: touches, event: event) {
        stroke.state = .done
        state = .ended
    }
}

override func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?) {
    if append(touches: touches, event: event) {
        stroke.state = .cancelled
        state = .failed
    }
}
```

The [`touchesBegan(_:with:)`](uigesturerecognizer/touchesbegan(_:with:).md) method sets a timer to give other gesture recognizers, such as pan and pinch, time to handle touches that the user makes with their finger. This behavior is unique to drawing apps such as Speed Sketch that start capturing and drawing a stroke the moment the user touches the screen.

In order to track finger and Apple Pencil touches separately, Speed Sketch uses two instances of `StrokeGestureRecognizer`: one for finger touches and the other to track touches coming from Apple Pencil.

```swift
self.fingerStrokeRecognizer = setupStrokeGestureRecognizer(isForPencil: false)
self.pencilStrokeRecognizer = setupStrokeGestureRecognizer(isForPencil: true)
```

To simplify the code, the app uses a helper method to create the gesture recognizers.

```swift
func setupStrokeGestureRecognizer(isForPencil: Bool) -> StrokeGestureRecognizer {
    let recognizer = StrokeGestureRecognizer(target: self, action: #selector(strokeUpdated(_:)))
    recognizer.delegate = self
    recognizer.cancelsTouchesInView = false
    scrollView.addGestureRecognizer(recognizer)
    recognizer.coordinateSpaceView = cgView
    recognizer.isForPencil = isForPencil
    return recognizer
}
```

The gesture recognizer distinguishes between the touch types by setting the [`allowedTouchTypes`](uigesturerecognizer/allowedtouchtypes.md) property to [`UITouch.TouchType.pencil`](uitouch/touchtype/pencil.md) when tracking Apple Pencil touches, and to [`UITouch.TouchType.direct`](uitouch/touchtype/direct.md) when tracking touches from a finger.

```swift
var isForPencil: Bool = false {
    didSet {
        if isForPencil {
            allowedTouchTypes = [UITouch.TouchType.pencil.rawValue as NSNumber]
        } else {
            allowedTouchTypes = [UITouch.TouchType.direct.rawValue as NSNumber]
        }
    }
}
```

Each time the user draws a stroke on the screen, the stroke gesture recognizer calls the `strokeUpdate(_:)` method. This method checks to see if the recognizer is for Apple Pencil, and if so, puts the app into pencil mode. While the app is in pencil mode, the user can use one finger to pan the drawing canvas. When the app isn’t in pencil mode — that is, when the user is drawing with their finger — the user uses two fingers to pan the drawing canvas.

```swift
var pencilMode = false {
    didSet {
        if pencilMode {
            scrollView.panGestureRecognizer.minimumNumberOfTouches = 1
            pencilButton.isHidden = false
            if let view = fingerStrokeRecognizer.view {
                view.removeGestureRecognizer(fingerStrokeRecognizer)
            }
        } else {
            scrollView.panGestureRecognizer.minimumNumberOfTouches = 2
            pencilButton.isHidden = true
            if fingerStrokeRecognizer.view == nil {
                scrollView.addGestureRecognizer(fingerStrokeRecognizer)
            }
        }
    }
}
```

##### Improve Drawing Performance

The stroke gesture recognizer receives touch events from the system. For most apps, the time span between each touch event is enough to handle the gesture. However, users of drawing apps expect greater precision, which requires the app to gather all the touches reported since the last delivered touch event.

To gather the additional touches, Speed Sketch calls the [`coalescedTouches(for:)`](uievent/coalescedtouches(for:).md) method. This method returns an array of [`UITouch`](uitouch.md) objects representing the touches received by the system but not delivered in the last event. The additional touches allow Speed Sketch to provide a smoother rendering of the stroke by storing the coalesced touches as part of the stroke’s data sample.

```swift
if collectsCoalescedTouches {
    if let event = event {
        let coalescedTouches = event.coalescedTouches(for: touchToAppend)!
        let lastIndex = coalescedTouches.count - 1
        for index in 0..<lastIndex {
            saveStrokeSample(stroke: stroke, touch: coalescedTouches[index], view: view, coalesced: true, predicted: false)
        }
        saveStrokeSample(stroke: stroke, touch: coalescedTouches[lastIndex], view: view, coalesced: false, predicted: false)
    }
} else {
    saveStrokeSample(stroke: stroke, touch: touchToAppend, view: view, coalesced: false, predicted: false)
}
```

In addition to coalesced touches, Speed Sketch uses touch data predicted by the system as a way to enhance the perceived accuracy of the app’s drawing capabilities. Speed Sketch retrieves the predicted touches by calling the [`predictedTouches(for:)`](uievent/predictedtouches(for:).md) method for the event, then saves the touches as part of the data sample for the stroke.

```swift
if usesPredictedSamples && stroke.state == .active {
    if let predictedTouches = event?.predictedTouches(for: touchToAppend) {
        for touch in predictedTouches {
            saveStrokeSample(stroke: stroke, touch: touch, view: view, coalesced: false, predicted: true)
        }
    }
}
```

The app replaces the predicted touches with actual touches as they become available.

```swift
override func touchesEstimatedPropertiesUpdated(_ touches: Set<UITouch>) {
    for touch in touches {
        guard let index = touch.estimationUpdateIndex else {
            continue
        }
        if let (stroke, sampleIndex) = outstandingUpdateIndexes[Int(index.intValue)] {
            var sample = stroke.samples[sampleIndex]
            let expectedUpdates = sample.estimatedPropertiesExpectingUpdates
            if expectedUpdates.contains(.force) {
                sample.force = touch.force
                if !touch.estimatedProperties.contains(.force) {
                    // Only remove the estimate flag if the new value isn't estimated as well.
                    sample.estimatedProperties.remove(.force)
                }
            }
            sample.estimatedPropertiesExpectingUpdates = touch.estimatedPropertiesExpectingUpdates
            if touch.estimatedPropertiesExpectingUpdates == [] {
                outstandingUpdateIndexes.removeValue(forKey: sampleIndex)
            }
            stroke.update(sample: sample, at: sampleIndex)
        }
    }
}
```

##### Enhance for Apple Pencil

Apple Pencil can sense tilt (altitude), force (pressure), and orientation (azimuth), which drawing apps can use to affect the appearance of strokes. For instance, Speed Sketch uses azimuth to enhance the strokes when using the app’s Calligraphy drawing tool.

```swift
func drawCalligraphy(in context: CGContext,
                     toSample: StrokeSample,
                     fromSample: StrokeSample,
                     forceAccessBlock: (_ sample: StrokeSample) -> CGFloat) {

    var fromAzimuthUnitVector = Stroke.calligraphyFallbackAzimuthUnitVector
    var toAzimuthUnitVector = Stroke.calligraphyFallbackAzimuthUnitVector

    if fromSample.azimuth != nil {

        if lockedAzimuthUnitVector == nil {
            lockedAzimuthUnitVector = fromSample.azimuthUnitVector
        }
        fromAzimuthUnitVector = fromSample.azimuthUnitVector
        toAzimuthUnitVector = toSample.azimuthUnitVector
        if fromSample.altitude! > azimuthLockAltitudeThreshold {
            fromAzimuthUnitVector = lockedAzimuthUnitVector!
        }
        if toSample.altitude! > azimuthLockAltitudeThreshold {
            toAzimuthUnitVector = lockedAzimuthUnitVector!
        } else {
            lockedAzimuthUnitVector = toAzimuthUnitVector
        }

    }
    // Rotate 90 degrees
    let calligraphyTransform = CGAffineTransform(rotationAngle: CGFloat.pi / 2.0)
    fromAzimuthUnitVector = fromAzimuthUnitVector.applying(calligraphyTransform)
    toAzimuthUnitVector = toAzimuthUnitVector.applying(calligraphyTransform)

    let fromUnitVector = fromAzimuthUnitVector * forceAccessBlock(fromSample)
    let toUnitVector = toAzimuthUnitVector * forceAccessBlock(toSample)

    context.beginPath()
    context.addLines(between: [
        fromSample.location + fromUnitVector,
        toSample.location + toUnitVector,
        toSample.location - toUnitVector,
        fromSample.location - fromUnitVector
        ])
    context.closePath()

    context.drawPath(using: .fillStroke)

}
```

Speed Sketch also displays the altitude and azimuth data as part of the stroke when the user selects the Debug drawing tool.

```swift
func drawDebugMarkings(in context: CGContext, fromSample: StrokeSample) {

    let isEstimated = fromSample.estimatedProperties.contains(.azimuth)
    guard displayOptions == .debug,
        fromSample.predicted == false,
        fromSample.azimuth != nil,
        (!fromSample.coalesced || isEstimated) else {
            return
    }

    let length = CGFloat(20.0)
    let azimuthUnitVector = fromSample.azimuthUnitVector
    let azimuthTarget = fromSample.location + azimuthUnitVector * length
    let altitudeStart = azimuthTarget + (azimuthUnitVector * (length / -2.0))
    let transformToApply = CGAffineTransform(rotationAngle: fromSample.altitude!)
    let altitudeTarget = altitudeStart + (azimuthUnitVector * (length / 2.0)).applying(transformToApply)

    // Draw altitude as black line coming from the center of the azimuth.
    altitudeSettings(in: context)
    context.beginPath()
    context.move(to: altitudeStart)
    context.addLine(to: altitudeTarget)
    context.strokePath()

    // Draw azimuth as blue (or orange if estimated) line.
    azimuthSettings(in: context)
    if isEstimated {
        context.setStrokeColor(UIColor.orange.cgColor)
    }
    context.beginPath()
    context.move(to: fromSample.location)
    context.addLine(to: azimuthTarget)
    context.strokePath()

}
```

Starting with the second generation Apple Pencil, users can double tap their finger on Apple Pencil to request an action from the app (see [`Apple Pencil interactions`](apple-pencil-interactions.md) for more information). When possible, apps should honor the system settings for double-tap actions on Apple Pencil, which include:

- Switching to the eraser or the last used tool
- Displaying a color pallet
- Ignoring double tap

Speed Sketch doesn’t have an eraser tool or color pallet, but it does have different drawing tools: Calligraphy, Ink, and Debug. When the user’s preferred double-tap action is [`UIPencilPreferredAction.switchPrevious`](uipencilpreferredaction/switchprevious.md) and the user double-taps their finger on Apple Pencil, Speed Sketch switches to the tool last used by the user. The sample app ignores the other preferred actions.

```swift
func pencilInteractionDidTap(_ interaction: UIPencilInteraction) {
    if UIPencilInteraction.preferredTapAction == .switchPrevious {
        leftRingControl.switchToPreviousTool()
    }
}
```

In order for Speed Sketch to receive the double-tap event, it adds a [`UIPencilInteraction`](uipencilinteraction.md) object to the canvas view.

```swift
let pencilInteraction = UIPencilInteraction()
pencilInteraction.delegate = self
view.addInteraction(pencilInteraction)
```

For additional information on supporting touch input in drawing apps and Apple Pencil, watch the WWDC 2016 session video [`Leveraging Touch Input on iOS`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2016/220) and the Tech Talks session video [`Designing for iPad Pro and Apple Pencil`](https://developer.apple.comhttps://developer.apple.com/videos/play/tech-talks/804/).

## See Also

- [Handling touches in your view](handling-touches-in-your-view.md)
  Use touch events directly on a view subclass if touch handling is intricately linked to the view’s content.
- [Handling input from Apple Pencil](handling-input-from-apple-pencil.md)
  Learn how to detect and respond to touches from Apple Pencil.
- [Tracking the force of 3D Touch events](tracking-the-force-of-3d-touch-events.md)
  Manipulate your content based on the force of touches.
- [Illustrating the force, altitude, and azimuth properties of touch input](illustrating-the-force-altitude-and-azimuth-properties-of-touch-input.md)
  Capture Apple Pencil and touch input in views.
- [class UITouch](uitouch.md)
  An object representing the location, size, movement, and force of a touch occurring on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/leveraging-touch-input-for-drawing-apps)*