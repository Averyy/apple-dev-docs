# origin

**Framework**: AVFoundation  
**Kind**: property

The region’s top-left position.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var origin: AVCaptionPoint { get }
```

#### Discussion

The caption’s origin may not provide undefined [`x`](avcaptionpoint/x.md) and [`y`](avcaptionpoint/y.md) values, which indicates the region doesn’t have positioning information for that dimension.

## See Also

- [struct AVCaptionPoint](avcaptionpoint.md)
  A structure that defines the origin point for a caption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionregion/origin)*