# VideoReader.CameraAsyncBuffers

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

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

## Overview

This sequence allows iterating through the camera frames. Only one iterator can be created per sequence.

## Topics

### Getting the capture session
- [var captureSession: AVCaptureSession](./cameraasyncbuffers/capturesession.md)
  The capture session.
### Getting the buffer count
- [var count: Int?](./cameraasyncbuffers/count.md)
  The number of frames. For this sequence count is always nil.
### Creating an iterator
- [func makeAsyncIterator() -> VideoReader.CameraAsyncBuffers.Iterator](./cameraasyncbuffers/makeasynciterator%28%29.md)
  Constructs an iterator.
- [VideoReader.CameraAsyncBuffers.Iterator](./cameraasyncbuffers/iterator.md)
  An async iterator of video frames.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [TemporalSequence](../temporalsequence.md)

## See Also

### Reading
- [static read(_:)](./read%28_%29.md)
  Reads a sequence of annotated files as an array of annotated async sequences of video frames.
- [static func readCamera(configuration: VideoReader.CameraConfiguration) async throws -> VideoReader.CameraAsyncBuffers](./readcamera%28configuration%29.md)
  Reads an async sequence of video frames captured with a video camera.
- [static func read(contentsOf: URL) async throws -> VideoReader.AsyncFrames](./read%28contentsof%29.md)
  Reads a video file as an async sequence of video frames.
- [VideoReader.AsyncFrames](./asyncframes.md)
  An async sequence of video frames.
- [VideoReader.CameraConfiguration](./cameraconfiguration.md)
  The configuration of the camera to pass to the `readCamera` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreader/cameraasyncbuffers)*