# AVAssetWriterInput.PixelBufferReceiver

**Framework**: AVFoundation  
**Kind**: class

Provides an interface for writing pixel buffers to an input.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class PixelBufferReceiver
```

## Topics

### Instance Properties
- [var pixelBufferPool: CVMutablePixelBuffer.Pool?](avassetwriterinput/pixelbufferreceiver/pixelbufferpool.md)
  A pixel buffer pool that will vend and efficiently recycle pixel buffer objects that can be appended to the receiver.
- [var sourcePixelBufferAttributes: CVPixelBufferCreationAttributes?](avassetwriterinput/pixelbufferreceiver/sourcepixelbufferattributes.md)
  The pixel buffer attributes of pixel buffers that will be vended by the receiver’s pixel buffer pool.
### Instance Methods
- [func append(CVReadOnlyPixelBuffer, with: CMTime, isolation: isolated (any Actor)?) async throws](avassetwriterinput/pixelbufferreceiver/append(_:with:isolation:).md)
  Suspends until the input is ready for more media data, then appends the pixel buffer.
- [func appendImmediately(CVReadOnlyPixelBuffer, with: CMTime) throws -> Bool](avassetwriterinput/pixelbufferreceiver/appendimmediately(_:with:).md)
  Appends the pixel buffer synchronously if the input is ready for more media data.
- [func finish()](avassetwriterinput/pixelbufferreceiver/finish.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/pixelbufferreceiver)*