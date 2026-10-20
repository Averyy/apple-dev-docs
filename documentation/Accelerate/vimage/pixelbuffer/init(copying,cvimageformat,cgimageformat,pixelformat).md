# init(copying:cvImageFormat:cgImageFormat:pixelFormat:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Initializes a pixel buffer by copying the data from a Core Video pixel buffer.

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
init(copying cvPixelBuffer: CVPixelBuffer, cvImageFormat: vImageCVImageFormat, cgImageFormat: inout vImage_CGImageFormat, pixelFormat: Format.Type = Format.self) throws
```

Available when `Format` conforms to `SinglePlanePixelFormat`.

#### Discussion

The following code shows how to incorporate a vImage pixel buffer into a [`CIImageProcessorKernel`](../../../CoreImage/ciimageprocessorkernel.md) instance. The code calls [`init(copying:cvImageFormat:cgImageFormat:pixelFormat:)`](./init%28copying,cvimageformat,cgimageformat,pixelformat%29.md) to initialize a pixel buffer from the processor kernel’s input:

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
   
        let buffer = try vImage.PixelBuffer(copying: inputPixelBuffer,
                                            cvImageFormat: cvImageFormat,
                                            cgImageFormat: &cgImageFormat,
                                            pixelFormat: vImage.Interleaved8x4.self)
        
        buffer.contrastStretch(destination: buffer)
        
        try buffer.copy(to: outputPixelBuffer,
                        cvImageFormat: cvImageFormat,
                        cgImageFormat: cgImageFormat)
    }
}
```

## Parameters

- `cvPixelBuffer`: The source Core Video pixel buffer.
- `cvImageFormat`: The image format of the Core Video pixel buffer.
- `cgImageFormat`: The Core Graphics image format that specifies the image output.
- `pixelFormat`: The pixel format of the initialized buffer.

## See Also

### Related Documentation
- [func vImageBuffer_InitWithCVPixelBuffer(UnsafeMutablePointer<vImage_Buffer>, UnsafeMutablePointer<vImage_CGImageFormat>, CVPixelBuffer, vImageCVImageFormat!, UnsafePointer<CGFloat>!, vImage_Flags) -> vImage_Error](../../vimagebuffer_initwithcvpixelbuffer%28_,_,_,_,_,_%29.md)
  Initializes a vImage buffer with a copy of the contents of a Core Video pixel buffer.
### Creating a pixel buffer from a Core Video buffer
- [init(referencing: CVPixelBuffer, converter: vImageConverter, destinationPixelFormat: Format.Type)](./init%28referencing,converter,destinationpixelformat%29.md)
  Returns a new pixel buffer that references the specified Core Video pixel buffer and populated converter.
- [init(referencing: CVPixelBuffer, planeIndex: Int, overrideSize: vImage.Size?, pixelFormat: Format.Type)](./init%28referencing,planeindex,overridesize,pixelformat%29.md)
  Initializes a pixel buffer by refencing the data from a single plane of a multiplane Core Video pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/init(copying:cvimageformat:cgimageformat:pixelformat:))*