# VideoReader.AsyncFrames

**Framework**: Create ML Components  
**Kind**: struct

An async sequence of video frames.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct AsyncFrames
```

#### Overview

This sequence allows iterating through the file only once.

## Topics

### Getting the properties
- [var count: Int?](videoreader/asyncframes/count.md)
  The number of frames. For this sequence count is always nil.
- [let frameSize: CGSize](videoreader/asyncframes/framesize.md)
  The frame size.
- [let nominalFrameRate: Float](videoreader/asyncframes/nominalframerate.md)
  The nominal frame rate.
- [let timescale: CMTimeScale](videoreader/asyncframes/timescale.md)
  The timescale of the video track.
- [let url: URL](videoreader/asyncframes/url.md)
  The video file URL, used when throwing an error.
- [let videoDuration: CMTime](videoreader/asyncframes/videoduration.md)
  The video duration.
### Creating an iterator
- [func makeAsyncIterator() -> VideoReader.AsyncFrames.Iterator](videoreader/asyncframes/makeasynciterator.md)
  Constructs an iterator.
- [VideoReader.AsyncFrames.Iterator](videoreader/asyncframes/iterator.md)
  An async iterator of video frames.
- [VideoReader.AsyncFrames.AsyncIterator](videoreader/asyncframes/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [VideoReader.AsyncFrames.Feature](videoreader/asyncframes/feature.md)
  The feature type.
### Type Aliases
- [VideoReader.AsyncFrames.Element](videoreader/asyncframes/element.md)
  The type of element produced by this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](videoreader/asyncframes/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
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
- [VideoReader.CameraAsyncBuffers](videoreader/cameraasyncbuffers.md)
  An async sequence of video frames.
- [VideoReader.CameraConfiguration](videoreader/cameraconfiguration.md)
  The configuration of the camera to pass to the `readCamera` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/videoreader/asyncframes)*