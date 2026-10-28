# preferredDisplayCriteria

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The asset’s display mode preference for optimal playback of its content.

**Availability**:
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static var preferredDisplayCriteria: AVAsyncProperty<Root, AVDisplayCriteria> { get }
```

Available when `Root` inherits `AVAsset`.

## Discussion

Use the [`load(_:isolation:)`](../avasynchronouskeyvalueloading/load%28_,isolation%29.md) method to retrieve the property value.

## See Also

### Loading asset preferences
- [static var preferredRate: AVAsyncProperty<Root, Float>](./preferredrate.md)
  The asset’s rate preference for playing its media.
- [static var preferredVolume: AVAsyncProperty<Root, Float>](./preferredvolume-20mb3.md)
  The asset’s volume preference for playing its audible media.
- [static var preferredTransform: AVAsyncProperty<Root, CGAffineTransform>](./preferredtransform-80d13.md)
  The asset’s transform preference to apply to its visual content during presentation or processing.
- [class AVDisplayCriteria](../avdisplaycriteria.md)
  An object the system uses to guide the selection of a display mode in tvOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avpartialasyncproperty/preferreddisplaycriteria)*