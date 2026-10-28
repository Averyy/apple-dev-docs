# vImageBuffer_InitForCopyToCVPixelBuffer(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Initializes an array of vImage buffers in the order necessary to copy to a Core Video pixel buffer.

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
func vImageBuffer_InitForCopyToCVPixelBuffer(_ buffers: UnsafeMutablePointer<vImage_Buffer>, _ converter: vImageConverter, _ pixelBuffer: CVPixelBuffer, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageBuffer_InitForCopyToCVPixelBuffer(vImage_Buffer *buffers, vImageConverterRef const converter, CVPixelBufferRef const pixelBuffer, vImage_Flags flags);
```

## Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

## Discussion

The vImage library represents multiple plane Core Video pixel buffers as individual vImage buffers. Call [`vImageConverter_GetNumberOfDestinationBuffers(_:)`](./vimageconverter_getnumberofdestinationbuffers%28_%29.md) to instantiate the correct number of destination buffers. Use this function to initialize the vImage buffers that you pass as the destinations to a Core-Video-to-Core-Graphics [`vImageConverter`](./vimageconverter.md) instance.

The following shows the code for creating the three destination buffers required to represent a [`kCVPixelFormatType_420YpCbCr8Planar`](../CoreVideo/kcvpixelformattype_420ypcbcr8planar.md) pixel buffer. On return of [`vImageConvert_AnyToAny(_:_:_:_:_:)`](./vimageconvert_anytoany%28_,_,_,_,_%29.md), the three vImage buffers contain the luminance, Cb, and Cr image data.

**Swift**:

```swift
let colorSpace = CGColorSpaceCreateDeviceRGB()

guard
    let cgImageFormat = vImage_CGImageFormat(
        bitsPerComponent: 8,
        bitsPerPixel: 32,
        colorSpace: colorSpace,
        bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.noneSkipFirst.rawValue),
        renderingIntent: .defaultIntent),
    
    let cvImageFormat = vImageCVImageFormat.make(
        format: .format420YpCbCr8Planar,
        matrix: kvImage_ARGBToYpCbCrMatrix_ITU_R_709_2.pointee,
        chromaSiting: .center,
        colorSpace: colorSpace,
        alphaIsOpaqueHint: false),
    
    let converterCGtoCV = try? vImageConverter.make(
        sourceFormat: cgImageFormat,
        destinationFormat: cvImageFormat) else {
    return
}

let destinationBufferCount = vImageConverter_GetNumberOfDestinationBuffers(converterCGtoCV)
var destinationBuffers = (0 ..< destinationBufferCount).map { _ in
    return vImage_Buffer()
}

// The `cvPixelBuffer` is the destination Core Video pixel buffer.
CVPixelBufferLockBaseAddress(cvPixelBuffer,
                             CVPixelBufferLockFlags(rawValue: 0))

// Initialize the destination buffers.
vImageBuffer_InitForCopyToCVPixelBuffer(
    &destinationBuffers,
    converterCGtoCV,
    cvPixelBuffer,
    vImage_Flags(kvImageNoAllocate))

// The source has an interleaved format with one or more channels, and 
// is encodable with a `vImage_CGImageFormat`.
assert(vImageConverter_GetNumberOfSourceBuffers(converterCGtoCV) == 1)

// On return, `destinationBuffers` contains the YpCbCr conversion of the RGB
// image data in the vImage source buffer.
// The `sourceBuffer` is the source vImage buffer.
vImageConvert_AnyToAny(converterCGtoCV,
                       &sourceBuffer,
                       &destinationBuffers,
                       nil,
                       vImage_Flags(kvImageNoFlags))

CVPixelBufferUnlockBaseAddress(cvPixelBuffer,
                               CVPixelBufferLockFlags(rawValue: 0))
```

**Objective-C**:

```objc
CGColorSpaceRef colorSpace = CGColorSpaceCreateDeviceRGB();

vImage_CGImageFormat cgImageFormat = {
    .bitsPerComponent = 8,
    .bitsPerPixel = 32,
    .colorSpace = colorSpace,
    .bitmapInfo = kCGBitmapByteOrderDefault | kCGImageAlphaNoneSkipFirst,
    .renderingIntent = kCGRenderingIntentDefault
};

vImageCVImageFormatRef cvImageFormat = vImageCVImageFormat_Create(
    kCVPixelFormatType_420YpCbCr8Planar,
    kvImage_ARGBToYpCbCrMatrix_ITU_R_709_2,
    kCVImageBufferChromaLocation_Center,
    colorSpace,
    0);

vImage_Error error = kvImageNoError;
vImageConverterRef converterCGtoCV = vImageConverter_CreateForCGToCVImageFormat(
    &cgImageFormat,
    cvImageFormat,
    NULL,
    kvImageNoFlags,
    &error);

unsigned int destinationBufferCount = vImageConverter_GetNumberOfDestinationBuffers(converterCGtoCV);
vImage_Buffer *destinationBuffers = (vImage_Buffer *)calloc(destinationBufferCount, sizeof(vImage_Buffer));

// The `cvPixelBuffer` is the destination Core Video pixel buffer.
CVPixelBufferLockBaseAddress(cvPixelBuffer, 0);

// Initialize the destination buffers.
vImageBuffer_InitForCopyToCVPixelBuffer(
    destinationBuffers,
    converterCGtoCV,
    cvPixelBuffer,
    kvImageNoAllocate);

// The source has an interleaved format with one or more channels,
// and is encodable with a `vImage_CGImageFormat`.

// On return, `destinationBuffers` contains the YpCbCr conversion of the RGB
// image data in the vImage source buffer.
// The `sourceBuffer` is the source vImage buffer.
vImageConvert_AnyToAny(converterCGtoCV,
                       &sourceBuffer,
                       destinationBuffers,
                       NULL,
                       kvImageNoFlags);

CVPixelBufferUnlockBaseAddress(cvPixelBuffer, 0);

free(destinationBuffers);
vImageConverter_Release(converterCGtoCV);
vImageCVImageFormat_Release(cvImageFormat);
CGColorSpaceRelease(colorSpace);
```

## Parameters

- `buffers`: An array of [`vImage_Buffer`](./vimage_buffer.md) structures. The number of destination buffers is the return value of [`vImageConverter_GetNumberOfDestinationBuffers(_:)`](./vimageconverter_getnumberofdestinationbuffers%28_%29.md).
- `converter`: A Core-Graphics-to-Core-Video [`vImageConverter`](./vimageconverter.md) instance.
- `pixelBuffer`: A locked [`CVPixelBuffer`](../CoreVideo/cvpixelbuffer.md) instance.
- `flags`: The options to use when performing this operation.

  > ❗ **Important**:  Always pass the [`kvImageNoAllocate`](./kvimagenoallocate.md) flag to this function. The [`kvImageNoAllocate`](./kvimagenoallocate.md) flag instructs the function to initialize the buffers to read directly from a locked [`CVPixelBuffer`](../CoreVideo/cvpixelbuffer.md) instance. All operations that use the buffers must be between calls to the [`CVPixelBufferLockBaseAddress(_:_:)`](../CoreVideo/cvpixelbufferlockbaseaddress%28_,_%29.md) and [`CVPixelBufferUnlockBaseAddress(_:_:)`](../CoreVideo/cvpixelbufferunlockbaseaddress%28_,_%29.md) functions.

## See Also

### Initializing vImage buffers that reference Core Video pixel buffer data
- [func vImageBuffer_InitForCopyFromCVPixelBuffer(UnsafeMutablePointer<vImage_Buffer>, vImageConverter, CVPixelBuffer, vImage_Flags) -> vImage_Error](./vimagebuffer_initforcopyfromcvpixelbuffer%28_,_,_,_%29.md)
  Initializes an array of vImage buffers in the order necessary to copy from a Core Video pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagebuffer_initforcopytocvpixelbuffer(_:_:_:_:))*