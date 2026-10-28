# read(_:configuration:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Type Method

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

**Other overloads**:

```swift
static func read<S, Annotation>(_ annotatedFiles: S, configuration: AudioReader.Configuration = .init()) throws -> [AnnotatedFeature<AudioReader.AsyncBuffers, Annotation>] where S : Sequence, Annotation : Equatable, Annotation : Sendable, S.Element == AnnotatedFeature<URL, Annotation>
```

## Return Value

An array of async sequences of audio buffers.

## Parameters

- `files`: A sequence of URLs.
- `configuration`: The configuration for reading buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audioreader/read(_:configuration:)-3nyda)*