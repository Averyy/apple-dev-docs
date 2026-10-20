# pixelBuffer

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An output pixelBuffer object that your Core Image Processor Kernel can write to.

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

```objc
@property (nonatomic, readonly, nullable) CVPixelBufferRef pixelBuffer;
```

## See Also

### Providing Output Image Data
- [var baseAddress: UnsafeMutableRawPointer](./baseaddress.md)
  The base address of CPU memory that your Core Image Processor Kernel can write pixels to.
- [var metalTexture: (any MTLTexture)?](./metaltexture.md)
  A Metal texture object that can be bound for output using Metal.
- [var surface: IOSurfaceRef](./surface.md)
  An output surface object that your Core Image Processor Kernel can write to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/pixelbuffer)*