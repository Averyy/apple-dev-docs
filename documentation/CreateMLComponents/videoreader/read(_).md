# read(_:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Type Method

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

**Other overloads**:

```swift
static func read<S>(_ files: S) async throws -> [VideoReader.AsyncFrames] where S : Sequence, S.Element == URL
```

## Return Value

An array of annotated async sequences.

## Parameters

- `annotatedFiles`: A sequence of annotated URLs.

## See Also

### Reading
- [static func readCamera(configuration: VideoReader.CameraConfiguration) async throws -> VideoReader.CameraAsyncBuffers](./readcamera%28configuration%29.md)
  Reads an async sequence of video frames captured with a video camera.
- [static func read(contentsOf: URL) async throws -> VideoReader.AsyncFrames](./read%28contentsof%29.md)
  Reads a video file as an async sequence of video frames.
- [VideoReader.AsyncFrames](./asyncframes.md)
  An async sequence of video frames.
- [VideoReader.CameraAsyncBuffers](./cameraasyncbuffers.md)
  An async sequence of video frames.
- [VideoReader.CameraConfiguration](./cameraconfiguration.md)
  The configuration of the camera to pass to the `readCamera` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreader/read(_:))*