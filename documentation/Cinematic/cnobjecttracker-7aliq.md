# CNObjectTracker

**Framework**: Cinematic  
**Kind**: class  
**Role**: Class

An object that converts a normalized point or rectangle into a detection track that tracks an object over time.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
@interface CNObjectTracker : NSObject
```

## Topics

### Instance Methods
- [- continueTrackingAt:sourceImage:sourceDisparity:](./cnobjecttracker-7aliq/continuetrackingat_sourceimage_sourcedisparity_.md)
  Continues to track an object that you’ve started tracking, and adds a new detection to the detection track you’re building.
- [- findObjectAtPoint:sourceImage:](./cnobjecttracker-7aliq/findobjectatpoint_sourceimage_.md)
  Finds the bounds of an object at the given point.
- [- finishDetectionTrack](./cnobjecttracker-7aliq/finishdetectiontrack.md)
  Finish constructing the detection track and return it.
- [- initWithCommandQueue:](./cnobjecttracker-7aliq/initwithcommandqueue_.md)
  Creates a new detection track builder.
- [- resetDetectionTrack](./cnobjecttracker-7aliq/resetdetectiontrack.md)
  Resets the builder to construct a new detection track.
- [- startTrackingAt:within:sourceImage:sourceDisparity:](./cnobjecttracker-7aliq/starttrackingat_within_sourceimage_sourcedisparity_.md)
  Starts creating a detection track to track an object within the given bounds.
### Type Properties
- [isSupported](./cnobjecttracker-7aliq/issupported.md)
  Indicates whether the current device supports object detection and tracking.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Custom Object Tracking
- [CNBoundsPrediction](./cnboundsprediction-c.class.md)
  An object representing the bounds of the predicted subject.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnobjecttracker-7aliq)*