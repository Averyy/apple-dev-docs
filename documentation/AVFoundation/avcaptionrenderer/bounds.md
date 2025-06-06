# bounds

**Framework**: AVFoundation  
**Kind**: property

The drawing bounds of caption scenes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var bounds: CGRect { get set }
```

#### Discussion

Set this property value before drawing. The renderer uses the value in each call to [`render(in:for:)`](avcaptionrenderer/render(in:for:).md), until you change it to a new value.

## See Also

- [var captions: [AVCaption]](avcaptionrenderer/captions.md)
  The captions to render.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/bounds)*