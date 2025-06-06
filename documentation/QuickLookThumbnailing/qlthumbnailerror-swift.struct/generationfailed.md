# generationFailed

**Framework**: Quick Look Thumbnailing  
**Kind**: property

The thumbnail couldn’t be created for the given file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
static var generationFailed: QLThumbnailError.Code { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailerror-swift.struct/generationfailed)*