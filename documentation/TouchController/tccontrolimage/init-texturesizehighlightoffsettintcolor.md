# init(texture:size:highlight:offset:tintColor:)

**Framework**: Touch Controller  
**Kind**: init

Creates a new image with the specified texture, size, highlight texture, offset, and color tint.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
init(texture: any MTLTexture, size: CGSize, highlight highlightTexture: (any MTLTexture)?, offset: CGPoint, tintColor: CGColor)
```

#### Return Value

A new `TCControlImage` instance.

## Parameters

- `texture`: The Metal texture to use for the image.
- `size`: The size of the image in points.
- `highlightTexture`: The Metal texture to use for the image when highlighted. May be  .
- `offset`: The offset from the center of the parent control in points.
- `tintColor`: The color tint to apply to the texture. The color ref is retained.

## See Also

- [convenience init?(cgImage: CGImage, size: CGSize, device: any MTLDevice)](tccontrolimage/init(cgimage:size:device:).md)
  Creates a new image from a CGImage.
- [convenience init(texture: any MTLTexture, size: CGSize)](tccontrolimage/init(texture:size:).md)
  Creates a new image with the specified texture and size.
- [convenience init?(uiImage: UIImage, size: CGSize, device: any MTLDevice)](tccontrolimage/init(uiimage:size:device:).md)
  Creates a new image from a UIImage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolimage/init(texture:size:highlight:offset:tintcolor:))*