# preferredTransform

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The asset’s transform preference to apply to its visual content during presentation or processing.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var preferredTransform: CGAffineTransform { get set }
```

```objc
@property (nonatomic) CGAffineTransform preferredTransform;
```

#### Discussion

The value is typically, but not always, the identity transform.

## See Also

### Inspecting preferences
- [var preferredRate: Float](./preferredrate.md)
  The asset’s rate preference for playing its media.
- [var preferredVolume: Float](./preferredvolume.md)
  The asset’s volume preference for playing its audible media.
- [var preferredMediaSelection: AVMediaSelection](./preferredmediaselection.md)
  The default media selections for this asset’s media selection groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovie/preferredtransform)*