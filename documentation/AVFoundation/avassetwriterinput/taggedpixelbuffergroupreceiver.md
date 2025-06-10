# AVAssetWriterInput.TaggedPixelBufferGroupReceiver

**Framework**: AVFoundation  
**Kind**: class

Provides an interface for writing tagged pixel buffers to an input.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class TaggedPixelBufferGroupReceiver
```

## Topics

### Instance Properties
- [var pixelBufferPool: CVMutablePixelBuffer.Pool?](avassetwriterinput/taggedpixelbuffergroupreceiver/pixelbufferpool.md)
  A pixel buffer pool that will vend and efficiently recycle pixel buffer objects that can be appended to the receiver.
- [var sourcePixelBufferAttributes: CVPixelBufferCreationAttributes?](avassetwriterinput/taggedpixelbuffergroupreceiver/sourcepixelbufferattributes.md)
  The pixel buffer attributes of pixel buffers that will be vended by the receiver’s pixel buffer pool.
### Instance Methods
- [func append([CMTaggedDynamicBuffer], with: CMTime, isolation: isolated (any Actor)?) async throws](avassetwriterinput/taggedpixelbuffergroupreceiver/append(_:with:isolation:).md)
  Suspends until the input is ready for more media data, then appends the tagged pixel buffers.
- [func appendImmediately([CMTaggedDynamicBuffer], with: CMTime) throws -> Bool](avassetwriterinput/taggedpixelbuffergroupreceiver/appendimmediately(_:with:).md)
  Appends the tagged pixel buffers synchronously if the input is ready for more media data.
- [func finish()](avassetwriterinput/taggedpixelbuffergroupreceiver/finish.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver)*