# append(_:)

**Framework**: AVFoundation  
**Kind**: method

Suspends until the input is ready for more media data, then appends the sample buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
(nonsending) func append(_ sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) async throws
```

#### Discussion

> **Note**: An error if the underlying writer failed.

## Parameters

- `sampleBuffer`: The sample buffer to be appended.

## See Also

- [func appendImmediately(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) throws -> Bool](avassetwriterinput/samplebufferreceiver/appendimmediately(_:).md)
  Appends the sample buffer synchronously if the input is ready for more media data.
- [func finish()](avassetwriterinput/samplebufferreceiver/finish.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/samplebufferreceiver/append(_:))*