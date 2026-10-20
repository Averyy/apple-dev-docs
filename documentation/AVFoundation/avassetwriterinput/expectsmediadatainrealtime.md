# expectsMediaDataInRealTime

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the input tailors its processing for real-time sources.

**Availability**:
- iOS 4.1+ - Deprecated in 27.0
- iPadOS 4.1+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.7+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use the input receiver's appendImmediately(...) method instead

## Declaration

```swift
var expectsMediaDataInRealTime: Bool { get set }
```

```objc
@property (nonatomic) BOOL expectsMediaDataInRealTime;
```

#### Discussion

Set this value to [`true`](../../Swift/true.md) if your app appends media data to the input from a real-time source, such as an [`AVCaptureOutput`](../avcaptureoutput.md). Setting a [`true`](../../Swift/true.md) value optimizes the input for real-time usage so it accurately calculates the state of its [`isReadyForMoreMediaData`](./isreadyformoremediadata.md) property value.

You can’t set this value after writing starts.

> ❗ **Important**:  To ensure optimal behavior, don’t set the value of this property and [`performsMultiPassEncodingIfSupported`](./performsmultipassencodingifsupported.md) to [`true`](../../Swift/true.md) at the same time.

## See Also

### Appending media samples
- [var isReadyForMoreMediaData: Bool](./isreadyformoremediadata.md)
  A Boolean value that indicates whether the input is ready to accept media data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/expectsmediadatainrealtime)*