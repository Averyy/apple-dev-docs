# append(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Suspends until the input is ready for more media data, then appends the timed metadata group.

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
(nonsending) func append(_ timedMetadataGroup: AVTimedMetadataGroup) async throws
```

#### Discussion

> **Throws**: An error if the underlying writer failed.

## Parameters

- `timedMetadataGroup`: The timed metadata group to be appended.

## See Also

### Appending metadata
- [func appendImmediately(AVTimedMetadataGroup) throws -> Bool](./appendimmediately%28_%29.md)
  Appends the timed metadata group synchronously if the input is ready for more media data.
- [func finish()](./finish%28%29.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/metadatareceiver/append(_:))*