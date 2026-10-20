# vImageCVImageFormat

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

A mutable description of image encoding in a Core Video pixel buffer.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class vImageCVImageFormat
```

```c
typedef struct vImageCVImageFormat * vImageCVImageFormatRef;
```

## Mentions

- [Converting chroma-subsampled images](./converting-chroma-subsampled-images.md)

#### Overview

The vImage library uses the information in an image format to construct [`vImageConverter`](./vimageconverter.md) instances that convert to and from images encoded with the format. The format stores a description of the pixels in the image, such as color representation, bit depth, and number of channels.

A [`vImageCVImageFormat`](./vimagecvimageformat.md) instance is capable of holding an incomplete encoding representation. In this case, the [`vImageConverter_CreateForCGToCVImageFormat(_:_:_:_:_:)`](./vimageconverter_createforcgtocvimageformat%28_,_,_,_,_%29.md) and [`vImageConverter_CreateForCVToCGImageFormat(_:_:_:_:_:)`](./vimageconverter_createforcvtocgimageformat%28_,_,_,_,_%29.md) functions return an error code that indicates what information is missing.

- **[`kvImageCVImageFormat_ConversionMatrix`](./kvimagecvimageformat_conversionmatrix.md)**: Use [`vImageCVImageFormat_CopyConversionMatrix(_:_:_:)`](./vimagecvimageformat_copyconversionmatrix%28_,_,_%29.md) to add the missing conversion matrix.
- **[`kvImageCVImageFormat_ChromaSiting`](./kvimagecvimageformat_chromasiting.md)**: Use [`vImageCVImageFormat_SetChromaSiting(_:_:)`](./vimagecvimageformat_setchromasiting%28_,_%29.md) to add the missing chrominance siting information.
- **[`kvImageCVImageFormat_ColorSpace`](./kvimagecvimageformat_colorspace.md)**: Use [`vImageCVImageFormat_SetColorSpace(_:_:)`](./vimagecvimageformat_setcolorspace%28_,_%29.md) to add the missing color space that contains primaries and transfer function.

Reuse a [`vImageCVImageFormat`](./vimagecvimageformat.md) instance with other Core Video pixel buffers of the same format, such as other frames from the same movie.

## Topics

### Creating a Core Video image format
- [static func make(buffer: CVPixelBuffer) -> vImageCVImageFormat?](./vimagecvimageformat/make%28buffer%29.md)
  Creates the description of the image encoding in an existing Core Video pixel buffer.
- [static func make(format: vImageCVImageFormat.Format, matrix: vImage_ARGBToYpCbCrMatrix, chromaSiting: vImageCVImageFormat.ChromaSiting, colorSpace: CGColorSpace, alphaIsOpaqueHint: Bool) -> vImageCVImageFormat?](./vimagecvimageformat/make%28format,matrix,chromasiting,colorspace,alphaisopaquehint%29.md)
  Creates the description of image encoding in a Core Video pixel buffer from the specified properties.
- [static func make(format: vImageCVImageFormat.Format, colorSpace: CGColorSpace, alphaIsOpaqueHint: Bool) -> vImageCVImageFormat?](./vimagecvimageformat/make%28format,colorspace,alphaisopaquehint%29.md)
  Creates the description of an RGB image encoding in a Core Video pixel buffer from the specified properties.
### Inspecting a Core Video image format’s properties
- [var channelCount: UInt32](./vimagecvimageformat/channelcount.md)
  The number of channels, including alpha, for the Core Video image format.
- [var channels: [vImage.BufferType]](./vimagecvimageformat/channels.md)
  The channels of the Core Video image format.
- [func channelDescription(bufferType: vImage.BufferType) -> vImageChannelDescription?](./vimagecvimageformat/channeldescription%28buffertype%29.md)
  Returns the range and clamp limits for a specified channel in a Core Video image format.
- [var formatCode: UInt32](./vimagecvimageformat/formatcode.md)
  The four-character code that encodes the pixel format of the Core Video image format.
- [var chromaSiting: vImageCVImageFormat.ChromaSiting?](./vimagecvimageformat/chromasiting-swift.property.md)
  The chrominance siting of the Core Video image format.
- [var colorSpace: CGColorSpace?](./vimagecvimageformat/colorspace.md)
  The color space of the Core Video image format.
- [var alphaIsOpaqueHint: Bool](./vimagecvimageformat/alphaisopaquehint.md)
  The alpha hint of the Core Video image format.
### Supporting types
- [vImageCVImageFormat.ChromaSiting](./vimagecvimageformat/chromasiting-swift.enum.md)
  Constants that specify the chrominance siting of a Core Video image format.
- [vImageCVImageFormat.Format](./vimagecvimageformat/format.md)
  Constants that specify the format of a Core Video image format.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Creating Core Video image formats
- [class vImageConstCVImageFormat](./vimageconstcvimageformat.md)
  An immutable description of image encoding in a Core Video pixel buffer.
- [func vImageCVImageFormat_CreateWithCVPixelBuffer(CVPixelBuffer!) -> Unmanaged<vImageCVImageFormat>!](./vimagecvimageformat_createwithcvpixelbuffer%28_%29.md)
  Creates the description of the image encoding in an existing Core Video pixel buffer.
- [func vImageCVImageFormat_Create(UInt32, UnsafePointer<vImage_ARGBToYpCbCrMatrix>!, CFString!, CGColorSpace!, Int32) -> Unmanaged<vImageCVImageFormat>!](./vimagecvimageformat_create%28_,_,_,_,_%29.md)
  Creates the description of image encoding in a Core Video pixel buffer from the specified properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat)*