# VideoReader.CameraAsyncBuffers

**Framework**: Create ML Components  
**Kind**: struct

An async sequence of video frames.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct CameraAsyncBuffers
```

#### Overview

This sequence allows iterating through the camera frames. Only one iterator can be created per sequence.

## Topics

### Getting the capture session
- [var captureSession: AVCaptureSession](videoreader/cameraasyncbuffers/capturesession.md)
  The capture session.
### Getting the buffer count
- [var count: Int?](videoreader/cameraasyncbuffers/count.md)
  The number of frames. For this sequence count is always nil.
### Creating an iterator
- [func makeAsyncIterator() -> VideoReader.CameraAsyncBuffers.Iterator](videoreader/cameraasyncbuffers/makeasynciterator.md)
  Constructs an iterator.
- [VideoReader.CameraAsyncBuffers.Iterator](videoreader/cameraasyncbuffers/iterator.md)
  An async iterator of video frames.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TemporalSequence](temporalsequence.md)

## See Also

- [static read(_:)](videoreader/read(_:).md)
  Reads a sequence of annotated files as an array of annotated async sequences of video frames.
- [static func readCamera(configuration: VideoReader.CameraConfiguration) async throws -> VideoReader.CameraAsyncBuffers](videoreader/readcamera(configuration:).md)
  Reads an async sequence of video frames captured with a video camera.
- [static func read(contentsOf: URL) async throws -> VideoReader.AsyncFrames](videoreader/read(contentsof:).md)
  Reads a video file as an async sequence of video frames.
- [VideoReader.AsyncFrames](videoreader/asyncframes.md)
  An async sequence of video frames.
- [VideoReader.CameraConfiguration](videoreader/cameraconfiguration.md)
  The configuration of the camera to pass to the `readCamera` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreader/cameraasyncbuffers)*