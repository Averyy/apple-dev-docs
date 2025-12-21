# ICReturnConnectionError

**Framework**: ImageCaptureCore  
**Kind**: struct

A connection error returned from ImageCaptureCore.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
struct ICReturnConnectionError
```

## Topics

### Error Domain
- [let ICErrorDomain: String](icerrordomain.md)
  An error returned by the ImageCaptureCore framework.
### Error Codes
- [static var closedSessionSuddenly: ICReturnConnectionError.Code](icreturnconnectionerror/closedsessionsuddenly.md)
  Device closed session without request.
- [static var driverExited: ICReturnConnectionError.Code](icreturnconnectionerror/driverexited.md)
  Device driver exited without request.
- [static var ejectFailed: ICReturnConnectionError.Code](icreturnconnectionerror/ejectfailed.md)
  Device reports eject has failed.
- [static var ejectedSuddenly: ICReturnConnectionError.Code](icreturnconnectionerror/ejectedsuddenly.md)
  Device ejected without request.
- [static var failedToOpen: ICReturnConnectionError.Code](icreturnconnectionerror/failedtoopen.md)
  Failed to open a connection to the device.
- [static var failedToOpenDevice: ICReturnConnectionError.Code](icreturnconnectionerror/failedtoopendevice.md)
  Failed to open the device.
- [static var sessionAlreadyOpen: ICReturnConnectionError.Code](icreturnconnectionerror/sessionalreadyopen.md)
  Device reports session is already open.
- [ICReturnConnectionError.Code](icreturnconnectionerror/code.md)
### Type Properties
- [static var errorDomain: String](icreturnconnectionerror/errordomain.md)
- [static var notAuthorizedToOpenDevice: ICReturnConnectionError.Code](icreturnconnectionerror/notauthorizedtoopendevice.md)

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
- [struct ICReturnDownloadError](icreturndownloaderror.md)
  A download error returned from ImageCaptureCore.
- [struct ICReturnMetadataError](icreturnmetadataerror.md)
  A metadata error returned from ImageCaptureCore.
- [struct ICReturnObjectError](icreturnobjecterror.md)
  An object error returned from ImageCaptureCore.
- [struct ICReturnPTPDeviceError](icreturnptpdeviceerror.md)
  A PTP device error returned from ImageCaptureCore.
- [struct ICReturnThumbnailError](icreturnthumbnailerror.md)
  A thumbnail error returned from ImageCaptureCore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icreturnconnectionerror)*