# append(_:)

**Framework**: AVFoundation  
**Kind**: method

Suspends until the input is ready for more media data, then appends the caption.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
nonisolated
(nonsending) func append(_ caption: AVCaption) async throws
```

#### Discussion

> **Note**: An error if the underlying writer failed.

## Parameters

- `caption`: The caption to be appended.

## See Also

- [func append(AVCaptionGroup) async throws](avassetwriterinput/captionreceiver/append(_:)-4opbd.md)
  Suspends until the input is ready for more media data, then appends the caption group.
- [func appendImmediately(AVCaptionGroup) throws -> Bool](avassetwriterinput/captionreceiver/appendimmediately(_:)-7q21r.md)
  Appends the caption group synchronously if the input is ready for more media data.
- [func appendImmediately(AVCaption) throws -> Bool](avassetwriterinput/captionreceiver/appendimmediately(_:)-9uy14.md)
  Appends the caption synchronously if the input is ready for more media data.
- [func finish()](avassetwriterinput/captionreceiver/finish.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/captionreceiver/append(_:)-4wpi2)*