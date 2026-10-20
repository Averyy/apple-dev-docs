# QLThumbnailError.Code.requestInvalid

**Framework**: Quick Look Thumbnailing  
**Kind**: case  
**Role**: Case

The request to create a thumbnail was invalid, for example, there’s no file at a provided URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case requestInvalid
```

```c
QLThumbnailErrorRequestInvalid
```

## See Also

### Error Codes
- [QLThumbnailError.Code.generationFailed](./generationfailed.md)
  The thumbnail couldn’t be created for the given file.
- [QLThumbnailError.Code.noCachedThumbnail](./nocachedthumbnail.md)
  A low-quality thumbnail couldn’t be created.
- [QLThumbnailError.Code.noCloudThumbnail](./nocloudthumbnail.md)
  The thumbnail for a remote file couldn’t be created.
- [QLThumbnailError.Code.requestCancelled](./requestcancelled.md)
  The request to create a thumbnail was canceled.
- [QLThumbnailError.Code.savingToURLFailed](./savingtourlfailed.md)
  The thumbnail couldn’t be saved at the given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailerror-swift.struct/code/requestinvalid)*