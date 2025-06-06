# ICReturnDownloadError

**Framework**: ImageCaptureCore  
**Kind**: struct

A download error returned from ImageCaptureCore.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
struct ICReturnDownloadError
```

## Topics

### Error Domain
- [let ICErrorDomain: String](icerrordomain.md)
  An error returned by the ImageCaptureCore framework.
### Error Codes
- [static var fileWritable: ICReturnDownloadError.Code](icreturndownloaderror/filewritable.md)
  The destination file is not writable.
- [static var pathInvalid: ICReturnDownloadError.Code](icreturndownloaderror/pathinvalid.md)
  The destination path is invalid.
- [ICReturnDownloadError.Code](icreturndownloaderror/code.md)
### Type Properties
- [static var errorDomain: String](icreturndownloaderror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [ICReturn](icreturn.md)
  An error returned from ImageCaptureCore.
- [ICLegacyReturn](iclegacyreturn.md)
  A legacy error returned from ImageCaptureCore.
- [struct ICReturnConnectionError](icreturnconnectionerror.md)
  A connection error returned from ImageCaptureCore.
- [struct ICReturnMetadataError](icreturnmetadataerror.md)
  A metadata error returned from ImageCaptureCore.
- [struct ICReturnObjectError](icreturnobjecterror.md)
  An object error returned from ImageCaptureCore.
- [struct ICReturnPTPDeviceError](icreturnptpdeviceerror.md)
  A PTP device error returned from ImageCaptureCore.
- [struct ICReturnThumbnailError](icreturnthumbnailerror.md)
  A thumbnail error returned from ImageCaptureCore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icreturndownloaderror)*