# read(contentsOf:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Type Method

Reads a video file as an async sequence of video frames.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func read(contentsOf url: URL) async throws -> VideoReader.AsyncFrames
```

#### Return Value

An async sequence of `VideoFrames`.

## Parameters

- `url`: A video file URL.

## See Also

### Reading
- [static read(_:)](./read%28_%29.md)
  Reads a sequence of annotated files as an array of annotated async sequences of video frames.
- [static func readCamera(configuration: VideoReader.CameraConfiguration) async throws -> VideoReader.CameraAsyncBuffers](./readcamera%28configuration%29.md)
  Reads an async sequence of video frames captured with a video camera.
- [VideoReader.AsyncFrames](./asyncframes.md)
  An async sequence of video frames.
- [VideoReader.CameraAsyncBuffers](./cameraasyncbuffers.md)
  An async sequence of video frames.
- [VideoReader.CameraConfiguration](./cameraconfiguration.md)
  The configuration of the camera to pass to the `readCamera` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreader/read(contentsof:))*