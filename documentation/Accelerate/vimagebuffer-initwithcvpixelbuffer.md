# vImageBuffer_InitWithCVPixelBuffer(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Initializes a vImage buffer with a copy of the contents of a Core Video pixel buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 8.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageBuffer_InitWithCVPixelBuffer(_ buffer: UnsafeMutablePointer<vImage_Buffer>, _ desiredFormat: UnsafeMutablePointer<vImage_CGImageFormat>, _ cvPixelBuffer: CVPixelBuffer, _ cvImageFormat: vImageCVImageFormat!, _ backgroundColor: UnsafePointer<CGFloat>!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

Some Core Video pixel buffers and image formats have incompletely specified color information that prevents [`vImageBuffer_InitWithCVPixelBuffer(_:_:_:_:_:_:)`](vimagebuffer_initwithcvpixelbuffer(_:_:_:_:_:_:).md) from performing the conversion. In this situation, the function returns one of the format errors below. To proceed, create a [`vImageCVImageFormat`](vimagecvimageformat.md) instance, add the missing information, and pass the image format instance as the `cvImageFormat` parameter to this function. It’s possible that more than one piece of information is missing.

- **[`kvImageCVImageFormat_ConversionMatrix`](kvimagecvimageformat_conversionmatrix.md)**: The conversion matrix is missing from the `cvPixelBuffer` or the `vImageCVImageFormat`. Use the [`vImageCVImageFormat_CopyConversionMatrix(_:_:_:)`](vimagecvimageformat_copyconversionmatrix(_:_:_:).md) function to copy a conversion matrix to an image format.
- **[`kvImageCVImageFormat_ChromaSiting`](kvimagecvimageformat_chromasiting.md)**: The chrominance siting information is missing from the `cvPixelBuffer` or the `vImageCVImageFormat`. Use [`vImageCVImageFormat_SetChromaSiting(_:_:)`](vimagecvimageformat_setchromasiting(_:_:).md) to set the chrominance siting on an image format.
- **[`kvImageCVImageFormat_ColorSpace`](kvimagecvimageformat_colorspace.md)**: The color space that contains primaries and transfer function is missing from the `cvPixelBuffer` or the `vImageCVImageFormat`. Use [`vImageCVImageFormat_SetColorSpace(_:_:)`](vimagecvimageformat_setcolorspace(_:_:).md) to set the color space on an image format.

#### Discussion

For compatibility with Core Video, vImage substitutes gamma `1/1.961` for [`kCVImageBufferTransferFunction_ITU_R_709_2`](https://developer.apple.com/documentation/CoreVideo/kCVImageBufferTransferFunction_ITU_R_709_2) and substitutes the ITU-R BT.709-5 transfer function for [`kCVImageBufferTransferFunction_SMPTE_240M_1995`](https://developer.apple.com/documentation/CoreVideo/kCVImageBufferTransferFunction_SMPTE_240M_1995). You can manually set the transfer function using [`vImageCreateRGBColorSpaceWithPrimariesAndTransferFunction(_:_:_:_:_:)`](vimagecreatergbcolorspacewithprimariesandtransferfunction(_:_:_:_:_:).md) and [`vImageCVImageFormat_SetColorSpace(_:_:)`](vimagecvimageformat_setcolorspace(_:_:).md) to avoid this substitution.

## Parameters

- `buffer`: The destination empty [`vImage_Buffer`](vimage_buffer.md) structure. On return, the function allocates new memory to the buffer and sets the buffer’s size to match the [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/CVPixelBuffer) instance’s dimensions.
- `desiredFormat`: A [`vImage_CGImageFormat`](vimage_cgimageformat.md) structure that specifies the image format of the [`vImage_Buffer`](vimage_buffer.md) structure. If [`colorSpace`](vimage_cgimageformat/colorspace.md) is `nil`, the function uses [`sRGB`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace/sRGB).
- `cvPixelBuffer`: The source [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/CVPixelBuffer) instance. It’s not necessary to lock the pixel buffer before calling this function.
- `cvImageFormat`: An optional [`vImageCVImageFormat`](vimagecvimageformat.md) instance that specifies the pixel format of the source pixel buffer. If this parameter is `nil`, the function attempts to derive this information from the Core Video pixel buffer.
- `backgroundColor`: If the source image contains alpha information and the destination format doesn’t contain alpha information, this function flattens the source image against this parameter.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](kvimagenoflags.md). Pass [`kvImageNoAllocate`](kvimagenoallocate.md) if the destination buffer references existing data. If the pixel buffer uses chrominance subsampling and you want vImage to use a higher quality, but a slower, resampling filter, set the [`kvImageHighQualityResampling`](kvimagehighqualityresampling.md) flag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagebuffer_initwithcvpixelbuffer(_:_:_:_:_:_:))*