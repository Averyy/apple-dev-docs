# expectsMediaDataInRealTime

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the input tailors its processing for real-time sources.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var expectsMediaDataInRealTime: Bool { get set }
```

#### Discussion

Set this value to [`true`](https://developer.apple.com/documentation/Swift/true) if your app appends media data to the input from a real-time source, such as an [`AVCaptureOutput`](avcaptureoutput.md). Setting a [`true`](https://developer.apple.com/documentation/Swift/true) value optimizes the input for real-time usage so it accurately calculates the state of its [`isReadyForMoreMediaData`](avassetwriterinput/isreadyformoremediadata.md) property value.

You can’t set this value after writing starts.

> ❗ **Important**:  To ensure optimal behavior, don’t set the value of this property and [`performsMultiPassEncodingIfSupported`](avassetwriterinput/performsmultipassencodingifsupported.md) to [`true`](https://developer.apple.com/documentation/Swift/true) at the same time.

## See Also

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
- [AVAssetWriterInput.CaptionReceiver](avassetwriterinput/captionreceiver.md)
  Provides an interface for writing caption data to an input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/expectsmediadatainrealtime)*