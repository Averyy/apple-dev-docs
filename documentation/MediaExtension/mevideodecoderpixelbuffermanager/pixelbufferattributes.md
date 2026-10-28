# pixelBufferAttributes

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

A dictionary that contains the attributes Video Toolbox uses to create a pixel buffer for the decoder.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var pixelBufferAttributes: [String : Any] { get set }
```

```objc
@property (nonatomic, copy, readwrite) NSDictionary<NSString *,id> * pixelBufferAttributes;
```

## Discussion

The decoder can update this dictionary before it requests a new pixel buffer.

## See Also

### Creating a pixel buffer
- [func makePixelBuffer() throws -> CVPixelBuffer](./makepixelbuffer%28%29.md)
  Generates a pixel buffer using the session’s pixel buffer pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoderpixelbuffermanager/pixelbufferattributes)*