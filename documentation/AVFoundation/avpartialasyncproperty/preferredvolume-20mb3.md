# preferredVolume

**Framework**: AVFoundation  
**Kind**: property

The asset’s volume preference for playing its audible media.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var preferredVolume: AVAsyncProperty<Root, Float> { get }
```

#### Discussion

Use the [`load(_:)`](avasynchronouskeyvalueloading/load(_:).md) method to retrieve the property value.

The preferred volume for an audio track is typically, but not always, `1.0`. For nonaudible tracks, the value is `0.0`.

## See Also

- [static var preferredRate: AVAsyncProperty<Root, Float>](avpartialasyncproperty/preferredrate.md)
  The asset’s rate preference for playing its media.
- [static var preferredTransform: AVAsyncProperty<Root, CGAffineTransform>](avpartialasyncproperty/preferredtransform-80d13.md)
  The asset’s transform preference to apply to its visual content during presentation or processing.
- [static var preferredDisplayCriteria: AVAsyncProperty<Root, AVDisplayCriteria>](avpartialasyncproperty/preferreddisplaycriteria.md)
  The asset’s display mode preference for optimal playback of its content.
- [class AVDisplayCriteria](avdisplaycriteria.md)
  An object the system uses to guide the selection of a display mode in tvOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/preferredvolume-20mb3)*