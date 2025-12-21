# AVSampleBufferAudioRenderer

**Framework**: AVFoundation  
**Kind**: class

An object used to decompress audio and play compressed or uncompressed audio.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class AVSampleBufferAudioRenderer
```

## Mentions

- [Implementing flexible enhanced buffering for your content](implementing-flexible-enhanced-buffering-for-your-content.md)
- [Supporting AirPlay in your app](supporting-airplay-in-your-app.md)

#### Overview

You must add an instance of this class to an [`AVSampleBufferRenderSynchronizer`](avsamplebufferrendersynchronizer.md) before queuing the first sample buffer.

## Topics

### Determining rendering status
- [var status: AVQueuedSampleBufferRenderingStatus](avsamplebufferaudiorenderer/status.md)
  The status of the audio renderer.
- [enum AVQueuedSampleBufferRenderingStatus](avqueuedsamplebufferrenderingstatus.md)
  The statuses for sample buffer rendering.
### Removing queued buffers
- [func flush(fromSourceTime: CMTime, completionHandler: (Bool) -> Void)](avsamplebufferaudiorenderer/flush(fromsourcetime:completionhandler:).md)
  Flushes queued sample buffers with presentation time stamps later than or equal to the specified time.
- [let AVSampleBufferAudioRendererFlushTimeKey: String](avsamplebufferaudiorendererflushtimekey.md)
  The key that indicates the presentation timestamp of the first queued sample that was flushed.
### Configuring time and pitch
- [var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm](avsamplebufferaudiorenderer/audiotimepitchalgorithm.md)
  The processing algorithm used to manage audio pitch at different rates.
- [struct AVAudioTimePitchAlgorithm](avaudiotimepitchalgorithm.md)
  An algorithm used to set the audio pitch as the rate changes.
### Configuring audio spatialization
- [var allowedAudioSpatializationFormats: AVAudioSpatializationFormats](avsamplebufferaudiorenderer/allowedaudiospatializationformats.md)
  The source audio channel layouts the audio renderer supports for spatialization.
### Managing audio output
- [var volume: Float](avsamplebufferaudiorenderer/volume.md)
  The current audio volume for the audio renderer.
- [var isMuted: Bool](avsamplebufferaudiorenderer/ismuted.md)
  A Boolean value that indicates whether audio for the renderer is in a muted state.
- [var audioOutputDeviceUniqueID: String?](avsamplebufferaudiorenderer/audiooutputdeviceuniqueid.md)
  The unique identifier of the output device used to play audio.
### Responding to errors
- [var error: (any Error)?](avsamplebufferaudiorenderer/error.md)
  The error that caused the renderer to no longer render sample buffers.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [AVQueuedSampleBufferRendering](avqueuedsamplebufferrendering.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol AVQueuedSampleBufferRendering](avqueuedsamplebufferrendering.md)
  Methods you can implement to enqueue sample buffers for presentation.
- [class AVSampleBufferRenderSynchronizer](avsamplebufferrendersynchronizer.md)
  An object used to synchronize multiple queued sample buffers to a single timeline.
- [class AVSampleBufferDisplayLayer](avsamplebufferdisplaylayer.md)
  An object that displays compressed or uncompressed video frames.
- [class AVSampleBufferVideoRenderer](avsamplebuffervideorenderer.md)
  An object that enqueues video sample buffers for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer)*