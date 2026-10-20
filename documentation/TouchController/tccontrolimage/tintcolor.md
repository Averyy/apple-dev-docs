# tintColor

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property

The color tint to apply to the texture. The color ref is retained.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
unowned(unsafe) var tintColor: CGColor { get set }
```

```objc
@property (nonatomic, assign) CGColorRef tintColor;
```

## See Also

### Inspecting the control image
- [var highlightTexture: (any MTLTexture)?](./highlighttexture.md)
  The Metal texture to use for the image when highlighted. May be `nil`.
- [var offset: CGPoint](./offset.md)
  The offset from the center of the parent control in points.
- [var size: CGSize](./size.md)
  The size of the image in points.
- [var texture: any MTLTexture](./texture.md)
  The Metal texture to use for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolimage/tintcolor)*