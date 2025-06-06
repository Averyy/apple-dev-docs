# preferredMediaSelection

**Framework**: AVFoundation  
**Kind**: property

The default media selections for this asset’s media selection groups.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var preferredMediaSelection: AVMediaSelection { get }
```

#### Discussion

Provides an instance of [`AVMediaSelection`](avmediaselection.md) with the default selections for each of the assets media selection groups.

## See Also

- [var preferredRate: Float](avcomposition/preferredrate.md)
  The asset’s rate preference for playing its media.
- [var preferredVolume: Float](avcomposition/preferredvolume.md)
  The asset’s volume preference for playing its audible media.
- [var preferredTransform: CGAffineTransform](avcomposition/preferredtransform.md)
  The asset’s transform preference to apply to its visual content during presentation or processing.
- [var preferredDisplayCriteria: AVDisplayCriteria](avcomposition/preferreddisplaycriteria.md)
  The asset’s display mode preference for optimal playback of its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcomposition/preferredmediaselection)*