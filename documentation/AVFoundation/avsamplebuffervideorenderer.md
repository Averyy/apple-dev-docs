# AVSampleBufferVideoRenderer

**Framework**: AVFoundation  
**Kind**: class

An object that enqueues video sample buffers for rendering.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class AVSampleBufferVideoRenderer
```

## Topics

### Flushing the renderer
- [var requiresFlushToResumeDecoding: Bool](avsamplebuffervideorenderer/requiresflushtoresumedecoding.md)
  A Boolean value that Indicates whether the renderer requires flushing to continue decoding frames.
- [class let requiresFlushToResumeDecodingDidChangeNotification: NSNotification.Name](avsamplebuffervideorenderer/requiresflushtoresumedecodingdidchangenotification.md)
  A notification that indicates that the video renderer requires flushing to continue rendering sample buffers.
- [let AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotificationRequiresFlushKey: String](avsamplebuffervideorendererrequiresflushtoresumedecodingdidchangenotificationrequiresflushkey.md)
- [func flush(removingDisplayedImage: Bool, completionHandler: (() -> Void)?)](avsamplebuffervideorenderer/flush(removingdisplayedimage:completionhandler:).md)
  Tells the video renderer to discard pending enqueued sample buffers.
### Setting presentation time expectations
- [var presentationTimeExpectation: AVSampleBufferVideoRenderer.PresentationTimeExpectation](avsamplebuffervideorenderer/presentationtimeexpectation-swift.property.md)
- [AVSampleBufferVideoRenderer.PresentationTimeExpectation](avsamplebuffervideorenderer/presentationtimeexpectation-swift.enum.md)
  Options that specify the expected presentation time stamps of enqueue samples.
### Inspecting the status
- [var status: AVQueuedSampleBufferRenderingStatus](avsamplebuffervideorenderer/status.md)
  A status value that indicates whether this object can enqueue and render sample buffers.
- [var error: (any Error)?](avsamplebuffervideorenderer/error.md)
  An object the describes the error that caused the rendering failure.
### Accessing the pixel buffer
- [func displayedPixelBuffer() -> CVPixelBuffer?](avsamplebuffervideorenderer/displayedpixelbuffer.md)
- [var recommendedPixelBufferAttributes: CVPixelBufferAttributes](avsamplebuffervideorenderer/recommendedpixelbufferattributes-6zrqb.md)
  Recommended pixel buffer attributes for optimal performance when using CMSampleBuffers containing CVPixelbuffers.
### Handling decode failures
- [class let didFailToDecodeNotification: NSNotification.Name](avsamplebuffervideorenderer/didfailtodecodenotification.md)
  A notification that indicates the video renderer fails to decode a sample buffer.
- [class let didFailToDecodeNotificationErrorKey: String](avsamplebuffervideorenderer/didfailtodecodenotificationerrorkey.md)
  A key to retrieve an error object that provides the details of the failure.
### Capturing performance metrics
- [func loadVideoPerformanceMetrics(completionHandler: (AVVideoPerformanceMetrics?) -> Void)](avsamplebuffervideorenderer/loadvideoperformancemetrics(completionhandler:).md)
### Classes
- [AVSampleBufferVideoRenderer.Receiver](avsamplebuffervideorenderer/receiver.md)
### Instance Properties
- [var hasSufficientMediaDataForReliablePlaybackStart: Bool](avsamplebuffervideorenderer/hassufficientmediadataforreliableplaybackstart.md)
  Indicates whether the enqueued media data meets the renderer’s preroll level.
- [var isReadyForMoreMediaData: Bool](avsamplebuffervideorenderer/isreadyformoremediadata.md)
  Indicates the readiness of the receiver to accept more sample buffers.
### Instance Methods
- [func enqueue(CMSampleBuffer)](avsamplebuffervideorenderer/enqueue(_:).md)
  Sends a sample buffer in order to render its contents.
- [func flush()](avsamplebuffervideorenderer/flush.md)
  Instructs the receiver to discard pending enqueued sample buffers.
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](avsamplebuffervideorenderer/requestmediadatawhenready(on:using:).md)
  Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for playback.
- [func stopRequestingMediaData()](avsamplebuffervideorenderer/stoprequestingmediadata.md)
  Cancels any current requestMediaDataWhenReadyOnQueue:usingBlock: call.

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
- [class AVSampleBufferAudioRenderer](avsamplebufferaudiorenderer.md)
  An object used to decompress audio and play compressed or uncompressed audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer)*