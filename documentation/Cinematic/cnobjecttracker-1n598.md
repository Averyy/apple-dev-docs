# CNObjectTracker

**Framework**: Cinematic  
**Kind**: class  
**Role**: Class

An object that converts a normalized point or rectangle into a detection track that tracks an object over time.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
class CNObjectTracker
```

## Topics

### Initializers
- [init(commandQueue: any MTLCommandQueue)](./cnobjecttracker-1n598/init%28commandqueue%29.md)
  Creates a new detection track builder.
### Instance Methods
- [func continueTracking(at: CMTime, sourceImage: CVPixelBuffer, sourceDisparity: CVPixelBuffer) -> CNBoundsPrediction?](./cnobjecttracker-1n598/continuetracking%28at,sourceimage,sourcedisparity%29.md)
  An object that continues to track an object that you’ve started tracking, and adds a new detection to the detection track you’re building.
- [func findObject(at: CGPoint, sourceImage: CVPixelBuffer) -> CNBoundsPrediction?](./cnobjecttracker-1n598/findobject%28at,sourceimage%29.md)
  An object that finds the bounds of an object at the given point.
- [func finishDetectionTrack() -> CNDetectionTrack](./cnobjecttracker-1n598/finishdetectiontrack%28%29.md)
  Finish constructing the detection track and return it.
- [func resetDetectionTrack()](./cnobjecttracker-1n598/resetdetectiontrack%28%29.md)
  Resets the builder to construct a new detection track.
- [func startTracking(at: CMTime, within: CGRect, sourceImage: CVPixelBuffer, sourceDisparity: CVPixelBuffer) -> Bool](./cnobjecttracker-1n598/starttracking%28at,within,sourceimage,sourcedisparity%29.md)
  Starts creating a detection track to track an object within the given bounds.
### Type Properties
- [static var isSupported: Bool](./cnobjecttracker-1n598/issupported.md)
  Indicates whether the current device supports object detection and tracking.

## See Also

### Custom Object Tracking
- [struct CNBoundsPrediction](./cnboundsprediction-swift.struct.md)
  A structure representing the bounds of the predicted subject.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnobjecttracker-1n598)*