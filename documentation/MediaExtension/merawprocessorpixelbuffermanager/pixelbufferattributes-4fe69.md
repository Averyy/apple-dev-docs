# pixelBufferAttributes

**Framework**: MediaExtension  
**Kind**: property

A dictionary that contains the attributes Video Toolbox uses to create a pixel buffer for the video RAW processor.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var pixelBufferAttributes: [String : any Sendable] { get set }
```

#### Discussion

The processor can update this dictionary before it requests a new pixel buffer.

## See Also

- [func makePixelBuffer() throws -> CVPixelBuffer](merawprocessorpixelbuffermanager/makepixelbuffer.md)
  Generates a pixel buffer using the session’s pixel buffer pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessorpixelbuffermanager/pixelbufferattributes-4fe69)*