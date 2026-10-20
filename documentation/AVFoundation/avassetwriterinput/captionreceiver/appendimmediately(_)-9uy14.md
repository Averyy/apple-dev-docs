# appendImmediately(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Appends the caption synchronously if the input is ready for more media data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func appendImmediately(_ caption: AVCaption) throws -> Bool
```

#### Return Value

Returns true if the append was successful, false if the input was not ready for more media data.

#### Discussion

> **Throws**: An error if the underlying writer failed.

## Parameters

- `caption`: The caption to be appended.

## See Also

### Appending captions
- [func append(AVCaptionGroup) async throws](./append%28_%29-4opbd.md)
  Suspends until the input is ready for more media data, then appends the caption group.
- [func append(AVCaption) async throws](./append%28_%29-4wpi2.md)
  Suspends until the input is ready for more media data, then appends the caption.
- [func appendImmediately(AVCaptionGroup) throws -> Bool](./appendimmediately%28_%29-7q21r.md)
  Appends the caption group synchronously if the input is ready for more media data.
- [func finish()](./finish%28%29.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/captionreceiver/appendimmediately(_:)-9uy14)*