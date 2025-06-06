# read(_:configuration:)

**Framework**: Create ML Components  
**Kind**: method

Reads a sequence of annotated files as a lazy sequence of results each containing an audio buffers or an error.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func read<S, Annotation>(_ annotatedFiles: S, configuration: AudioReader.Configuration = .init()) throws -> [AnnotatedFeature<AudioReader.AsyncBuffers, Annotation>] where S : Sequence, Annotation : Equatable, Annotation : Sendable, S.Element == AnnotatedFeature<URL, Annotation>
```

#### Return Value

An array of annotated async sequences.

## Parameters

- `annotatedFiles`: A sequence of annotated URLs.
- `configuration`: The configuration for reading buffers.

## See Also

- [static func read(contentsOf: URL, configuration: AudioReader.Configuration) throws -> AudioReader.AsyncBuffers](audioreader/read(contentsof:configuration:).md)
  Reads an audio file as an async sequence of audio buffers.
- [static func read<S>(S, configuration: AudioReader.Configuration) throws -> [AudioReader.AsyncBuffers]](audioreader/read(_:configuration:)-3nyda.md)
  Reads a sequence of files as an array of async sequences of audio buffers.
- [static func readMicrophone(configuration: AudioReader.Configuration) async throws -> AudioReader.MicrophoneAsyncBuffers](audioreader/readmicrophone(configuration:).md)
  Reads an async sequence of audio frames captured with a microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreader/read(_:configuration:)-4wma1)*