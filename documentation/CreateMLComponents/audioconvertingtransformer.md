# AudioConvertingTransformer

**Framework**: Create ML Components  
**Kind**: struct

A transformer for audio conversion.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct AudioConvertingTransformer
```

## Topics

### Creating the transformer
- [init(targetFormat: AVAudioFormat)](audioconvertingtransformer/init(targetformat:).md)
  Creates an audio conversion transformer to convert the format of the buffers.
### Getting the properties
- [let targetFormat: AVAudioFormat](audioconvertingtransformer/targetformat.md)
  The target audio format for the output buffers. It must have an AVAudioPCMFormat as its common format type.
### Applying the transformer
- [func applied(to: AVAudioPCMBuffer, eventHandler: EventHandler?) throws -> AVAudioPCMBuffer](audioconvertingtransformer/applied(to:eventhandler:).md)
  Performs conversion of the input audio buffer.
### Type Aliases
- [AudioConvertingTransformer.Input](audioconvertingtransformer/input.md)
  The input type.
- [AudioConvertingTransformer.Output](audioconvertingtransformer/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](audioconvertingtransformer/customdebugstringconvertible-implementations.md)
- [Transformer Implementations](audioconvertingtransformer/transformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Transformer](transformer.md)

## See Also

- [struct AudioReader](audioreader.md)
  An audio file reader.
- [struct AudioFeaturePrint](audiofeatureprint.md)
  A stream transformer that extracts audio features from audio buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioconvertingtransformer)*