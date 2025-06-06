# vImageBuffer_CopyToCVPixelBuffer(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

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

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

For compatibility with Core Video, vImage substitutes gamma `1/1.961` for [`kCVImageBufferTransferFunction_ITU_R_709_2`](https://developer.apple.com/documentation/CoreVideo/kCVImageBufferTransferFunction_ITU_R_709_2) and substitutes the ITU-R BT.709-5 transfer function for [`kCVImageBufferTransferFunction_SMPTE_240M_1995`](https://developer.apple.com/documentation/CoreVideo/kCVImageBufferTransferFunction_SMPTE_240M_1995). You can manually set the transfer function using [`vImageCreateRGBColorSpaceWithPrimariesAndTransferFunction(_:_:_:_:_:)`](vimagecreatergbcolorspacewithprimariesandtransferfunction(_:_:_:_:_:).md) and [`vImageCVImageFormat_SetColorSpace(_:_:)`](vimagecvimageformat_setcolorspace(_:_:).md) to avoid this substitution.

## Parameters

- `buffer`: The source vImage buffer.
- `bufferFormat`: A   structure that specifies the image format of the   structure. If   is  , the function uses  .
- `cvPixelBuffer`: The destination   instance. It’s not necessary to lock the pixel buffer before calling this function.
- `cvImageFormat`: An optional   instance that specifies the pixel format of the source pixel buffer. If this parameter is  , the function attempts to derive this information from the Core Video pixel buffer.
- `backgroundColor`: If the source image contains alpha information and the destination format doesn’t contain alpha information, this function flattens the source image against this parameter.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagebuffer_copytocvpixelbuffer(_:_:_:_:_:_:))*