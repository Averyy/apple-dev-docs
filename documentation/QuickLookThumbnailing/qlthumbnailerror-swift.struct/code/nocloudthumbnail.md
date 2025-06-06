# QLThumbnailError.Code.noCloudThumbnail

**Framework**: Quick Look Thumbnailing  
**Kind**: case

The thumbnail for a remote file couldn’t be created.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case noCloudThumbnail
```

#### Discussion

The creation of a thumbnail for a remote file stored in a FileProvider extension such as iCloud or another cloud service failed. The request to generate a thumbnail failed because the remote file itself isn’t available locally or couldn’t be used to generate a thumbnail. QuickLookThumbnailing tried to download a thumbnail from the cloud service instead but no thumbnail was available in the cloud service, or an available thumbnail couldn’t be downloaded.

## See Also

- [QLThumbnailError.Code.generationFailed](qlthumbnailerror-swift.struct/code/generationfailed.md)
  The thumbnail couldn’t be created for the given file.
- [QLThumbnailError.Code.noCachedThumbnail](qlthumbnailerror-swift.struct/code/nocachedthumbnail.md)
  A low-quality thumbnail couldn’t be created.
- [QLThumbnailError.Code.requestCancelled](qlthumbnailerror-swift.struct/code/requestcancelled.md)
  The request to create a thumbnail was canceled.
- [QLThumbnailError.Code.requestInvalid](qlthumbnailerror-swift.struct/code/requestinvalid.md)
  The request to create a thumbnail was invalid, for example, there’s no file at a provided URL.
- [QLThumbnailError.Code.savingToURLFailed](qlthumbnailerror-swift.struct/code/savingtourlfailed.md)
  The thumbnail couldn’t be saved at the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailerror-swift.struct/code/nocloudthumbnail)*