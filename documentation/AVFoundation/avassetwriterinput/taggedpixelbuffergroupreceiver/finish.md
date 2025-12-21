# finish()

**Framework**: AVFoundation  
**Kind**: method

Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func finish()
```

## See Also

- [func append([CMTaggedDynamicBuffer], with: CMTime) async throws](avassetwriterinput/taggedpixelbuffergroupreceiver/append(_:with:).md)
  Suspends until the input is ready for more media data, then appends the tagged pixel buffers.
- [func appendImmediately([CMTaggedDynamicBuffer], with: CMTime) throws -> Bool](avassetwriterinput/taggedpixelbuffergroupreceiver/appendimmediately(_:with:).md)
  Appends the tagged pixel buffers synchronously if the input is ready for more media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/finish())*