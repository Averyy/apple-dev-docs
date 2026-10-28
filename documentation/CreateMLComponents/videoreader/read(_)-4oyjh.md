# read(_:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Type Method

Reads a sequence of files as an array of async sequences of video frames.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func read<S>(_ files: S) async throws -> [VideoReader.AsyncFrames] where S : Sequence, S.Element == URL
```

**Other overloads**:

```swift
static func read<S, Annotation>(_ annotatedFiles: S) async throws -> [AnnotatedFeature<VideoReader.AsyncFrames, Annotation>] where S : Sequence, Annotation : Equatable, Annotation : Sendable, S.Element == AnnotatedFeature<URL, Annotation>
```

## Return Value

An array of async sequences of video frames.

## Parameters

- `files`: A sequence of URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreader/read(_:)-4oyjh)*