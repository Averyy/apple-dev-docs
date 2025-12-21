# finish()

**Framework**: AVFoundation  
**Kind**: method

Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func finish()
```

## See Also

- [func append(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) async throws](avassetwriterinput/samplebufferreceiver/append(_:).md)
  Suspends until the input is ready for more media data, then appends the sample buffer.
- [func appendImmediately(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) throws -> Bool](avassetwriterinput/samplebufferreceiver/appendimmediately(_:).md)
  Appends the sample buffer synchronously if the input is ready for more media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/samplebufferreceiver/finish())*