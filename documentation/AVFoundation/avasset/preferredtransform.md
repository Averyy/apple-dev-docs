# preferredTransform

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The asset’s transform preference to apply to its visual content during presentation or processing.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`preferredTransform`](../avpartialasyncproperty/preferredtransform-80d13.md) asynchronously instead.

## Declaration

```swift
var preferredTransform: CGAffineTransform { get }
```

```objc
@property (nonatomic, readonly) CGAffineTransform preferredTransform;
```

## Discussion

The value is typically, but not always, the identity transform.

## See Also

### Accessing asset preferences
- [preferredRate](./preferredrate.md)
  The asset’s rate preference for playing its media.
- [preferredVolume](./preferredvolume.md)
  The asset’s volume preference for playing its audible media.
- [preferredMediaSelection](./preferredmediaselection.md)
  The default media selections for this asset’s media selection groups.
- [preferredDisplayCriteria](./preferreddisplaycriteria.md)
  The asset’s display mode preference for optimal playback of its content.
- [AVDisplayCriteria](../avdisplaycriteria.md)
  An object the system uses to guide the selection of a display mode in tvOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/preferredtransform)*