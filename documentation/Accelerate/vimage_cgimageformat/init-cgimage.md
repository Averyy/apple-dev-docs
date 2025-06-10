# init(cgImage:)

**Framework**: Accelerate  
**Kind**: init

Creates a Core Graphics image format of the specified image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
init?(cgImage: CGImage)
```

## Mentions

- [Converting bitmap data between Core Graphics images and vImage buffers](converting-bitmap-data-between-core-graphics-images-and-vimage-buffers.md)

## Parameters

- `cgImage`: The source Core Graphics image.

## See Also

- [init(bitsPerComponent: UInt32, bitsPerPixel: UInt32, colorSpace: Unmanaged<CGColorSpace>!, bitmapInfo: CGBitmapInfo, version: UInt32, decode: UnsafePointer<CGFloat>!, renderingIntent: CGColorRenderingIntent)](vimage_cgimageformat/init(bitspercomponent:bitsperpixel:colorspace:bitmapinfo:version:decode:renderingintent:).md)
  Creates a Core Graphics image format.
- [init?(bitsPerComponent: Int, bitsPerPixel: Int, colorSpace: CGColorSpace, bitmapInfo: CGBitmapInfo, renderingIntent: CGColorRenderingIntent)](vimage_cgimageformat/init(bitspercomponent:bitsperpixel:colorspace:bitmapinfo:renderingintent:).md)
  Creates a Core Graphics image format with a color space instance and default decode array.
- [init()](vimage_cgimageformat/init.md)
  Creates an empty Core Graphics image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat/init(cgimage:))*