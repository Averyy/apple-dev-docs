# init(bitsPerComponent:bitsPerPixel:colorSpace:bitmapInfo:renderingIntent:)

**Framework**: Accelerate  
**Kind**: init

Creates a Core Graphics image format with a color space instance and default decode array.

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
init?(bitsPerComponent: Int, bitsPerPixel: Int, colorSpace: CGColorSpace, bitmapInfo: CGBitmapInfo, renderingIntent: CGColorRenderingIntent = .defaultIntent)
```

## Parameters

- `bitsPerComponent`: The number of bits that represents one channel of data in one pixel.
- `bitsPerPixel`: The number of bits that represents one pixel.
- `colorSpace`: A description of the position of the pixel data in the image, relative to a reference XYZ color space.
- `bitmapInfo`: The component information that describes the color channels.
- `renderingIntent`: A rendering intent constant that specifies how Core Graphics handles colors that aren’t within the destination color space gamut.

## See Also

- [init(bitsPerComponent: UInt32, bitsPerPixel: UInt32, colorSpace: Unmanaged<CGColorSpace>!, bitmapInfo: CGBitmapInfo, version: UInt32, decode: UnsafePointer<CGFloat>!, renderingIntent: CGColorRenderingIntent)](vimage_cgimageformat/init(bitspercomponent:bitsperpixel:colorspace:bitmapinfo:version:decode:renderingintent:).md)
  Creates a Core Graphics image format.
- [init?(cgImage: CGImage)](vimage_cgimageformat/init(cgimage:).md)
  Creates a Core Graphics image format of the specified image.
- [init()](vimage_cgimageformat/init.md)
  Creates an empty Core Graphics image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat/init(bitspercomponent:bitsperpixel:colorspace:bitmapinfo:renderingintent:))*