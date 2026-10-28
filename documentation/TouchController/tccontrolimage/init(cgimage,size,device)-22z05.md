# init(cgImage:size:device:)

**Framework**: Touch Controller  
**Kind**: init  
**Role**: Initializer

Creates a new image from a CGImage.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
convenience init?(cgImage: CGImage, size: CGSize, device: any MTLDevice)
```

```objc
- (instancetype) initWithCGImage:(CGImageRef) cgImage size:(CGSize) size device:(id<MTLDevice>) device;
```

## Return Value

A new `TCControlImage` instance, or `nil` if texture creation fails.

## Parameters

- `cgImage`: The Core Graphics image to create the texture from.
- `size`: The size of the image in points.
- `device`: The Metal device used to create the texture.

## See Also

### Creating a control image
- [convenience init(texture: any MTLTexture, size: CGSize)](./init%28texture,size%29.md)
  Creates a new image with the specified texture and size.
- [init(texture: any MTLTexture, size: CGSize, highlight: (any MTLTexture)?, offset: CGPoint, tintColor: CGColor)](./init%28texture,size,highlight,offset,tintcolor%29.md)
  Creates a new image with the specified texture, size, highlight texture, offset, and color tint.
- [convenience init?(uiImage: UIImage, size: CGSize, device: any MTLDevice)](./init%28uiimage,size,device%29-3hqf.md)
  Creates a new image from a UIImage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolimage/init(cgimage:size:device:)-22z05)*