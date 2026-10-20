# read(_:configuration:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Type Method

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

**Other overloads**:

```swift
static func read<S>(_ files: S, configuration: AudioReader.Configuration = .init()) throws -> [AudioReader.AsyncBuffers] where S : Sequence, S.Element == URL
```

#### Return Value

An array of annotated async sequences.

## Parameters

- `annotatedFiles`: A sequence of annotated URLs.
- `configuration`: The configuration for reading buffers.

## See Also

### Reading audio
- [static func read(contentsOf: URL, configuration: AudioReader.Configuration) throws -> AudioReader.AsyncBuffers](./read%28contentsof,configuration%29.md)
  Reads an audio file as an async sequence of audio buffers.
- [static func readMicrophone(configuration: AudioReader.Configuration) async throws -> AudioReader.MicrophoneAsyncBuffers](./readmicrophone%28configuration%29.md)
  Reads an async sequence of audio frames captured with a microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreader/read(_:configuration:))*