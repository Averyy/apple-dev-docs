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
### Creating an iterator
- [func makeAsyncIterator() -> VideoReader.CameraAsyncBuffers.Iterator](videoreader/cameraasyncbuffers/makeasynciterator.md)
  Constructs an iterator.
- [VideoReader.CameraAsyncBuffers.Iterator](videoreader/cameraasyncbuffers/iterator.md)
  An async iterator of video frames.
- [VideoReader.CameraAsyncBuffers.AsyncIterator](videoreader/cameraasyncbuffers/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [VideoReader.CameraAsyncBuffers.Feature](videoreader/cameraasyncbuffers/feature.md)
  The feature type.
### Instance Properties
- [var count: Int?](videoreader/cameraasyncbuffers/count.md)
  The number of frames. For this sequence count is always nil.
### Type Aliases
- [VideoReader.CameraAsyncBuffers.Element](videoreader/cameraasyncbuffers/element.md)
  The type of element produced by this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](videoreader/cameraasyncbuffers/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TemporalSequence](temporalsequence.md)

## See Also

- [static func read<S>(S) async throws -> [VideoReader.AsyncFrames]](videoreader/read(_:)-4oyjh.md)
  Reads a sequence of files as an array of async sequences of video frames.
- [static func read<S, Annotation>(S) async throws -> [AnnotatedFeature<VideoReader.AsyncFrames, Annotation>]](videoreader/read(_:)-sluv.md)
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