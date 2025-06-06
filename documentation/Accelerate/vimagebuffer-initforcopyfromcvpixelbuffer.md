# vImageBuffer_InitForCopyFromCVPixelBuffer(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Initializes an array of vImage buffers in the order necessary to copy from a Core Video pixel buffer.

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
func vImageBuffer_InitForCopyFromCVPixelBuffer(_ buffers: UnsafeMutablePointer<vImage_Buffer>, _ converter: vImageConverter, _ pixelBuffer: CVPixelBuffer, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The vImage library represents multiple plane Core Video pixel buffers as individual vImage buffers. Call [`vImageConverter_GetNumberOfSourceBuffers(_:)`](vimageconverter_getnumberofsourcebuffers(_:).md) to instantiate the correct number of source buffers. Use this function to initialize the vImage buffers that you pass as the sources to a Core-Video-to-Core-Graphics [`vImageConverter`](vimageconverter.md) instance.

The following shows the code for creating the three source buffers required to represent a [`kCVPixelFormatType_420YpCbCr8Planar`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_420YpCbCr8Planar) pixel buffer. On return of [`vImageBuffer_InitForCopyFromCVPixelBuffer(_:_:_:_:)`](vimagebuffer_initforcopyfromcvpixelbuffer(_:_:_:_:).md), the three vImage buffers contain the luminance, Cb, and Cr image data.

```swift
let colorSpace = CGColorSpaceCreateDeviceRGB()

guard
    let cvImageFormat = vImageCVImageFormat.make(
        format: .format420YpCbCr8Planar,
        matrix: kvImage_ARGBToYpCbCrMatrix_ITU_R_709_2.pointee,
        chromaSiting: .center,
        colorSpace: colorSpace,
        alphaIsOpaqueHint: false),
    
    var cgImageFormat = vImage_CGImageFormat(
        bitsPerComponent: 8,
        bitsPerPixel: 32,
        colorSpace: colorSpace,
        bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.noneSkipFirst.rawValue),
        renderingIntent: .defaultIntent),
    
    let converterCVtoCG = try? vImageConverter.make(
        sourceFormat: cvImageFormat,
        destinationFormat: cgImageFormat) else {
    return
}

let sourceBufferCount = vImageConverter_GetNumberOfSourceBuffers(converterCVtoCG)
var sourceBuffers = (0 ..< sourceBufferCount).map { _ in
    return vImage_Buffer()
}

// `cvPixelBuffer` is the source Core Video pixel buffer.
CVPixelBufferLockBaseAddress(cvPixelBuffer,
                             CVPixelBufferLockFlags.readOnly)

// Initialize the source buffers.
vImageBuffer_InitForCopyFromCVPixelBuffer(
    &sourceBuffers,
    converterCVtoCG,
    cvPixelBuffer,
    vImage_Flags(kvImageNoAllocate ))

// The destination has an interleaved format with one or more channels, and 
// is encodable with a `vImage_CGImageFormat`.
assert(vImageConverter_GetNumberOfDestinationBuffers(converterCVtoCG) == 1)

// Initialize the destination buffer.
var destinationBuffer = vImage_Buffer()
vImageBuffer_Init(&destinationBuffer,
                  sourceBuffers[0].height,
                  sourceBuffers[0].width,
                  cgImageFormat.bitsPerPixel,
                  vImage_Flags(kvImageNoFlags))
defer {
    destinationBuffer.free()
}

// On return, `destinationBuffer` contains the RGB conversion of the image
// data in the Core Video pixel buffer.
vImageConvert_AnyToAny(converterCVtoCG,
                       sourceBuffers,
                       &destinationBuffer,
                       nil,
                       vImage_Flags(kvImageNoFlags))

CVPixelBufferUnlockBaseAddress(cvPixelBuffer,
                               CVPixelBufferLockFlags.readOnly)
```

## Parameters

- `buffers`: An array of   structures. The number of source buffers is the return value of  .
- `converter`: A Core-Video-to-Core-Graphics   instance.
- `pixelBuffer`: A locked   instance.
- `flags`: The options to use when performing this operation.

## See Also

- [func vImageBuffer_InitForCopyToCVPixelBuffer(UnsafeMutablePointer<vImage_Buffer>, vImageConverter, CVPixelBuffer, vImage_Flags) -> vImage_Error](vimagebuffer_initforcopytocvpixelbuffer(_:_:_:_:).md)
  Initializes an array of vImage buffers in the order necessary to copy to a Core Video pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagebuffer_initforcopyfromcvpixelbuffer(_:_:_:_:))*