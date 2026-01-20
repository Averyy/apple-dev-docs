# pixelBuffer

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

An input pixel buffer object that your Core Image Processor Kernel can read from.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var pixelBuffer: CVPixelBuffer? { get }
```

#### Discussion

> ⚠️ **Warning**: This buffer must not be modified by the [`CIImageProcessorKernel`](ciimageprocessorkernel.md).

## See Also

- [var baseAddress: UnsafeRawPointer](ciimageprocessorinput/baseaddress.md)
  The base address of CPU memory that your Core Image Processor Kernel can read pixels from.
- [var metalTexture: (any MTLTexture)?](ciimageprocessorinput/metaltexture.md)
  A MTLTexture object that can be bound for input using Metal.
- [var surface: IOSurfaceRef](ciimageprocessorinput/surface.md)
  An input surface object that your Core Image Processor Kernel can read from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/pixelbuffer)*