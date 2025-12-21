# requestMediaDataWhenReady(on:using:)

**Framework**: AVFoundation  
**Kind**: method

Tells the input to request media data, at its convenience, to write to the output file.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func requestMediaDataWhenReady(on queue: dispatch_queue_t, using block: @escaping () -> Void)
```

#### Discussion

Use this method when working with pull-style buffer sources, such as an [`AVAssetReaderOutput`](avassetreaderoutput.md). The callback you provide appends media data to the input until its [`isReadyForMoreMediaData`](avassetwriterinput/isreadyformoremediadata.md) property becomes [`false`](https://developer.apple.com/documentation/Swift/false), or when there’s no more media data to process (at which point you may mark the input as finished by calling its [`markAsFinished()`](avassetwriterinput/markasfinished().md) method). If you don’t mark the input as finished, after the input processes the media data and becomes ready for more, it invokes the callback again to append more data. The example below shows a typical callback implementation.

```swift
let serialQueue = DispatchQueue(label: "RequestMedia")
assetWriterInput?.requestMediaDataWhenReady(on: serialQueue) { [weak self] in
    guard let self = self,
          let assetWriterInput = self.assetWriterInput else { return }
    while self.assetWriterInput!.isReadyForMoreMediaData {
        // Copy the next sample buffer from your source media.
        guard let nextSampleBuffer = copyNextSampleBufferToWrite() else {
            // Mark the input as finished.
            self.assetWriterInput!.markAsFinished()
            break
        }
        // Append the sample buffer to the input.
        self.assetWriterInput!.append(nextSampleBuffer)
    }      
}
```

When working with push-style sources, such as an [`AVCaptureAudioDataOutput`](avcaptureaudiodataoutput.md) or [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md), append buffers directly to the asset writer input when you receive them using its [`append(_:)`](avassetwriterinput/append(_:).md) method. Using this method helps avoid having to queue up buffers in between the buffer source and the asset writer input.

## Parameters

- `queue`: The queue on which the system invokes the callback.
- `block`: A callback that the input invokes to retrieve additional media data.

## See Also

- [var expectsMediaDataInRealTime: Bool](avassetwriterinput/expectsmediadatainrealtime.md)
  A Boolean value that indicates whether the input tailors its processing for real-time sources.
- [var isReadyForMoreMediaData: Bool](avassetwriterinput/isreadyformoremediadata.md)
  A Boolean value that indicates whether the input is ready to accept media data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/requestmediadatawhenready(on:using:))*