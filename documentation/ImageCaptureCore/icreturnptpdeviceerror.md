# ICReturnPTPDeviceError

**Framework**: ImageCaptureCore  
**Kind**: struct

A PTP device error returned from ImageCaptureCore.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
struct ICReturnPTPDeviceError
```

## Topics

### Error Domain
- [let ICErrorDomain: String](icerrordomain.md)
  An error returned by the ImageCaptureCore framework.
### Error Codes
- [static var failedToSendCommand: ICReturnPTPDeviceError.Code](icreturnptpdeviceerror/failedtosendcommand.md)
  Sending a PTP command failed.
- [ICReturnPTPDeviceError.Code](icreturnptpdeviceerror/code.md)
### Type Properties
- [static var errorDomain: String](icreturnptpdeviceerror/errordomain.md)
- [static var notAuthorizedToSendCommand: ICReturnPTPDeviceError.Code](icreturnptpdeviceerror/notauthorizedtosendcommand.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ICReturn](icreturn.md)
- [struct ICLegacyReturn](iclegacyreturn.md)
- [struct ICReturnConnectionError](icreturnconnectionerror.md)
  A connection error returned from ImageCaptureCore.
- [struct ICReturnDownloadError](icreturndownloaderror.md)
  A download error returned from ImageCaptureCore.
- [struct ICReturnMetadataError](icreturnmetadataerror.md)
  A metadata error returned from ImageCaptureCore.
- [struct ICReturnObjectError](icreturnobjecterror.md)
  An object error returned from ImageCaptureCore.
- [struct ICReturnThumbnailError](icreturnthumbnailerror.md)
  A thumbnail error returned from ImageCaptureCore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icreturnptpdeviceerror)*