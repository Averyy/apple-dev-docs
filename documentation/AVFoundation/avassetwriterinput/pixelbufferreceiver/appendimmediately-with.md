# appendImmediately(_:with:)

**Framework**: AVFoundation  
**Kind**: method

Appends the pixel buffer synchronously if the input is ready for more media data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func appendImmediately(_ pixelBuffer: CVReadOnlyPixelBuffer, with presentationTime: CMTime) throws -> Bool
```

#### Return Value

Returns true if the append was successful, false if the input was not ready for more media data.

#### Discussion

> **Note**: An error if the underlying writer failed.

## Parameters

- `pixelBuffer`: The pixel buffer to be appended.
- `presentationTime`: The presentation time for the pixel buffer to be appended.

## See Also

- [func append(CVReadOnlyPixelBuffer, with: CMTime) async throws](avassetwriterinput/pixelbufferreceiver/append(_:with:).md)
  Suspends until the input is ready for more media data, then appends the pixel buffer.
- [func finish()](avassetwriterinput/pixelbufferreceiver/finish.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/pixelbufferreceiver/appendimmediately(_:with:))*