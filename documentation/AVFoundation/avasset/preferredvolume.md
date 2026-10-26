# preferredVolume

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The asset’s volume preference for playing its audible media.

**Availability**:
- iOS 4.0+ - Deprecated in 16.0
- iPadOS 4.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`preferredVolume`](../avpartialasyncproperty/preferredvolume-20mb3.md) asynchronously instead.

## Declaration

```swift
var preferredVolume: Float { get }
```

```objc
@property (nonatomic, readonly) float preferredVolume;
```

#### Discussion

This value is typically, but not always, 1.0.

## See Also

### Accessing asset preferences
- [preferredRate](./preferredrate.md)
  The asset’s rate preference for playing its media.
- [preferredTransform](./preferredtransform.md)
  The asset’s transform preference to apply to its visual content during presentation or processing.
- [preferredMediaSelection](./preferredmediaselection.md)
  The default media selections for this asset’s media selection groups.
- [preferredDisplayCriteria](./preferreddisplaycriteria.md)
  The asset’s display mode preference for optimal playback of its content.
- [AVDisplayCriteria](../avdisplaycriteria.md)
  An object the system uses to guide the selection of a display mode in tvOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/preferredvolume)*