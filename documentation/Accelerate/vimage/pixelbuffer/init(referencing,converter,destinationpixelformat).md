# init(referencing:converter:destinationPixelFormat:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new pixel buffer that references the specified Core Video pixel buffer and populated converter.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
init(referencing lockedCVPixelBuffer: CVPixelBuffer, converter: vImageConverter, destinationPixelFormat: Format.Type = Format.self)
```

Available when `Format` conforms to `SinglePlanePixelFormat`.

## Discussion

The following code shows how to incorporate a vImage pixel buffer into a [`CIImageProcessorKernel`](../../../CoreImage/ciimageprocessorkernel.md) instance. The code calls [`init(referencing:converter:destinationPixelFormat:)`](./init%28referencing,converter,destinationpixelformat%29.md) to initialize a source and destination vImage pixel buffers that share data with the processor kernel’s input and output:

```swift
class ContrastStretchImageProcessorKernel: CIImageProcessorKernel {
    
    static var cgImageFormat = vImage_CGImageFormat(
        bitsPerComponent: 8,
        bitsPerPixel: 32,
        colorSpace: CGColorSpaceCreateDeviceRGB(),
        bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.noneSkipLast.rawValue),
        renderingIntent: .defaultIntent)!
    
    static let cvImageFormat = vImageCVImageFormat.make(
        format: .format32BGRA,
        colorSpace: CGColorSpaceCreateDeviceRGB(),
        alphaIsOpaqueHint: true)!
    
    static let converter = try! vImageConverter.make(sourceFormat: cvImageFormat,
                                                     destinationFormat: cgImageFormat)
    
    override class var outputFormat: CIFormat {
        return CIFormat.BGRA8
    }
    
    override class func formatForInput(at input: Int32) -> CIFormat {
        return CIFormat.BGRA8
    }
    
    override class func process(with inputs: [CIImageProcessorInput]?,
                                arguments: [String: Any]?,
                                output: CIImageProcessorOutput) throws {
        
        guard
            let input = inputs?.first,
            let inputPixelBuffer = input.pixelBuffer,
            let outputPixelBuffer = output.pixelBuffer else {
                return
            }
        
        CVPixelBufferLockBaseAddress(inputPixelBuffer,
                                     CVPixelBufferLockFlags.readOnly)
        CVPixelBufferLockBaseAddress(outputPixelBuffer,
                                     CVPixelBufferLockFlags(rawValue: 0))
        
        defer {
            CVPixelBufferUnlockBaseAddress(inputPixelBuffer,
                                           CVPixelBufferLockFlags.readOnly)
            CVPixelBufferUnlockBaseAddress(outputPixelBuffer,
                                           CVPixelBufferLockFlags(rawValue: 0))
        }
        
        let source = vImage.PixelBuffer(
            referencing: inputPixelBuffer,
            converter: converter,
            destinationPixelFormat: vImage.Interleaved8x4.self)
        
        let destination = vImage.PixelBuffer(
            referencing: outputPixelBuffer,
            converter: converter,
            destinationPixelFormat: vImage.Interleaved8x4.self)
        
        source.contrastStretch(destination: destination)
    }
}
```

## Parameters

- `lockedCVPixelBuffer`: The locked Core Video pixel buffer. Use [`CVPixelBufferLockBaseAddress(_:_:)`](../../../CoreVideo/cvpixelbufferlockbaseaddress%28_,_%29.md) and [`CVPixelBufferUnlockBaseAddress(_:_:)`](../../../CoreVideo/cvpixelbufferunlockbaseaddress%28_,_%29.md) to lock and unlock the pixel buffer.
- `converter`: The vImage Core Video to Core Graphics any-to-any converter.
- `destinationPixelFormat`: The pixel format of the initialized buffer.

## See Also

### Related Documentation
- [func vImageBuffer_InitForCopyFromCVPixelBuffer(UnsafeMutablePointer<vImage_Buffer>, vImageConverter, CVPixelBuffer, vImage_Flags) -> vImage_Error](../../vimagebuffer_initforcopyfromcvpixelbuffer%28_,_,_,_%29.md)
  Initializes an array of vImage buffers in the order necessary to copy from a Core Video pixel buffer.
### Creating a pixel buffer from a Core Video buffer
- [init(copying: CVPixelBuffer, cvImageFormat: vImageCVImageFormat, cgImageFormat: inout vImage_CGImageFormat, pixelFormat: Format.Type) throws](./init%28copying,cvimageformat,cgimageformat,pixelformat%29.md)
  Initializes a pixel buffer by copying the data from a Core Video pixel buffer.
- [init(referencing: CVPixelBuffer, planeIndex: Int, overrideSize: vImage.Size?, pixelFormat: Format.Type)](./init%28referencing,planeindex,overridesize,pixelformat%29.md)
  Initializes a pixel buffer by refencing the data from a single plane of a multiplane Core Video pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/init(referencing:converter:destinationpixelformat:))*