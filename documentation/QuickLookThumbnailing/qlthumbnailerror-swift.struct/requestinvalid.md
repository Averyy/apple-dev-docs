# requestInvalid

**Framework**: Quick Look Thumbnailing  
**Kind**: property  
**Role**: Type Property

The request to create a thumbnail was invalid, for example, there’s no file at a provided URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
static var requestInvalid: QLThumbnailError.Code { get }
```

## See Also

### Error Codes
- [static var generationFailed: QLThumbnailError.Code](./generationfailed.md)
  The thumbnail couldn’t be created for the given file.
- [static var noCachedThumbnail: QLThumbnailError.Code](./nocachedthumbnail.md)
  A low-quality thumbnail couldn’t be created.
- [static var noCloudThumbnail: QLThumbnailError.Code](./nocloudthumbnail.md)
  The thumbnail for a remote file couldn’t be created.
- [static var requestCancelled: QLThumbnailError.Code](./requestcancelled.md)
  The request to create a thumbnail was canceled.
- [static var savingToURLFailed: QLThumbnailError.Code](./savingtourlfailed.md)
  The thumbnail couldn’t be saved at the given URL.
- [QLThumbnailError.Code](./code.md)
  Error codes that may be returned when generating a thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailerror-swift.struct/requestinvalid)*