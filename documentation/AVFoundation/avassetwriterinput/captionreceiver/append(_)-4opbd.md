# append(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Suspends until the input is ready for more media data, then appends the caption group.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
nonisolated(nonsending)
func append(_ captionGroup: AVCaptionGroup) async throws
```

## Discussion

> **Throws**: An error if the underlying writer failed.

## Parameters

- `captionGroup`: The caption group to be appended.

## See Also

### Appending captions
- [func append(AVCaption) async throws](./append%28_%29-4wpi2.md)
  Suspends until the input is ready for more media data, then appends the caption.
- [func appendImmediately(AVCaptionGroup) throws -> Bool](./appendimmediately%28_%29-7q21r.md)
  Appends the caption group synchronously if the input is ready for more media data.
- [func appendImmediately(AVCaption) throws -> Bool](./appendimmediately%28_%29-9uy14.md)
  Appends the caption synchronously if the input is ready for more media data.
- [func finish()](./finish%28%29.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/captionreceiver/append(_:)-4opbd)*