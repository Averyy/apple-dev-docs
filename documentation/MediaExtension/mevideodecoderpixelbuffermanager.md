# MEVideoDecoderPixelBufferManager

**Framework**: MediaExtension  
**Kind**: class  
**Role**: Class

Describes pixel buffer requirements and creates new pixel buffers.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class MEVideoDecoderPixelBufferManager
```

```objc
@interface MEVideoDecoderPixelBufferManager : NSObject
```

## Discussion

Contains the interfaces that the [`MEVideoDecoder`](./mevideodecoder.md) uses for two tasks. First, to declare its set of requirements for output `CVPixelBuffer` objects in the form of a [`pixelBufferAttributes`](./mevideodecoderpixelbuffermanager/pixelbufferattributes.md) dictionary. Second, to create pixel buffers that match decoder output requirements but also satisfy [Video Toolbox](../VideoToolbox/VideoToolbox.md) and client requirements.

## Topics

### Creating a pixel buffer
- [var pixelBufferAttributes: [String : Any]](./mevideodecoderpixelbuffermanager/pixelbufferattributes.md)
  A dictionary that contains the attributes Video Toolbox uses to create a pixel buffer for the decoder.
- [func makePixelBuffer() throws -> CVPixelBuffer](./mevideodecoderpixelbuffermanager/makepixelbuffer%28%29.md)
  Generates a pixel buffer using the session’s pixel buffer pool.
### Registering Custom Pixel Formats
- [func registerCustomPixelFormat([String : Any])](./mevideodecoderpixelbuffermanager/registercustompixelformat%28_%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Video decoders
- [Supporting custom media formats and decoders](./supporting-custom-media-formats-and-decoders.md)
  Extend the media formats the system can open by providing a format reader and a video decoder.
- [protocol MEVideoDecoder](./mevideodecoder.md)
  A protocol that defines the requirements for a video decoder.
- [protocol MEVideoDecoderExtension](./mevideodecoderextension.md)
  A protocol that defines a factory to create new video decoders for a codec type that the extension implements.
- [class MEDecodeFrameOptions](./medecodeframeoptions.md)
  An object that guides the video decoder operation on a per-frame basis.
- [Video decoder property list dictionary](./video-decoder-property-list-dictionary.md)
  Include a property list dictionary to describe a video decoder.
- [Video decoder entitlement](./video-decoder-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension video decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mevideodecoderpixelbuffermanager)*