# AVAssetWriterInput.SampleBufferReceiver

**Framework**: AVFoundation  
**Kind**: class

Provides an interface for writing sample buffers to an input.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class SampleBufferReceiver
```

## Topics

### Appending samples
- [func append(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) async throws](avassetwriterinput/samplebufferreceiver/append(_:).md)
  Suspends until the input is ready for more media data, then appends the sample buffer.
- [func appendImmediately(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) throws -> Bool](avassetwriterinput/samplebufferreceiver/appendimmediately(_:).md)
  Appends the sample buffer synchronously if the input is ready for more media data.
- [func finish()](avassetwriterinput/samplebufferreceiver/finish.md)
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
- [AVAssetWriterInput.PixelBufferReceiver](avassetwriterinput/pixelbufferreceiver.md)
  Provides an interface for writing pixel buffers to an input.
- [AVAssetWriterInput.TaggedPixelBufferGroupReceiver](avassetwriterinput/taggedpixelbuffergroupreceiver.md)
  Provides an interface for writing tagged pixel buffers to an input.
- [AVAssetWriterInput.MetadataReceiver](avassetwriterinput/metadatareceiver.md)
  Provides an interface for writing timed metadata groups to an input.
- [AVAssetWriterInput.CaptionReceiver](avassetwriterinput/captionreceiver.md)
  Provides an interface for writing caption data to an input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/samplebufferreceiver)*