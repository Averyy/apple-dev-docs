# ICReturnThumbnailError

**Framework**: ImageCaptureCore  
**Kind**: struct

A thumbnail error returned from ImageCaptureCore.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
struct ICReturnThumbnailError
```

## Topics

### Error Domain
- [let ICErrorDomain: String](icerrordomain.md)
  An error returned by the ImageCaptureCore framework.
### Error Codes
- [static var alreadyFetching: ICReturnThumbnailError.Code](icreturnthumbnailerror/alreadyfetching.md)
  Item thumbnail request is being serviced.
- [static var canceled: ICReturnThumbnailError.Code](icreturnthumbnailerror/canceled.md)
  Item thumbnail request has been canceled.
- [static var invalid: ICReturnThumbnailError.Code](icreturnthumbnailerror/invalid.md)
  Item thumbnail request completed with invalid result.
- [static var notAvailable: ICReturnThumbnailError.Code](icreturnthumbnailerror/notavailable.md)
  Item does not have thumbnail available.
- [ICReturnThumbnailError.Code](icreturnthumbnailerror/code.md)
### Type Properties
- [static var errorDomain: String](icreturnthumbnailerror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ICReturn](icreturn.md)
  An error returned from ImageCaptureCore.
- [ICLegacyReturn](iclegacyreturn.md)
  A legacy error returned from ImageCaptureCore.
- [struct ICReturnConnectionError](icreturnconnectionerror.md)
  A connection error returned from ImageCaptureCore.
- [struct ICReturnDownloadError](icreturndownloaderror.md)
  A download error returned from ImageCaptureCore.
- [struct ICReturnMetadataError](icreturnmetadataerror.md)
  A metadata error returned from ImageCaptureCore.
- [struct ICReturnObjectError](icreturnobjecterror.md)
  An object error returned from ImageCaptureCore.
- [struct ICReturnPTPDeviceError](icreturnptpdeviceerror.md)
  A PTP device error returned from ImageCaptureCore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icreturnthumbnailerror)*