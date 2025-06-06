# QLThumbnailError.Code

**Framework**: Quick Look Thumbnailing  
**Kind**: enum

Error codes that may be returned when generating a thumbnail.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Error Codes
- [QLThumbnailError.Code.generationFailed](qlthumbnailerror-swift.struct/code/generationfailed.md)
  The thumbnail couldn’t be created for the given file.
- [QLThumbnailError.Code.noCachedThumbnail](qlthumbnailerror-swift.struct/code/nocachedthumbnail.md)
  A low-quality thumbnail couldn’t be created.
- [QLThumbnailError.Code.noCloudThumbnail](qlthumbnailerror-swift.struct/code/nocloudthumbnail.md)
  The thumbnail for a remote file couldn’t be created.
- [QLThumbnailError.Code.requestCancelled](qlthumbnailerror-swift.struct/code/requestcancelled.md)
  The request to create a thumbnail was canceled.
- [QLThumbnailError.Code.requestInvalid](qlthumbnailerror-swift.struct/code/requestinvalid.md)
  The request to create a thumbnail was invalid, for example, there’s no file at a provided URL.
- [QLThumbnailError.Code.savingToURLFailed](qlthumbnailerror-swift.struct/code/savingtourlfailed.md)
  The thumbnail couldn’t be saved at the given URL.
### Initializers
- [init?(rawValue: Int)](qlthumbnailerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let QLThumbnailErrorDomain: String](qlthumbnailerrordomain.md)
  The error domain of the QuickLookThumbnailing framework.
- [struct QLThumbnailError](qlthumbnailerror-swift.struct.md)
  Error information that might return when you generate a thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailerror-swift.struct/code)*