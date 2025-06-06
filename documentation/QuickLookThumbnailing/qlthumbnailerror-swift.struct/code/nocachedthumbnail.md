# QLThumbnailError.Code.noCachedThumbnail

**Framework**: Quick Look Thumbnailing  
**Kind**: case

A low-quality thumbnail couldn’t be created.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case noCachedThumbnail
```

#### Discussion

In response to a request for a low-quality thumbnail, QuickLookThumbnailing searched for a previously created thumbnail to achieve a lower latency but didn’t find one.

## See Also

- [QLThumbnailError.Code.generationFailed](qlthumbnailerror-swift.struct/code/generationfailed.md)
  The thumbnail couldn’t be created for the given file.
- [QLThumbnailError.Code.noCloudThumbnail](qlthumbnailerror-swift.struct/code/nocloudthumbnail.md)
  The thumbnail for a remote file couldn’t be created.
- [QLThumbnailError.Code.requestCancelled](qlthumbnailerror-swift.struct/code/requestcancelled.md)
  The request to create a thumbnail was canceled.
- [QLThumbnailError.Code.requestInvalid](qlthumbnailerror-swift.struct/code/requestinvalid.md)
  The request to create a thumbnail was invalid, for example, there’s no file at a provided URL.
- [QLThumbnailError.Code.savingToURLFailed](qlthumbnailerror-swift.struct/code/savingtourlfailed.md)
  The thumbnail couldn’t be saved at the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailerror-swift.struct/code/nocachedthumbnail)*