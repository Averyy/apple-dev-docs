# appendImmediately(_:with:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Appends the tagged pixel buffers synchronously if the input is ready for more media data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func appendImmediately(_ taggedPixelBufferGroup: [CMTaggedDynamicBuffer], with presentationTime: CMTime) throws -> Bool
```

#### Return Value

Returns true if the append was successful, false if the input was not ready for more media data.

#### Discussion

> **Throws**: An error if the underlying writer failed.

## Parameters

- `taggedPixelBufferGroup`: The tagged pixel buffers to be appended.
- `presentationTime`: The presentation time for the tagged pixel buffers to be appended.

## See Also

### Appending tagged buffers
- [func append([CMTaggedDynamicBuffer], with: CMTime) async throws](./append%28_,with%29.md)
  Suspends until the input is ready for more media data, then appends the tagged pixel buffers.
- [func finish()](./finish%28%29.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/appendimmediately(_:with:))*