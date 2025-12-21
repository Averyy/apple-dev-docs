# AVAssetWriterInput.CaptionReceiver

**Framework**: AVFoundation  
**Kind**: class

Provides an interface for writing caption data to an input.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
class CaptionReceiver
```

## Topics

### Appending captions
- [func append(AVCaptionGroup) async throws](avassetwriterinput/captionreceiver/append(_:)-4opbd.md)
  Suspends until the input is ready for more media data, then appends the caption group.
- [func append(AVCaption) async throws](avassetwriterinput/captionreceiver/append(_:)-4wpi2.md)
  Suspends until the input is ready for more media data, then appends the caption.
- [func appendImmediately(AVCaptionGroup) throws -> Bool](avassetwriterinput/captionreceiver/appendimmediately(_:)-7q21r.md)
  Appends the caption group synchronously if the input is ready for more media data.
- [func appendImmediately(AVCaption) throws -> Bool](avassetwriterinput/captionreceiver/appendimmediately(_:)-9uy14.md)
  Appends the caption synchronously if the input is ready for more media data.
- [func finish()](avassetwriterinput/captionreceiver/finish.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.

## See Also

- [var expectsMediaDataInRealTime: Bool](avassetwriterinput/expectsmediadatainrealtime.md)
  A Boolean value that indicates whether the input tailors its processing for real-time sources.
- [var isReadyForMoreMediaData: Bool](avassetwriterinput/isreadyformoremediadata.md)
  A Boolean value that indicates whether the input is ready to accept media data.
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](avassetwriterinput/requestmediadatawhenready(on:using:).md)
  Tells the input to request media data, at its convenience, to write to the output file.
- [func append(CMSampleBuffer) -> Bool](avassetwriterinput/append(_:).md)
  Appends a sample buffer to an input to write to the output file.
- [func markAsFinished()](avassetwriterinput/markasfinished.md)
  Marks the input as finished to indicate that you’re done appending samples to it.
- [AVAssetWriterInput.SampleBufferReceiver](avassetwriterinput/samplebufferreceiver.md)
  Provides an interface for writing sample buffers to an input.
- [AVAssetWriterInput.PixelBufferReceiver](avassetwriterinput/pixelbufferreceiver.md)
  Provides an interface for writing pixel buffers to an input.
- [AVAssetWriterInput.TaggedPixelBufferGroupReceiver](avassetwriterinput/taggedpixelbuffergroupreceiver.md)
  Provides an interface for writing tagged pixel buffers to an input.
- [AVAssetWriterInput.MetadataReceiver](avassetwriterinput/metadatareceiver.md)
  Provides an interface for writing timed metadata groups to an input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/captionreceiver)*