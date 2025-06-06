# MEVideoDecoderExtension

**Framework**: MediaExtension  
**Kind**: protocol

A protocol that defines a factory to create new video decoders for a codec type that the extension implements.

**Availability**:
- macOS 14.0+

## Declaration

```swift
protocol MEVideoDecoderExtension : NSObjectProtocol
```

#### Discussion

This protocol provides a factory method to create a new [`MEVideoDecoder`](mevideodecoder.md) instance for a codecType implemented by the extension. A single [`MEVideoDecoderExtension`](mevideodecoderextension.md) is instantiated by the `VideoToolbox`, and will be called to create individual [`MEVideoDecoder`](mevideodecoder.md) instances as needed. If the codecType or `FormatDescription` passed to [`makeVideoDecoder(codecType:videoFormatDescription:videoDecoderSpecifications:pixelBufferManager:)`](mevideodecoderextension/makevideodecoder(codectype:videoformatdescription:videodecoderspecifications:pixelbuffermanager:).md) is not compatible with the [`MEVideoDecoder`](mevideodecoder.md) implementation, the factory call should fail and return [`MEError.Code.unsupportedFeature`](meerror-swift.struct/code/unsupportedfeature.md).

## Topics

### Creating a video decoder
- [init()](mevideodecoderextension/init.md)
  Creates a new video decoder factory.
- [func makeVideoDecoder(codecType: CMVideoCodecType, videoFormatDescription: CMVideoFormatDescription, videoDecoderSpecifications: [String : Any], pixelBufferManager: MEVideoDecoderPixelBufferManager) throws -> any MEVideoDecoder](mevideodecoderextension/makevideodecoder(codectype:videoformatdescription:videodecoderspecifications:pixelbuffermanager:).md)
  Creates a new video decoder that matches the codec type, format description, decoder specifications, and pixel buffer manager that you specify.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MEVideoDecoder](mevideodecoder.md)
  A protocol that defines the requirements for a video decoder.
- [class MEDecodeFrameOptions](medecodeframeoptions.md)
  An object that guides the video decoder operation on a per-frame basis.
- [class MEVideoDecoderPixelBufferManager](mevideodecoderpixelbuffermanager.md)
  Describes pixel buffer requirements and creates new pixel buffers.
- [Video decoder property list dictionary](video-decoder-property-list-dictionary.md)
  Include a property list dictionary to describe a video decoder.
- [Video decoder entitlement](video-decoder-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension video decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoderextension)*