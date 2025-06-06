# noCloudThumbnail

**Framework**: Quick Look Thumbnailing  
**Kind**: property

The thumbnail for a remote file couldn’t be created.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
static var noCloudThumbnail: QLThumbnailError.Code { get }
```

#### Discussion

The creation of a thumbnail for a remote file stored in a FileProvider extension such as iCloud or another cloud service failed. The request to generate a thumbnail failed because the remote file itself isn’t available locally or couldn’t be used to generate a thumbnail. QuickLookThumbnailing tried to download a thumbnail from the cloud service instead but no thumbnail was available in the cloud service, or an available thumbnail couldn’t be downloaded.

## See Also

- [static var generationFailed: QLThumbnailError.Code](qlthumbnailerror-swift.struct/generationfailed.md)
  The thumbnail couldn’t be created for the given file.
- [static var noCachedThumbnail: QLThumbnailError.Code](qlthumbnailerror-swift.struct/nocachedthumbnail.md)
  A low-quality thumbnail couldn’t be created.
- [static var requestCancelled: QLThumbnailError.Code](qlthumbnailerror-swift.struct/requestcancelled.md)
  The request to create a thumbnail was canceled.
- [static var requestInvalid: QLThumbnailError.Code](qlthumbnailerror-swift.struct/requestinvalid.md)
  The request to create a thumbnail was invalid, for example, there’s no file at a provided URL.
- [static var savingToURLFailed: QLThumbnailError.Code](qlthumbnailerror-swift.struct/savingtourlfailed.md)
  The thumbnail couldn’t be saved at the given URL.
- [QLThumbnailError.Code](qlthumbnailerror-swift.struct/code.md)
  Error codes that may be returned when generating a thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailerror-swift.struct/nocloudthumbnail)*