# QLThumbnailError

**Framework**: Quick Look Thumbnailing  
**Kind**: struct

Error information that might return when you generate a thumbnail.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
struct QLThumbnailError
```

## Topics

### Error Codes
- [static var generationFailed: QLThumbnailError.Code](qlthumbnailerror-swift.struct/generationfailed.md)
  The thumbnail couldn’t be created for the given file.
- [static var noCachedThumbnail: QLThumbnailError.Code](qlthumbnailerror-swift.struct/nocachedthumbnail.md)
  A low-quality thumbnail couldn’t be created.
- [static var noCloudThumbnail: QLThumbnailError.Code](qlthumbnailerror-swift.struct/nocloudthumbnail.md)
  The thumbnail for a remote file couldn’t be created.
- [static var requestCancelled: QLThumbnailError.Code](qlthumbnailerror-swift.struct/requestcancelled.md)
  The request to create a thumbnail was canceled.
- [static var requestInvalid: QLThumbnailError.Code](qlthumbnailerror-swift.struct/requestinvalid.md)
  The request to create a thumbnail was invalid, for example, there’s no file at a provided URL.
- [static var savingToURLFailed: QLThumbnailError.Code](qlthumbnailerror-swift.struct/savingtourlfailed.md)
  The thumbnail couldn’t be saved at the given URL.
- [QLThumbnailError.Code](qlthumbnailerror-swift.struct/code.md)
  Error codes that may be returned when generating a thumbnail.
### Type Properties
- [static var errorDomain: String](qlthumbnailerror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let QLThumbnailErrorDomain: String](qlthumbnailerrordomain.md)
  The error domain of the QuickLookThumbnailing framework.
- [QLThumbnailError.Code](qlthumbnailerror-swift.struct/code.md)
  Error codes that may be returned when generating a thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailerror-swift.struct)*