# AVAssetWriterInput.SampleBufferReceiver

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

Provides an interface for writing sample buffers to an input.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class SampleBufferReceiver
```

## Topics

### Appending samples
- [func append(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) async throws](./samplebufferreceiver/append%28_%29.md)
  Suspends until the input is ready for more media data, then appends the sample buffer.
- [func appendImmediately(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) throws -> Bool](./samplebufferreceiver/appendimmediately%28_%29.md)
  Appends the sample buffer synchronously if the input is ready for more media data.
- [func finish()](./samplebufferreceiver/finish%28%29.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.

## See Also

### Appending media samples
- [var expectsMediaDataInRealTime: Bool](./expectsmediadatainrealtime.md)
  A Boolean value that indicates whether the input tailors its processing for real-time sources.
- [var isReadyForMoreMediaData: Bool](./isreadyformoremediadata.md)
  A Boolean value that indicates whether the input is ready to accept media data.
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](./requestmediadatawhenready%28on,using%29.md)
  Tells the input to request media data, at its convenience, to write to the output file.
- [func append(CMSampleBuffer) -> Bool](./append%28_%29.md)
  Appends a sample buffer to an input to write to the output file.
- [func markAsFinished()](./markasfinished%28%29.md)
  Marks the input as finished to indicate that you’re done appending samples to it.
- [AVAssetWriterInput.PixelBufferReceiver](./pixelbufferreceiver.md)
  Provides an interface for writing pixel buffers to an input.
- [AVAssetWriterInput.TaggedPixelBufferGroupReceiver](./taggedpixelbuffergroupreceiver.md)
  Provides an interface for writing tagged pixel buffers to an input.
- [AVAssetWriterInput.MetadataReceiver](./metadatareceiver.md)
  Provides an interface for writing timed metadata groups to an input.
- [AVAssetWriterInput.CaptionReceiver](./captionreceiver.md)
  Provides an interface for writing caption data to an input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/samplebufferreceiver)*