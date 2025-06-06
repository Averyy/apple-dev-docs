# AudioReader

**Framework**: Create ML Components  
**Kind**: struct

An audio file reader.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct AudioReader
```

## Topics

### Creating an audio reader
- [init(configuration: AudioReader.Configuration)](audioreader/init(configuration:).md)
  Creates an audio reader.
### Getting the properties
- [var configuration: AudioReader.Configuration](audioreader/configuration-swift.property.md)
  The audio reader configuration
### Managing buffers
- [AudioReader.AsyncBuffers](audioreader/asyncbuffers.md)
  An async sequence of audio buffers read from an audio file.
- [AudioReader.Configuration](audioreader/configuration-swift.struct.md)
  The configuration of the audio reader.
- [AudioReader.MicrophoneAsyncBuffers](audioreader/microphoneasyncbuffers.md)
  An async sequence of audio frames.
### Reading audio
- [static func read(contentsOf: URL, configuration: AudioReader.Configuration) throws -> AudioReader.AsyncBuffers](audioreader/read(contentsof:configuration:).md)
  Reads an audio file as an async sequence of audio buffers.
- [static func read<S>(S, configuration: AudioReader.Configuration) throws -> [AudioReader.AsyncBuffers]](audioreader/read(_:configuration:)-3nyda.md)
  Reads a sequence of files as an array of async sequences of audio buffers.
- [static func read<S, Annotation>(S, configuration: AudioReader.Configuration) throws -> [AnnotatedFeature<AudioReader.AsyncBuffers, Annotation>]](audioreader/read(_:configuration:)-4wma1.md)
  Reads a sequence of annotated files as a lazy sequence of results each containing an audio buffers or an error.
- [static func readMicrophone(configuration: AudioReader.Configuration) async throws -> AudioReader.MicrophoneAsyncBuffers](audioreader/readmicrophone(configuration:).md)
  Reads an async sequence of audio frames captured with a microphone.
### Applying
- [func applied(to: URL, eventHandler: EventHandler?) throws -> AudioReader.AsyncBuffers](audioreader/applied(to:eventhandler:).md)
  Reads an audio file as an async sequence of audio buffers.
### Type Aliases
- [AudioReader.Input](audioreader/input.md)
  The input type.
- [AudioReader.Output](audioreader/output.md)
  The output type.
### Default Implementations
- [Transformer Implementations](audioreader/transformer-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [Transformer](transformer.md)

## See Also

- [struct AudioFeaturePrint](audiofeatureprint.md)
  A stream transformer that extracts audio features from audio buffers.
- [struct AudioConvertingTransformer](audioconvertingtransformer.md)
  A transformer for audio conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreader)*