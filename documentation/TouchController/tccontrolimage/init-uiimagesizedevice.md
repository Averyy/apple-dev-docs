# init(uiImage:size:device:)

**Framework**: Touch Controller  
**Kind**: init

Creates a new image from a UIImage.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
convenience init?(uiImage: UIImage, size: CGSize, device: any MTLDevice)
```

#### Return Value

A new `TCControlImage` instance, or `nil` if the UIImage has no backing CGImage or if texture creation fails.

## Parameters

- `uiImage`: The UIKit image to create the texture from.
- `size`: The size of the image in points.
- `device`: The Metal device used to create the texture.

## See Also

- [convenience init?(cgImage: CGImage, size: CGSize, device: any MTLDevice)](tccontrolimage/init(cgimage:size:device:).md)
  Creates a new image from a CGImage.
- [convenience init(texture: any MTLTexture, size: CGSize)](tccontrolimage/init(texture:size:).md)
  Creates a new image with the specified texture and size.
- [init(texture: any MTLTexture, size: CGSize, highlight: (any MTLTexture)?, offset: CGPoint, tintColor: CGColor)](tccontrolimage/init(texture:size:highlight:offset:tintcolor:).md)
  Creates a new image with the specified texture, size, highlight texture, offset, and color tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolimage/init(uiimage:size:device:))*