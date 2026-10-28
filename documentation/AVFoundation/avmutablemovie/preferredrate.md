# preferredRate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The asset’s rate preference for playing its media.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var preferredRate: Float { get set }
```

```objc
@property (nonatomic) float preferredRate;
```

## Discussion

This value is typically, but not always, 1.0.

## See Also

### Inspecting preferences
- [var preferredVolume: Float](./preferredvolume.md)
  The asset’s volume preference for playing its audible media.
- [var preferredTransform: CGAffineTransform](./preferredtransform.md)
  The asset’s transform preference to apply to its visual content during presentation or processing.
- [var preferredMediaSelection: AVMediaSelection](./preferredmediaselection.md)
  The default media selections for this asset’s media selection groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/preferredrate)*