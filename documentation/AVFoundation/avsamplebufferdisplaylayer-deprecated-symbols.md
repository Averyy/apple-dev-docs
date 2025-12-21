# Deprecated symbols

**Framework**: AVFoundation

Review unsupported symbols and their replacements.

## Topics

### Initiating media data requests
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](avsamplebufferdisplaylayer/requestmediadatawhenready(on:using:).md)
  Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for display.
- [var isReadyForMoreMediaData: Bool](avsamplebufferdisplaylayer/isreadyformoremediadata.md)
  A Boolean value that indicates the readiness of the layer to accept more sample buffers.
- [var requiresFlushToResumeDecoding: Bool](avsamplebufferdisplaylayer/requiresflushtoresumedecoding.md)
  A Boolean value that indicates whether the layer needs to flush its state to continue decoding frames.
- [func stopRequestingMediaData()](avsamplebufferdisplaylayer/stoprequestingmediadata.md)
  Cancels any current media data request.
- [var hasSufficientMediaDataForReliablePlaybackStart: Bool](avsamplebufferdisplaylayer/hassufficientmediadataforreliableplaybackstart.md)
  A Boolean value that indicates whether the enqueued media data meets the renderer’s preroll level.
### Flushing sample buffers
- [func flush()](avsamplebufferdisplaylayer/flush.md)
  Instructs the layer to discard any enqueued sample buffers that are pending.
- [func flushAndRemoveImage()](avsamplebufferdisplaylayer/flushandremoveimage.md)
  Instructs the layer to discard pending enqueued sample buffers and remove any currently displayed image.
### Configuring the timebase
- [var timebase: CMTimebase](avsamplebufferdisplaylayer/timebase.md)
  The renderer’s timebase, which determines how the layer interprets time stamps.
### Enqueuing the sample buffer
- [func enqueue(CMSampleBuffer)](avsamplebufferdisplaylayer/enqueue(_:).md)
  Sends a sample buffer for display.
### Getting display layer settings
- [var status: AVQueuedSampleBufferRenderingStatus](avsamplebufferdisplaylayer/status.md)
  The ability of the display layer to be used for enqueuing sample buffers.
- [enum AVQueuedSampleBufferRenderingStatus](avqueuedsamplebufferrenderingstatus.md)
  The statuses for sample buffer rendering.
### Handling errors
- [var error: (any Error)?](avsamplebufferdisplaylayer/error.md)
  The error that caused the failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer-deprecated-symbols)*