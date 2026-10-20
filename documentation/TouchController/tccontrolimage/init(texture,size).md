# init(texture:size:)

**Framework**: Touch Controller  
**Kind**: init  
**Role**: Initializer

Creates a new image with the specified texture and size.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
convenience init(texture: any MTLTexture, size: CGSize)
```

```objc
- (instancetype) initWithTexture:(id<MTLTexture>) texture size:(CGSize) size;
```

#### Return Value

A new `TCControlImage` instance.

## Parameters

- `texture`: The Metal texture to use for the image.
- `size`: The size of the image in points.

## See Also

### Creating a control image
- [convenience init?(cgImage: CGImage, size: CGSize, device: any MTLDevice)](./init%28cgimage,size,device%29-22z05.md)
  Creates a new image from a CGImage.
- [init(texture: any MTLTexture, size: CGSize, highlight: (any MTLTexture)?, offset: CGPoint, tintColor: CGColor)](./init%28texture,size,highlight,offset,tintcolor%29.md)
  Creates a new image with the specified texture, size, highlight texture, offset, and color tint.
- [convenience init?(uiImage: UIImage, size: CGSize, device: any MTLDevice)](./init%28uiimage,size,device%29-3hqf.md)
  Creates a new image from a UIImage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolimage/init(texture:size:))*