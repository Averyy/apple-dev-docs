# vImageBuffer_CopyToCVPixelBuffer(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Copies the contents of a vImage buffer to a Core Video pixel buffer.

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
func vImageBuffer_CopyToCVPixelBuffer(_ buffer: UnsafePointer<vImage_Buffer>, _ bufferFormat: UnsafePointer<vImage_CGImageFormat>, _ cvPixelBuffer: CVPixelBuffer, _ cvImageFormat: vImageCVImageFormat!, _ backgroundColor: UnsafePointer<CGFloat>!, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageBuffer_CopyToCVPixelBuffer(const vImage_Buffer *buffer, const vImage_CGImageFormat *bufferFormat, CVPixelBufferRef cvPixelBuffer, vImageCVImageFormatRef cvImageFormat, const CGFloat *backgroundColor, vImage_Flags flags);
```

## Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

## Discussion

For compatibility with Core Video, vImage substitutes gamma `1/1.961` for [`kCVImageBufferTransferFunction_ITU_R_709_2`](../CoreVideo/kcvimagebuffertransferfunction_itu_r_709_2.md) and substitutes the ITU-R BT.709-5 transfer function for [`kCVImageBufferTransferFunction_SMPTE_240M_1995`](../CoreVideo/kcvimagebuffertransferfunction_smpte_240m_1995.md). You can manually set the transfer function using [`vImageCreateRGBColorSpaceWithPrimariesAndTransferFunction(_:_:_:_:_:)`](./vimagecreatergbcolorspacewithprimariesandtransferfunction%28_,_,_,_,_%29.md) and [`vImageCVImageFormat_SetColorSpace(_:_:)`](./vimagecvimageformat_setcolorspace%28_,_%29.md) to avoid this substitution.

## Parameters

- `buffer`: The source vImage buffer.
- `bufferFormat`: A [`vImage_CGImageFormat`](./vimage_cgimageformat.md) structure that specifies the image format of the [`vImage_Buffer`](./vimage_buffer.md) structure. If [`colorSpace`](./vimage_cgimageformat/colorspace.md) is `nil`, the function uses [`sRGB`](../CoreGraphics/cgcolorspace/srgb.md).
- `cvPixelBuffer`: The destination [`CVPixelBuffer`](../CoreVideo/cvpixelbuffer.md) instance. It’s not necessary to lock the pixel buffer before calling this function.
- `cvImageFormat`: An optional [`vImageCVImageFormat`](./vimagecvimageformat.md) instance that specifies the pixel format of the source pixel buffer. If this parameter is `nil`, the function attempts to derive this information from the Core Video pixel buffer.
- `backgroundColor`: If the source image contains alpha information and the destination format doesn’t contain alpha information, this function flattens the source image against this parameter.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagebuffer_copytocvpixelbuffer(_:_:_:_:_:_:))*