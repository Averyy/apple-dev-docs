# finish()

**Framework**: AVFoundation  
**Kind**: method

Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
func finish()
```

## See Also

- [func append(AVCaptionGroup) async throws](avassetwriterinput/captionreceiver/append(_:)-4opbd.md)
  Suspends until the input is ready for more media data, then appends the caption group.
- [func append(AVCaption) async throws](avassetwriterinput/captionreceiver/append(_:)-4wpi2.md)
  Suspends until the input is ready for more media data, then appends the caption.
- [func appendImmediately(AVCaptionGroup) throws -> Bool](avassetwriterinput/captionreceiver/appendimmediately(_:)-7q21r.md)
  Appends the caption group synchronously if the input is ready for more media data.
- [func appendImmediately(AVCaption) throws -> Bool](avassetwriterinput/captionreceiver/appendimmediately(_:)-9uy14.md)
  Appends the caption synchronously if the input is ready for more media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/captionreceiver/finish())*