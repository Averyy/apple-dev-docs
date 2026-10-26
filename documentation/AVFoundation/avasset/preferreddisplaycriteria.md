# preferredDisplayCriteria

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The asset’s display mode preference for optimal playback of its content.

**Availability**:
- tvOS 11.2+ - Deprecated in 16.0

> **Deprecated**: Load the value of [`preferredDisplayCriteria`](../avpartialasyncproperty/preferreddisplaycriteria.md) asynchronously instead.

## Declaration

```swift
var preferredDisplayCriteria: AVDisplayCriteria { get }
```

```objc
@property (nonatomic, readonly) AVDisplayCriteria * preferredDisplayCriteria;
```

## See Also

### Accessing asset preferences
- [preferredRate](./preferredrate.md)
  The asset’s rate preference for playing its media.
- [preferredVolume](./preferredvolume.md)
  The asset’s volume preference for playing its audible media.
- [preferredTransform](./preferredtransform.md)
  The asset’s transform preference to apply to its visual content during presentation or processing.
- [preferredMediaSelection](./preferredmediaselection.md)
  The default media selections for this asset’s media selection groups.
- [AVDisplayCriteria](../avdisplaycriteria.md)
  An object the system uses to guide the selection of a display mode in tvOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/preferreddisplaycriteria)*