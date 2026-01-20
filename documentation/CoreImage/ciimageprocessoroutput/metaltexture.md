# metalTexture

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

A Metal texture object that can be bound for output using Metal.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var metalTexture: (any MTLTexture)? { get }
```

## See Also

- [var baseAddress: UnsafeMutableRawPointer](ciimageprocessoroutput/baseaddress.md)
  The base address of CPU memory that your Core Image Processor Kernel can write pixels to.
- [var pixelBuffer: CVPixelBuffer?](ciimageprocessoroutput/pixelbuffer.md)
  An output pixelBuffer object that your Core Image Processor Kernel can write to.
- [var surface: IOSurfaceRef](ciimageprocessoroutput/surface.md)
  An output surface object that your Core Image Processor Kernel can write to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/metaltexture)*