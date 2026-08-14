# AVPlayerItemSampleBufferOutput

**Framework**: AVFoundation  
**Kind**: class

[`AVPlayerItemSampleBufferOutput`](avplayeritemsamplebufferoutput.md) delivers `CMSampleBuffers` for [`AVPlayerItem`](avplayeritem.md) playback.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
class AVPlayerItemSampleBufferOutput
```

#### Overview

Playback only happens when the [`AVPlayerItem`](avplayeritem.md) is the current item of its [`AVPlayer`](avplayer.md).

Create an [`AVPlayerItemSampleBufferOutput`](avplayeritemsamplebufferoutput.md) with a [`AVPlayerItemSampleBufferOutputAudioConfiguration`](avplayeritemsamplebufferoutputaudioconfiguration.md) to configure it to deliver `CMSampleBuffers` containing the decoded audio, and attach it to the [`AVPlayerItem`](avplayeritem.md) using `-[AVPlayerItem addOutput:]`; the audio will be in the format specified by the configuration object’s `requestedAudioFormat`.

Note that [`AVPlayerItemSampleBufferOutput`](avplayeritemsamplebufferoutput.md) may be used to pull `CMSampleBuffers` far ahead of the current play time.  Practical use requires clients to monitor the item timebase time, and pause pulling when they have received CMSampleBuffers sufficient to prepare for near-term-future playback or processing.

Marker-only `CMSampleBuffers` may be among those returned; you can detect and skip these by testing whether `CMSampleBufferGetNumSamples(sampleBuffer) == 0`.

The output `CMSampleBuffers` will have appropriate OutputPresentationTimeStamps for playback, but beyond that, synchronizing presentation to the AVPlayerItem’s timebase is entirely up to the client.

Currently supported for HLS `AVPlayerItems` only, and only for delivering decoded PCM audio.

## Topics

### Creating a sample buffer output
- [init(configuration: AVPlayerItemSampleBufferOutputConfiguration?)](avplayeritemsamplebufferoutput/init(configuration:).md)
  Initializes an instance of [`AVPlayerItemSampleBufferOutput`](avplayeritemsamplebufferoutput.md).
### Retrieving sample buffers
- [func nextAvailableSampleBuffer() -> AVPlayerItemSampleBufferOutput.SampleBufferInSequence?](avplayeritemsamplebufferoutput/nextavailablesamplebuffer.md)
  Returns the next sample buffer if it is already available.
- [func nextSampleBuffer() async -> AVPlayerItemSampleBufferOutput.SampleBufferInSequence?](avplayeritemsamplebufferoutput/nextsamplebuffer.md)
  Returns next sample buffer once it becomes available.
- [AVPlayerItemSampleBufferOutput.SampleBufferInSequence](avplayeritemsamplebufferoutput/samplebufferinsequence.md)
  Holds the information necessary for processing generated sample buffers.

## Relationships

### Inherits From
- [AVPlayerItemOutput](avplayeritemoutput.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class AVPlayerVideoOutput](avplayervideooutput.md)
  An object that receives video data from a player object.
- [class AVVideoOutputSpecification](avvideooutputspecification.md)
  An object that specifies the pixel buffer attributes and tag collections handled by a player video output.
- [class AVPlayerItemOutput](avplayeritemoutput.md)
  An abstract class that defines the common interface to output media data from a player item.
- [class AVPlayerItemVideoOutput](avplayeritemvideooutput.md)
  An object that outputs video frames from a player item.
- [class AVPlayerItemLegibleOutput](avplayeritemlegibleoutput.md)
  An object that vends attributed strings for media with a legible characteristic.
- [class AVPlayerItemRenderedLegibleOutput](avplayeritemrenderedlegibleoutput.md)
  A player item output that vends media with a legible characteristic as rendered pixel buffers.
- [class AVRenderedCaptionImage](avrenderedcaptionimage.md)
  An object that provides a rendered pixel buffer and its position in pixels.
- [class AVPlayerItemMetadataOutput](avplayeritemmetadataoutput.md)
  An object that vends collections of metadata items that a player item’s tracks carry.
- [protocol AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md)
  A protocol that defines the methods to implement to respond to changes in the media data sequence.
- [class AVPlayerItemSampleBufferOutputConfiguration](avplayeritemsamplebufferoutputconfiguration.md)
  Configuration options specified when creating an [`AVPlayerItemSampleBufferOutput`](avplayeritemsamplebufferoutput.md).
- [class AVPlayerItemSampleBufferOutputAudioConfiguration](avplayeritemsamplebufferoutputaudioconfiguration.md)
  Audio-specific configuration options specified when creating an [`AVPlayerItemSampleBufferOutput`](avplayeritemsamplebufferoutput.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput)*