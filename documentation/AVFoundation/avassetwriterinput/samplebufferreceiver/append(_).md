# append(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Suspends until the input is ready for more media data, then appends the sample buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
(nonsending) func append(_ sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) async throws
```

#### Discussion

> **Throws**: An error if the underlying writer failed.

## Parameters

- `sampleBuffer`: The sample buffer to be appended.

## See Also

### Appending samples
- [func appendImmediately(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) throws -> Bool](./appendimmediately%28_%29.md)
  Appends the sample buffer synchronously if the input is ready for more media data.
- [func finish()](./finish%28%29.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/samplebufferreceiver/append(_:))*