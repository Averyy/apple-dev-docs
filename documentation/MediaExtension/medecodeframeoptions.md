# MEDecodeFrameOptions

**Framework**: MediaExtension  
**Kind**: class

An object that guides the video decoder operation on a per-frame basis.

**Availability**:
- macOS 14.0+

## Declaration

```swift
class MEDecodeFrameOptions
```

## Topics

### Inspecting frame decoding options
- [var doNotOutputFrame: Bool](medecodeframeoptions/donotoutputframe.md)
  A Boolean value that hints to the decoder whether or not it should emit an image buffer for the frame.
- [var realTimePlayback: Bool](medecodeframeoptions/realtimeplayback.md)
  A Boolean value that hints to the decoder to use a low-power mode that can’t decode faster than 1x real-time.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MEVideoDecoder](mevideodecoder.md)
  A protocol that defines the requirements for a video decoder.
- [protocol MEVideoDecoderExtension](mevideodecoderextension.md)
  A protocol that defines a factory to create new video decoders for a codec type that the extension implements.
- [class MEVideoDecoderPixelBufferManager](mevideodecoderpixelbuffermanager.md)
  Describes pixel buffer requirements and creates new pixel buffers.
- [Video decoder property list dictionary](video-decoder-property-list-dictionary.md)
  Include a property list dictionary to describe a video decoder.
- [Video decoder entitlement](video-decoder-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension video decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/medecodeframeoptions)*