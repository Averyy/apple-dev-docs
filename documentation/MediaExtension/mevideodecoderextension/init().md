# init()

**Framework**: MediaExtension  
**Kind**: init  
**Role**: Initializer  
**Required**: Yes

Creates a new video decoder factory.

**Availability**:
- macOS 14.0+

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

## See Also

### Creating a video decoder
- [func makeVideoDecoder(codecType: CMVideoCodecType, videoFormatDescription: CMVideoFormatDescription, videoDecoderSpecifications: [String : Any], pixelBufferManager: MEVideoDecoderPixelBufferManager) throws -> any MEVideoDecoder](./makevideodecoder%28codectype,videoformatdescription,videodecoderspecifications,pixelbuffermanager%29.md)
  Creates a new video decoder that matches the codec type, format description, decoder specifications, and pixel buffer manager that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoderextension/init())*