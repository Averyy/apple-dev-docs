# read(_:configuration:)

**Framework**: Create ML Components  
**Kind**: method

Reads a sequence of files as an array of async sequences of audio buffers.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func read<S>(_ files: S, configuration: AudioReader.Configuration = .init()) throws -> [AudioReader.AsyncBuffers] where S : Sequence, S.Element == URL
```

#### Return Value

An array of async sequences of audio buffers.

## Parameters

- `files`: A sequence of URLs.
- `configuration`: The configuration for reading buffers.

## See Also

- [static func read(contentsOf: URL, configuration: AudioReader.Configuration) throws -> AudioReader.AsyncBuffers](audioreader/read(contentsof:configuration:).md)
  Reads an audio file as an async sequence of audio buffers.
- [static func read<S, Annotation>(S, configuration: AudioReader.Configuration) throws -> [AnnotatedFeature<AudioReader.AsyncBuffers, Annotation>]](audioreader/read(_:configuration:)-4wma1.md)
  Reads a sequence of annotated files as a lazy sequence of results each containing an audio buffers or an error.
- [static func readMicrophone(configuration: AudioReader.Configuration) async throws -> AudioReader.MicrophoneAsyncBuffers](audioreader/readmicrophone(configuration:).md)
  Reads an async sequence of audio frames captured with a microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreader/read(_:configuration:)-3nyda)*