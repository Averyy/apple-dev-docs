# texture

**Framework**: Touch Controller  
**Kind**: property

The Metal texture to use for the image.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var texture: any MTLTexture { get set }
```

## See Also

- [var highlightTexture: (any MTLTexture)?](tccontrolimage/highlighttexture.md)
  The Metal texture to use for the image when highlighted. May be `nil`.
- [var offset: CGPoint](tccontrolimage/offset.md)
  The offset from the center of the parent control in points.
- [var size: CGSize](tccontrolimage/size.md)
  The size of the image in points.
- [var tintColor: CGColor](tccontrolimage/tintcolor.md)
  The color tint to apply to the texture. The color ref is retained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolimage/texture)*