# vImage_CGImageFormat

**Framework**: Accelerate  
**Kind**: struct

The description of a Core Graphics image.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct vImage_CGImageFormat
```

## Mentions

- [Converting bitmap data between Core Graphics images and vImage buffers](converting-bitmap-data-between-core-graphics-images-and-vimage-buffers.md)
- [Optimizing image-processing performance](optimizing-image-processing-performance.md)
- [Applying flood fills to an image](applying-flood-fills-to-an-image.md)
- [Transforming an image in three dimensions](transforming-an-image-in-three-dimensions.md)
- [Converting chroma-subsampled images](converting-chroma-subsampled-images.md)
- [Building a basic image conversion workflow](building-a-basic-image-conversion-workflow.md)

#### Overview

This structure describes the ordering and number of the color channels, the size and type of the data in the color channels, and alpha information. This format mirrors the image format descriptors that Core Graphics uses to create objects, such as [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) and doc://com.apple.documentation/documentation/coregraphics/cgbitmapcontext.

## Topics

### Initializers
- [init(bitsPerComponent: UInt32, bitsPerPixel: UInt32, colorSpace: Unmanaged<CGColorSpace>!, bitmapInfo: CGBitmapInfo, version: UInt32, decode: UnsafePointer<CGFloat>!, renderingIntent: CGColorRenderingIntent)](vimage_cgimageformat/init(bitspercomponent:bitsperpixel:colorspace:bitmapinfo:version:decode:renderingintent:).md)
  Creates a Core Graphics image format.
- [init?(bitsPerComponent: Int, bitsPerPixel: Int, colorSpace: CGColorSpace, bitmapInfo: CGBitmapInfo, renderingIntent: CGColorRenderingIntent)](vimage_cgimageformat/init(bitspercomponent:bitsperpixel:colorspace:bitmapinfo:renderingintent:).md)
  Creates a Core Graphics image format with a color space instance and default decode array.
- [init?(cgImage: CGImage)](vimage_cgimageformat/init(cgimage:).md)
  Creates a Core Graphics image format of the specified image.
- [init()](vimage_cgimageformat/init.md)
  Creates an empty Core Graphics image format.
### Instance properties
- [var bitsPerComponent: UInt32](vimage_cgimageformat/bitspercomponent.md)
  The number of bits that represents one channel of data in one pixel.
- [var bitsPerPixel: UInt32](vimage_cgimageformat/bitsperpixel.md)
  The number of bits that represents one pixel.
- [var colorSpace: Unmanaged<CGColorSpace>!](vimage_cgimageformat/colorspace.md)
  A description of the position of the pixel data in the image, relative to a reference XYZ color space.
- [var bitmapInfo: CGBitmapInfo](vimage_cgimageformat/bitmapinfo.md)
  The component information that describes the color channels.
- [var version: UInt32](vimage_cgimageformat/version.md)
  The version number.
- [var decode: UnsafePointer<CGFloat>!](vimage_cgimageformat/decode.md)
  The decode array for the image.
- [var renderingIntent: CGColorRenderingIntent](vimage_cgimageformat/renderingintent.md)
  A rendering intent constant that specifies how Core Graphics handles colors that aren’t within the destination color space gamut.
- [var componentCount: Int](vimage_cgimageformat/componentcount.md)
  The number of color and alpha channels.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat)*