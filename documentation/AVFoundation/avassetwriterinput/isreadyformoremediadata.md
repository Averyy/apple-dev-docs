# isReadyForMoreMediaData

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the input is ready to accept media data.

**Availability**:
- iOS 4.1+ - Deprecated in 27.0
- iPadOS 4.1+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.7+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use the input receiver's async append(...) method instead

## Declaration

```swift
var isReadyForMoreMediaData: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isReadyForMoreMediaData) BOOL readyForMoreMediaData;
```

## Discussion

An asset writer with multiple inputs writes media data in an interleaved manner for efficient playback and storage. To maintain appropriate interleaving, you can only append data to an input when the value of this property is [`true`](../../Swift/true.md).

Apps that write media data from a non-real-time source, such as an instance of [`AVAssetReader`](../avassetreader.md), wait to generate or retrieve more media data while this property value is [`false`](../../Swift/false.md). To control of the supply of non-real-time media data, use the [`requestMediaDataWhenReady(on:using:)`](./requestmediadatawhenready%28on,using%29.md) method to specify a callback for the input to invoke when it’s ready to append more data.

Apps that write media data from a real-time source, such as an instance of [`AVCaptureOutput`](../avcaptureoutput.md), set the input’s [`expectsMediaDataInRealTime`](./expectsmediadatainrealtime.md) property value to [`true`](../../Swift/true.md) so that the input accurately determines its readiness for more data. When [`expectsMediaDataInRealTime`](./expectsmediadatainrealtime.md) is [`true`](../../Swift/true.md), this property value becomes [`false`](../../Swift/false.md) only when the input can’t process media samples at the current data rate. If this property value becomes [`false`](../../Swift/false.md) for a real-time source, your app may need to reduce the rate at which it appends samples, or drop them altogether.

If the [`canPerformMultiplePasses`](./canperformmultiplepasses.md) value of any of an asset writer’s inputs is [`true`](../../Swift/true.md), the value of this property may start as [`false`](../../Swift/false.md), and remain that way for extended periods.

The value of this property often changes from [`false`](../../Swift/false.md) to [`true`](../../Swift/true.md) asynchronously, as the asset writer processes and writes media samples to the output. It’s possible for this property value to temporarily be [`false`](../../Swift/false.md) for all inputs.

This property is key-value observable. The system doesn’t notify observers on a specific thread.

## See Also

### Appending media samples
- [var expectsMediaDataInRealTime: Bool](./expectsmediadatainrealtime.md)
  A Boolean value that indicates whether the input tailors its processing for real-time sources.
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](./requestmediadatawhenready%28on,using%29.md)
  Tells the input to request media data, at its convenience, to write to the output file.
- [func append(CMSampleBuffer) -> Bool](./append%28_%29.md)
  Appends a sample buffer to an input to write to the output file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/isreadyformoremediadata)*