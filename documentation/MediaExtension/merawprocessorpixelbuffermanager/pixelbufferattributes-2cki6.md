# pixelBufferAttributes

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

A dictionary that contains the attributes Video Toolbox uses to create a pixel buffer for the video RAW processor.

**Availability**:
- macOS 15.0+

## Declaration

```objc
@property (nonatomic, copy, readwrite) NSDictionary<NSString *,id> * pixelBufferAttributes;
```

#### Discussion

The processor can update this dictionary before it requests a new pixel buffer.

## See Also

### Creating a pixel buffer
- [func makePixelBuffer() throws -> CVPixelBuffer](./makepixelbuffer%28%29.md)
  Generates a pixel buffer using the session’s pixel buffer pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessorpixelbuffermanager/pixelbufferattributes-2cki6)*