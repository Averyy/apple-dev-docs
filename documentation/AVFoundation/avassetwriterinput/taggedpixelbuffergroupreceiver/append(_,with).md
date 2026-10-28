# append(_:with:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Suspends until the input is ready for more media data, then appends the tagged pixel buffers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated(nonsending)
func append(_ taggedPixelBufferGroup: [CMTaggedDynamicBuffer], with presentationTime: CMTime) async throws
```

## Discussion

> **Throws**: An error if the underlying writer failed.

## Parameters

- `taggedPixelBufferGroup`: The tagged pixel buffers to be appended.
- `presentationTime`: The presentation time for the tagged pixel buffers to be appended.

## See Also

### Appending tagged buffers
- [func appendImmediately([CMTaggedDynamicBuffer], with: CMTime) throws -> Bool](./appendimmediately%28_,with%29.md)
  Appends the tagged pixel buffers synchronously if the input is ready for more media data.
- [func finish()](./finish%28%29.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/append(_:with:))*