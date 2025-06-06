# noCachedThumbnail

**Framework**: Quick Look Thumbnailing  
**Kind**: property

A low-quality thumbnail couldn’t be created.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
static var noCachedThumbnail: QLThumbnailError.Code { get }
```

#### Discussion

In response to a request for a low-quality thumbnail, QuickLookThumbnailing searched for a previously created thumbnail to achieve a lower latency but didn’t find one.

## See Also

- [static var generationFailed: QLThumbnailError.Code](qlthumbnailerror-swift.struct/generationfailed.md)
  The thumbnail couldn’t be created for the given file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailerror-swift.struct/nocachedthumbnail)*