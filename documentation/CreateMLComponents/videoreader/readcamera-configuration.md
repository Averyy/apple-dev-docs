# readCamera(configuration:)

**Framework**: Create ML Components  
**Kind**: method

Reads an async sequence of video frames captured with a video camera.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
static func readCamera(configuration: VideoReader.CameraConfiguration) async throws -> VideoReader.CameraAsyncBuffers
```

#### Return Value

An async sequence of camera video frames.

## Parameters

- `configuration`: The camera configuration

## See Also

- [static read(_:)](videoreader/read(_:).md)
  Reads a sequence of annotated files as an array of annotated async sequences of video frames.
- [static func read(contentsOf: URL) async throws -> VideoReader.AsyncFrames](videoreader/read(contentsof:).md)
  Reads a video file as an async sequence of video frames.
- [VideoReader.AsyncFrames](videoreader/asyncframes.md)
  An async sequence of video frames.
- [VideoReader.CameraAsyncBuffers](videoreader/cameraasyncbuffers.md)
  An async sequence of video frames.
- [VideoReader.CameraConfiguration](videoreader/cameraconfiguration.md)
  The configuration of the camera to pass to the `readCamera` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreader/readcamera(configuration:))*