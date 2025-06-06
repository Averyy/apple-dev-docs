# QLThumbnailError.Code.requestCancelled

**Framework**: Quick Look Thumbnailing  
**Kind**: case

The request to create a thumbnail was canceled.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case requestCancelled
```

#### Discussion

An app canceled a request to create a thumbnail using QLThumbnailGenerator’s [`cancel(_:)`](qlthumbnailgenerator/cancel(_:).md) method.

## See Also

- [QLThumbnailError.Code.generationFailed](qlthumbnailerror-swift.struct/code/generationfailed.md)
  The thumbnail couldn’t be created for the given file.
- [QLThumbnailError.Code.noCachedThumbnail](qlthumbnailerror-swift.struct/code/nocachedthumbnail.md)
  A low-quality thumbnail couldn’t be created.
- [QLThumbnailError.Code.noCloudThumbnail](qlthumbnailerror-swift.struct/code/nocloudthumbnail.md)
  The thumbnail for a remote file couldn’t be created.
- [QLThumbnailError.Code.requestInvalid](qlthumbnailerror-swift.struct/code/requestinvalid.md)
  The request to create a thumbnail was invalid, for example, there’s no file at a provided URL.
- [QLThumbnailError.Code.savingToURLFailed](qlthumbnailerror-swift.struct/code/savingtourlfailed.md)
  The thumbnail couldn’t be saved at the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailerror-swift.struct/code/requestcancelled)*