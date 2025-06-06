# pixelBufferAttributes

**Framework**: MediaExtension  
**Kind**: property

A dictionary that contains the attributes Video Toolbox uses to create a pixel buffer for the decoder.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var pixelBufferAttributes: [String : Any] { get set }
```

#### Discussion

The decoder can update this dictionary before it requests a new pixel buffer.

## See Also

- [func makePixelBuffer() throws -> CVPixelBuffer](mevideodecoderpixelbuffermanager/makepixelbuffer.md)
  Generates a pixel buffer using the session’s pixel buffer pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoderpixelbuffermanager/pixelbufferattributes)*