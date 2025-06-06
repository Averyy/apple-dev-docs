# AVSampleBufferDisplayLayer

**Framework**: AVFoundation  
**Kind**: class

An object that displays compressed or uncompressed video frames.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
class AVSampleBufferDisplayLayer
```

## Topics

### Accessing the video renderer
- [var sampleBufferRenderer: AVSampleBufferVideoRenderer](avsamplebufferdisplaylayer/samplebufferrenderer.md)
  An object that enqueues video sample buffers for rendering.
### Configuring the layer
- [var isReadyForDisplay: Bool](avsamplebufferdisplaylayer/isreadyfordisplay.md)
  A Boolean value that indicates whether the first video frame is ready for display.
- [var controlTimebase: CMTimebase?](avsamplebufferdisplaylayer/controltimebase.md)
  A timebase that determines how the layer interprets timestamps.
- [var videoGravity: AVLayerVideoGravity](avsamplebufferdisplaylayer/videogravity.md)
  A value that indicates how the layer displays video within its bounds.
- [struct AVLayerVideoGravity](avlayervideogravity.md)
  A structure that defines how a layer displays a player’s visual content within the layer’s bounds.
### Protecting content
- [var preventsCapture: Bool](avsamplebufferdisplaylayer/preventscapture.md)
  A Boolean value that indicates whether the layer protects against screen capture.
- [var isOutputObscuredDueToInsufficientExternalProtection: Bool](avsamplebufferdisplaylayer/isoutputobscuredduetoinsufficientexternalprotection.md)
  A Boolean value that indicates whether the system obscures decoded output due to insufficient external protection on the current device.
### Preventing backgrounding
- [var preventsDisplaySleepDuringVideoPlayback: Bool](avsamplebufferdisplaylayer/preventsdisplaysleepduringvideoplayback.md)
  A Boolean value that indicates whether the layer prevents the system from sleeping during video playback.
- [var preventsAutomaticBackgroundingDuringVideoPlayback: Bool](avsamplebufferdisplaylayer/preventsautomaticbackgroundingduringvideoplayback.md)
  A Boolean value that indicates whether video playback prevents the system from automatically backgrounding an app.
### Handling errors
- [static let AVSampleBufferDisplayLayerFailedToDecode: NSNotification.Name](../foundation/nsnotification/name/1390290-avsamplebufferdisplaylayerfailed.md)
  A notification the system posts when a sample buffer display layer fails to decode.
- [let AVSampleBufferDisplayLayerFailedToDecodeNotificationErrorKey: String](avsamplebufferdisplaylayerfailedtodecodenotificationerrorkey.md)
  The key for the corresponding error.
### Deprecated
- [Deprecated Symbols](avsamplebufferdisplaylayer-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## Relationships

### Inherits From
- [CALayer](../QuartzCore/CALayer.md)
### Conforms To
- [AVQueuedSampleBufferRendering](avqueuedsamplebufferrendering.md)
- [CAMediaTiming](../QuartzCore/CAMediaTiming.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [protocol AVQueuedSampleBufferRendering](avqueuedsamplebufferrendering.md)
  Methods you can implement to enqueue sample buffers for presentation.
- [class AVSampleBufferRenderSynchronizer](avsamplebufferrendersynchronizer.md)
  An object used to synchronize multiple queued sample buffers to a single timeline.
- [class AVSampleBufferVideoRenderer](avsamplebuffervideorenderer.md)
  An object that enqueues video sample buffers for rendering.
- [class AVSampleBufferAudioRenderer](avsamplebufferaudiorenderer.md)
  An object used to decompress audio and play compressed or uncompressed audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer)*