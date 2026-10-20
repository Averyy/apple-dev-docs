# finish()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func finish()
```

## See Also

### Appending captions
- [func append(AVCaptionGroup) async throws](./append%28_%29-4opbd.md)
  Suspends until the input is ready for more media data, then appends the caption group.
- [func append(AVCaption) async throws](./append%28_%29-4wpi2.md)
  Suspends until the input is ready for more media data, then appends the caption.
- [func appendImmediately(AVCaptionGroup) throws -> Bool](./appendimmediately%28_%29-7q21r.md)
  Appends the caption group synchronously if the input is ready for more media data.
- [func appendImmediately(AVCaption) throws -> Bool](./appendimmediately%28_%29-9uy14.md)
  Appends the caption synchronously if the input is ready for more media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/captionreceiver/finish())*