# AVAssetWriterInput.MetadataReceiver

**Framework**: AVFoundation  
**Kind**: class

Provides an interface for writing timed metadata groups to an input.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class MetadataReceiver
```

## Topics

### Instance Methods
- [func append(AVTimedMetadataGroup, isolation: isolated (any Actor)?) async throws](avassetwriterinput/metadatareceiver/append(_:isolation:).md)
  Suspends until the input is ready for more media data, then appends the timed metadata group.
- [func appendImmediately(AVTimedMetadataGroup) throws -> Bool](avassetwriterinput/metadatareceiver/appendimmediately(_:).md)
  Appends the timed metadata group synchronously if the input is ready for more media data.
- [func finish()](avassetwriterinput/metadatareceiver/finish.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/metadatareceiver)*