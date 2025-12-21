# append(_:with:)

**Framework**: AVFoundation  
**Kind**: method

Suspends until the input is ready for more media data, then appends the pixel buffer.

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
(nonsending) func append(_ pixelBuffer: CVReadOnlyPixelBuffer, with presentationTime: CMTime) async throws
```

#### Discussion

> **Note**: An error if the underlying writer failed.

## Parameters

- `pixelBuffer`: The pixel buffer to be appended.
- `presentationTime`: The presentation time for the pixel buffer to be appended.

## See Also

- [func appendImmediately(CVReadOnlyPixelBuffer, with: CMTime) throws -> Bool](avassetwriterinput/pixelbufferreceiver/appendimmediately(_:with:).md)
  Appends the pixel buffer synchronously if the input is ready for more media data.
- [func finish()](avassetwriterinput/pixelbufferreceiver/finish.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/pixelbufferreceiver/append(_:with:))*