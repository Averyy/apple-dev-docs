# CIImageProcessorInput

**Framework**: Core Image  
**Kind**: protocol

A container of image data and information for use in a custom image processor.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIImageProcessorInput
```

#### Overview

Your app does not define classes that adopt this protocol; Core Image provides an object of this type when applying a custom image processor you create with a [`CIImageProcessorKernel`](ciimageprocessorkernel.md) subclass.

In your image processor class’ [`process(with:arguments:output:)`](ciimageprocessorkernel/process(with:arguments:output:).md) method, use the provided `CIImageProcessorInput` object to access the image data and supporting information to perform your custom image processing routine. For example, if you process the image using a Metal shader, use the [`metalTexture`](ciimageprocessorinput/metaltexture.md) property to bind the image as an input texture. Or, if you process the image using a CPU-based routine, use the [`baseAddress`](ciimageprocessorinput/baseaddress.md) property to access pixel data in memory.

To finish setting up or performing your image processing routine, use the provided [`CIImageProcessorOutput`](ciimageprocessoroutput.md) object to return processed pixel data to Core Image.

## Topics

### Accessing Input Image Data
- [var baseAddress: UnsafeRawPointer](ciimageprocessorinput/baseaddress.md)
  The base address of CPU memory that your Core Image Processor Kernel can read pixels from.
- [var metalTexture: (any MTLTexture)?](ciimageprocessorinput/metaltexture.md)
  A MTLTexture object that can be bound for input using Metal.
- [var pixelBuffer: CVPixelBuffer?](ciimageprocessorinput/pixelbuffer.md)
  An input pixel buffer object that your Core Image Processor Kernel can read from.
- [var surface: IOSurfaceRef](ciimageprocessorinput/surface.md)
  An input surface object that your Core Image Processor Kernel can read from.
### Getting Supplemental Information for Image Processing
- [var region: CGRect](ciimageprocessorinput/region.md)
  The rectangular region of the input image that your Core Image Processor Kernel can use to provide the output.
- [var bytesPerRow: Int](ciimageprocessorinput/bytesperrow.md)
  The bytes per row of the CPU memory that your Core Image Processor Kernel can read pixelsfrom.
- [var format: CIFormat](ciimageprocessorinput/format.md)
  The pixel format of the CPU memory that your Core Image Processor Kernel can read pixels from.
### Instance Properties
- [var digest: UInt64](ciimageprocessorinput/digest.md)
  A 64-bit digest that uniquely describes the contents of the input to a processor.
- [var roiTileCount: Int](ciimageprocessorinput/roitilecount.md)
  This property tells a tiled-input processor how many input tiles will be processed.
- [var roiTileIndex: Int](ciimageprocessorinput/roitileindex.md)
  This property tells a tiled-input processor which input tile index is being processed.

## See Also

- [class CIImageProcessorKernel](ciimageprocessorkernel.md)
  The abstract class you extend to create custom image processors that can integrate with Core Image workflows.
- [protocol CIImageProcessorOutput](ciimageprocessoroutput.md)
  A container for writing image data and information produced by a custom image processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput)*