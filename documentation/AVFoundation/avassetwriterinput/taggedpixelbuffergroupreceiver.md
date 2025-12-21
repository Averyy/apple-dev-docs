# AVAssetWriterInput.TaggedPixelBufferGroupReceiver

**Framework**: AVFoundation  
**Kind**: class

Provides an interface for writing tagged pixel buffers to an input.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class TaggedPixelBufferGroupReceiver
```

## Topics

### Appending tagged buffers
- [func append([CMTaggedDynamicBuffer], with: CMTime) async throws](avassetwriterinput/taggedpixelbuffergroupreceiver/append(_:with:).md)
  Suspends until the input is ready for more media data, then appends the tagged pixel buffers.
- [func appendImmediately([CMTaggedDynamicBuffer], with: CMTime) throws -> Bool](avassetwriterinput/taggedpixelbuffergroupreceiver/appendimmediately(_:with:).md)
  Appends the tagged pixel buffers synchronously if the input is ready for more media data.
- [func finish()](avassetwriterinput/taggedpixelbuffergroupreceiver/finish.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.
### Accessing the pixel buffer pool
- [var pixelBufferPool: CVMutablePixelBuffer.Pool?](avassetwriterinput/taggedpixelbuffergroupreceiver/pixelbufferpool.md)
  A pixel buffer pool that will vend and efficiently recycle pixel buffer objects that can be appended to the receiver.
- [var sourcePixelBufferAttributes: CVPixelBufferCreationAttributes?](avassetwriterinput/taggedpixelbuffergroupreceiver/sourcepixelbufferattributes.md)
  The pixel buffer attributes of pixel buffers that will be vended by the receiver’s pixel buffer pool.

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
- [AVAssetWriterInput.MetadataReceiver](avassetwriterinput/metadatareceiver.md)
  Provides an interface for writing timed metadata groups to an input.
- [AVAssetWriterInput.CaptionReceiver](avassetwriterinput/captionreceiver.md)
  Provides an interface for writing caption data to an input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver)*