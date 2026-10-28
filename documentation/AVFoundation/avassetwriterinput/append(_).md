# append(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Appends a sample buffer to an input to write to the output file.

**Availability**:
- iOS 4.1+ - Deprecated in 27.0
- iPadOS 4.1+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.7+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use SampleBufferReceiver.append(_:) instead

## Declaration

```swift
func append(_ sampleBuffer: CMSampleBuffer) -> Bool
```

```objc
- (BOOL) appendSampleBuffer:(CMSampleBufferRef) sampleBuffer;
```

## Return Value

[`true`](../../Swift/true.md) if the input successfully appends the sample buffer; otherwise, [`false`](../../Swift/false.md).

## Discussion

Order the samples you append according to storage requirements. For example, if you’re working with sample buffers containing compressed video, order and append them according to their decode timestamp. The system uses the timing information in the sample buffer relative to the time you set in the call to [`startSession(atSourceTime:)`](../avassetwriter/startsession%28atsourcetime%29.md) to determine the timing of samples in the output file.

If this method returns [`false`](../../Swift/false.md), check the value of the asset writer’s [`status`](../avassetwriter/status-swift.property.md) property to determine whether the writing operation’s status is complete, failed, or canceled. If the status is [`AVAssetWriter.Status.failed`](../avassetwriter/status-swift.enum/failed.md), the asset writer’s [`error`](../avassetwriter/error.md) property contains an error object that describes the failure.

> ❗ **Important**:  Don’t modify the sample buffer or its contents after you’ve passed it to this method.

## Parameters

- `sampleBuffer`: The sample buffer to append.

## See Also

### Appending media samples
- [var expectsMediaDataInRealTime: Bool](./expectsmediadatainrealtime.md)
  A Boolean value that indicates whether the input tailors its processing for real-time sources.
- [var isReadyForMoreMediaData: Bool](./isreadyformoremediadata.md)
  A Boolean value that indicates whether the input is ready to accept media data.
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](./requestmediadatawhenready%28on,using%29.md)
  Tells the input to request media data, at its convenience, to write to the output file.
- [func markAsFinished()](./markasfinished%28%29.md)
  Marks the input as finished to indicate that you’re done appending samples to it.
- [AVAssetWriterInput.SampleBufferReceiver](./samplebufferreceiver.md)
  Provides an interface for writing sample buffers to an input.
- [AVAssetWriterInput.PixelBufferReceiver](./pixelbufferreceiver.md)
  Provides an interface for writing pixel buffers to an input.
- [AVAssetWriterInput.TaggedPixelBufferGroupReceiver](./taggedpixelbuffergroupreceiver.md)
  Provides an interface for writing tagged pixel buffers to an input.
- [AVAssetWriterInput.MetadataReceiver](./metadatareceiver.md)
  Provides an interface for writing timed metadata groups to an input.
- [AVAssetWriterInput.CaptionReceiver](./captionreceiver.md)
  Provides an interface for writing caption data to an input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/append(_:))*