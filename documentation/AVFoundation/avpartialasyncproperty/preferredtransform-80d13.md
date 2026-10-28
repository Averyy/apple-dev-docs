# preferredTransform

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The asset’s transform preference to apply to its visual content during presentation or processing.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var preferredTransform: AVAsyncProperty<Root, CGAffineTransform> { get }
```

Available when `Root` inherits `AVAsset`.

## Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

This value typically, but not always, equals [`CGAffineTransformIdentity`](../../CoreGraphics/cgaffinetransformidentity.md).

## See Also

### Loading asset preferences
- [static var preferredRate: AVAsyncProperty<Root, Float>](./preferredrate.md)
  The asset’s rate preference for playing its media.
- [static var preferredVolume: AVAsyncProperty<Root, Float>](./preferredvolume-20mb3.md)
  The asset’s volume preference for playing its audible media.
- [static var preferredDisplayCriteria: AVAsyncProperty<Root, AVDisplayCriteria>](./preferreddisplaycriteria.md)
  The asset’s display mode preference for optimal playback of its content.
- [class AVDisplayCriteria](../avdisplaycriteria.md)
  An object the system uses to guide the selection of a display mode in tvOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/preferredtransform-80d13)*