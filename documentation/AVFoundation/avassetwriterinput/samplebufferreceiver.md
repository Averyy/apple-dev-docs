# AVAssetWriterInput.SampleBufferReceiver

**Framework**: AVFoundation  
**Kind**: class

Provides an interface for writing sample buffers to an input.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class SampleBufferReceiver
```

## Topics

### Instance Methods
- [func append(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>, isolation: isolated (any Actor)?) async throws](avassetwriterinput/samplebufferreceiver/append(_:isolation:).md)
  Suspends until the input is ready for more media data, then appends the sample buffer.
- [func appendImmediately(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) throws -> Bool](avassetwriterinput/samplebufferreceiver/appendimmediately(_:).md)
  Appends the sample buffer synchronously if the input is ready for more media data.
- [func finish()](avassetwriterinput/samplebufferreceiver/finish.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/samplebufferreceiver)*