# vImage_Buffer

**Framework**: Accelerate  
**Kind**: struct

An image buffer that stores an image’s pixel data, dimensions, and row stride.

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
struct vImage_Buffer
```

## Mentions

- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
- [Applying vImage operations to regions of interest](applying-vimage-operations-to-regions-of-interest.md)
- [Creating and Populating Buffers from Core Graphics Images](creating-and-populating-buffers-from-core-graphics-images.md)
- [Building a basic image conversion workflow](building-a-basic-image-conversion-workflow.md)
- [Building a Basic Image-Processing Workflow](building-a-basic-image-processing-workflow.md)
- [Compositing images with vImage blend modes](compositing-images-with-vimage-blend-modes.md)
- [Converting bitmap data between Core Graphics images and vImage buffers](converting-bitmap-data-between-core-graphics-images-and-vimage-buffers.md)

#### Overview

The vImage buffer is the fundamental data structure that the vImage library uses to represent image data. To ensure the best performance, the vImage buffer initialization functions may add extra padding to each row. For example, the following code declares an 8-bit per pixel buffer that’s 10 pixels wide:

```swift
var buffer = vImage_Buffer()

vImageBuffer_Init(&buffer,
                  5,    // height
                  10,   // width
                  8,    // bits per pixel
                  vImage_Flags(kvImageNoFlags))
```

Although the code defines a buffer with 10 bytes per row, to maximize performance, [`vImageBuffer_Init(_:_:_:_:_:)`](vimagebuffer_init(_:_:_:_:_:).md) initializes a buffer with 16 bytes per row:

![A diagram that shows the visible pixels and the padding of a vImage buffer.](https://docs-assets.developer.apple.com/published/28556585f1059b162e1423b669798cbe/media-4052499%402x.png)

If you provide your own buffer storage, call [`preferredAlignmentAndRowBytes(width:height:bitsPerPixel:)`](vimage_buffer/preferredalignmentandrowbytes(width:height:bitsperpixel:).md) to get the row stride that ensures your buffer achieves the best performance.

```swift
let width = 10
let height = 5

let alignmentAndRowBytes = try vImage_Buffer.preferredAlignmentAndRowBytes(
    width: width,
    height: height,
    bitsPerPixel: 8)

// Prints "16".
print(alignmentAndRowBytes.rowBytes)

let data = UnsafeMutableRawPointer.allocate(
    byteCount: alignmentAndRowBytes.rowBytes * height,
    alignment: alignmentAndRowBytes.alignment)

let buffer = vImage_Buffer(data: data,
                           height: vImagePixelCount(height),
                           width: vImagePixelCount(width),
                           rowBytes: alignmentAndRowBytes.rowBytes)
```

## Topics

### Creating an empty vImage buffer
- [init(width: Int, height: Int, bitsPerPixel: UInt32) throws](vimage_buffer/init(width:height:bitsperpixel:).md)
  Creates a new buffer with the specified width, height, and bits per pixel.
- [init(size: CGSize, bitsPerPixel: UInt32) throws](vimage_buffer/init(size:bitsperpixel:).md)
  Creates a new buffer with the specified size and bits per pixel.
- [init()](vimage_buffer/init.md)
  Creates an empty vImage buffer.
### Creating a buffer that references existing data
- [init(data: UnsafeMutableRawPointer!, height: vImagePixelCount, width: vImagePixelCount, rowBytes: Int)](vimage_buffer/init(data:height:width:rowbytes:).md)
  Creates a new buffer with the specified size that references existing data.
- [static func preferredAlignmentAndRowBytes(width: Int, height: Int, bitsPerPixel: UInt32) throws -> (alignment: Int, rowBytes: Int)](vimage_buffer/preferredalignmentandrowbytes(width:height:bitsperpixel:).md)
  Returns the preferred alignment and row bytes for a specified size and bits per pixel.
### Consuming and producing Core Graphics images
- [init(cgImage: CGImage, flags: vImage.Options) throws](vimage_buffer/init(cgimage:flags:).md)
  Creates a new buffer with the contents of a Core Graphics image.
- [init(cgImage: CGImage, format: vImage_CGImageFormat, flags: vImage.Options) throws](vimage_buffer/init(cgimage:format:flags:).md)
  Creates a new buffer with the contents of a Core Graphics image using the supplied image format.
- [func createCGImage(format: vImage_CGImageFormat, flags: vImage.Options) throws -> CGImage](vimage_buffer/createcgimage(format:flags:).md)
  Creates a Core Graphics image from the vImage buffer.
### Inspecting a buffer’s properties
- [var data: UnsafeMutableRawPointer!](vimage_buffer/data.md)
  A pointer to the top-left pixel of the image.
- [var height: vImagePixelCount](vimage_buffer/height.md)
  The height of the image, in pixels.
- [var width: vImagePixelCount](vimage_buffer/width.md)
  The width of the image, in pixels.
- [var size: CGSize](vimage_buffer/size.md)
  The size of the image, in pixels.
- [var rowBytes: Int](vimage_buffer/rowbytes.md)
  The distance, in bytes, between the start of one pixel row and the next in an image, including any unused space between them.
### Copying a buffer’s contents
- [func copy(destinationBuffer: inout vImage_Buffer, pixelSize: Int, flags: vImage.Options) throws](vimage_buffer/copy(destinationbuffer:pixelsize:flags:).md)
  Copies the contents of a vImage buffer to the specified destination buffer.
### Deallocating a buffer
- [func free()](vimage_buffer/free.md)
  Frees the resources associated with the vImage buffer.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [typealias vImagePixelCount](vimagepixelcount.md)
  A type for the number of pixels.
- [struct vImage_AffineTransform](vimage_affinetransform.md)
  A structure for values that represent an affine transformation.
- [struct vImage_AffineTransform_Double](vimage_affinetransform_double.md)
  A structure for values that represent a double-precision affine transformation.
- [typealias vImage_CGAffineTransform](vimage_cgaffinetransform.md)
  A structure for values that represent a Core Graphics–compatible affine transformation.
- [typealias vImage_Error](vimage_error.md)
  A type for image errors.
- [typealias vImage_Flags](vimage_flags.md)
  A type for processing options.
- [typealias GammaFunction](gammafunction.md)
  A type for a gamma function.
- [typealias ResamplingFilter](resamplingfilter.md)
  A pointer to a resampling filter callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_buffer)*