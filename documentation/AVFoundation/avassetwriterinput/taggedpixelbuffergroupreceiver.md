# AVAssetWriterInput.TaggedPixelBufferGroupReceiver

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

Provides an interface for writing tagged pixel buffers to an input.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class TaggedPixelBufferGroupReceiver
```

## Topics

### Appending tagged buffers
- [func append([CMTaggedDynamicBuffer], with: CMTime) async throws](./taggedpixelbuffergroupreceiver/append%28_,with%29.md)
  Suspends until the input is ready for more media data, then appends the tagged pixel buffers.
- [func appendImmediately([CMTaggedDynamicBuffer], with: CMTime) throws -> Bool](./taggedpixelbuffergroupreceiver/appendimmediately%28_,with%29.md)
  Appends the tagged pixel buffers synchronously if the input is ready for more media data.
- [func finish()](./taggedpixelbuffergroupreceiver/finish%28%29.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.
### Accessing the pixel buffer pool
- [var pixelBufferPool: CVMutablePixelBuffer.Pool?](./taggedpixelbuffergroupreceiver/pixelbufferpool.md)
  A pixel buffer pool that will vend and efficiently recycle pixel buffer objects that can be appended to the receiver.
- [var sourcePixelBufferAttributes: CVPixelBufferCreationAttributes?](./taggedpixelbuffergroupreceiver/sourcepixelbufferattributes.md)
  The pixel buffer attributes of pixel buffers that will be vended by the receiver’s pixel buffer pool.

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
- [AVAssetWriterInput.SampleBufferReceiver](./samplebufferreceiver.md)
  Provides an interface for writing sample buffers to an input.
- [AVAssetWriterInput.PixelBufferReceiver](./pixelbufferreceiver.md)
  Provides an interface for writing pixel buffers to an input.
- [AVAssetWriterInput.MetadataReceiver](./metadatareceiver.md)
  Provides an interface for writing timed metadata groups to an input.
- [AVAssetWriterInput.CaptionReceiver](./captionreceiver.md)
  Provides an interface for writing caption data to an input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver)*