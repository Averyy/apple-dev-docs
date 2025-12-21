# init(texture:size:)

**Framework**: Touch Controller  
**Kind**: init

Creates a new image with the specified texture and size.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
convenience init(texture: any MTLTexture, size: CGSize)
```

#### Return Value

A new `TCControlImage` instance.

## Parameters

- `texture`: The Metal texture to use for the image.
- `size`: The size of the image in points.

## See Also

- [convenience init?(cgImage: CGImage, size: CGSize, device: any MTLDevice)](tccontrolimage/init(cgimage:size:device:).md)
  Creates a new image from a CGImage.
- [init(texture: any MTLTexture, size: CGSize, highlight: (any MTLTexture)?, offset: CGPoint, tintColor: CGColor)](tccontrolimage/init(texture:size:highlight:offset:tintcolor:).md)
  Creates a new image with the specified texture, size, highlight texture, offset, and color tint.
- [convenience init?(uiImage: UIImage, size: CGSize, device: any MTLDevice)](tccontrolimage/init(uiimage:size:device:).md)
  Creates a new image from a UIImage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolimage/init(texture:size:))*