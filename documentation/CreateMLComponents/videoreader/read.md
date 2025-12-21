# read(_:)

**Framework**: Create ML Components  
**Kind**: method

Reads a sequence of annotated files as an array of annotated async sequences of video frames.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func read<S, Annotation>(_ annotatedFiles: S) async throws -> [AnnotatedFeature<VideoReader.AsyncFrames, Annotation>] where S : Sequence, Annotation : Equatable, Annotation : Sendable, S.Element == AnnotatedFeature<URL, Annotation>
```

#### Return Value

An array of annotated async sequences.

## Parameters

- `annotatedFiles`: A sequence of annotated URLs.

## See Also

- [static func readCamera(configuration: VideoReader.CameraConfiguration) async throws -> VideoReader.CameraAsyncBuffers](videoreader/readcamera(configuration:).md)
  Reads an async sequence of video frames captured with a video camera.
- [static func read(contentsOf: URL) async throws -> VideoReader.AsyncFrames](videoreader/read(contentsof:).md)
  Reads a video file as an async sequence of video frames.
- [VideoReader.AsyncFrames](videoreader/asyncframes.md)
  An async sequence of video frames.
- [VideoReader.CameraAsyncBuffers](videoreader/cameraasyncbuffers.md)
  An async sequence of video frames.
- [VideoReader.CameraConfiguration](videoreader/cameraconfiguration.md)
  The configuration of the camera to pass to the `readCamera` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreader/read(_:))*