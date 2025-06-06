# makePixelBuffer()

**Framework**: MediaExtension  
**Kind**: method

Generates a pixel buffer using the session’s pixel buffer pool.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func makePixelBuffer() throws -> CVPixelBuffer
```

#### Return Value

A pixel buffer that’s compatible with the extension’s most recently set pixel buffer attributes.

## See Also

- [var pixelBufferAttributes: [String : any Sendable]](merawprocessorpixelbuffermanager/pixelbufferattributes-4fe69.md)
  A dictionary that contains the attributes Video Toolbox uses to create a pixel buffer for the video RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessorpixelbuffermanager/makepixelbuffer())*