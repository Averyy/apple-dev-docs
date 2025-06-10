# AVAssetWriterInput.CaptionReceiver

**Framework**: AVFoundation  
**Kind**: class

Provides an interface for writing caption data to an input.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
class CaptionReceiver
```

## Topics

### Instance Methods
- [func append(AVCaption, isolation: isolated (any Actor)?) async throws](avassetwriterinput/captionreceiver/append(_:isolation:)-2zcpo.md)
  Suspends until the input is ready for more media data, then appends the caption.
- [func append(AVCaptionGroup, isolation: isolated (any Actor)?) async throws](avassetwriterinput/captionreceiver/append(_:isolation:)-6947i.md)
  Suspends until the input is ready for more media data, then appends the caption group.
- [func appendImmediately(AVCaptionGroup) throws -> Bool](avassetwriterinput/captionreceiver/appendimmediately(_:)-7q21r.md)
  Appends the caption group synchronously if the input is ready for more media data.
- [func appendImmediately(AVCaption) throws -> Bool](avassetwriterinput/captionreceiver/appendimmediately(_:)-9uy14.md)
  Appends the caption synchronously if the input is ready for more media data.
- [func finish()](avassetwriterinput/captionreceiver/finish.md)
  Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/captionreceiver)*