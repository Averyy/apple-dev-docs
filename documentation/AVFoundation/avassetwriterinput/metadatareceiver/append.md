# append(_:)

**Framework**: AVFoundation  
**Kind**: method

Suspends until the input is ready for more media data, then appends the timed metadata group.

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
(nonsending) func append(_ timedMetadataGroup: AVTimedMetadataGroup) async throws
```

#### Discussion

> **Note**: An error if the underlying writer failed.

## Parameters

- `timedMetadataGroup`: The timed metadata group to be appended.

## See Also

- [func appendImmediately(AVTimedMetadataGroup) throws -> Bool](avassetwriterinput/metadatareceiver/appendimmediately(_:).md)
  Appends the timed metadata group synchronously if the input is ready for more media data.
- [func finish()](avassetwriterinput/metadatareceiver/finish.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/metadatareceiver/append(_:))*