# appendImmediately(_:)

**Framework**: AVFoundation  
**Kind**: method

Appends the timed metadata group synchronously if the input is ready for more media data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func appendImmediately(_ timedMetadataGroup: AVTimedMetadataGroup) throws -> Bool
```

#### Return Value

Returns true if the append was successful, false if the input was not ready for more media data.

#### Discussion

> **Note**: An error if the underlying writer failed.

## Parameters

- `timedMetadataGroup`: The timed metadata group to be appended

## See Also

- [func append(AVTimedMetadataGroup) async throws](avassetwriterinput/metadatareceiver/append(_:).md)
  Suspends until the input is ready for more media data, then appends the timed metadata group.
- [func finish()](avassetwriterinput/metadatareceiver/finish.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/metadatareceiver/appendimmediately(_:))*