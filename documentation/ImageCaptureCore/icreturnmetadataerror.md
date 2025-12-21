# ICReturnMetadataError

**Framework**: ImageCaptureCore  
**Kind**: struct

A metadata error returned from ImageCaptureCore.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
struct ICReturnMetadataError
```

## Topics

### Error Domain
- [let ICErrorDomain: String](icerrordomain.md)
  An error returned by the ImageCaptureCore framework.
### Error Codes
- [static var alreadyFetching: ICReturnMetadataError.Code](icreturnmetadataerror/alreadyfetching.md)
  Item metadata request is being serviced.
- [static var canceled: ICReturnMetadataError.Code](icreturnmetadataerror/canceled.md)
  Item metadata request has been canceled.
- [static var invalid: ICReturnMetadataError.Code](icreturnmetadataerror/invalid.md)
  Item metadata request completed with invalid result.
- [static var notAvailable: ICReturnMetadataError.Code](icreturnmetadataerror/notavailable.md)
  Item does not have metadata available.
- [ICReturnMetadataError.Code](icreturnmetadataerror/code.md)
### Type Properties
- [static var errorDomain: String](icreturnmetadataerror/errordomain.md)

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
- [struct ICReturnObjectError](icreturnobjecterror.md)
  An object error returned from ImageCaptureCore.
- [struct ICReturnPTPDeviceError](icreturnptpdeviceerror.md)
  A PTP device error returned from ImageCaptureCore.
- [struct ICReturnThumbnailError](icreturnthumbnailerror.md)
  A thumbnail error returned from ImageCaptureCore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icreturnmetadataerror)*