# readCamera(configuration:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Type Method

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

### Reading
- [static read(_:)](./read%28_%29.md)
  Reads a sequence of annotated files as an array of annotated async sequences of video frames.
- [static func read(contentsOf: URL) async throws -> VideoReader.AsyncFrames](./read%28contentsof%29.md)
  Reads a video file as an async sequence of video frames.
- [VideoReader.AsyncFrames](./asyncframes.md)
  An async sequence of video frames.
- [VideoReader.CameraAsyncBuffers](./cameraasyncbuffers.md)
  An async sequence of video frames.
- [VideoReader.CameraConfiguration](./cameraconfiguration.md)
  The configuration of the camera to pass to the `readCamera` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreader/readcamera(configuration:))*