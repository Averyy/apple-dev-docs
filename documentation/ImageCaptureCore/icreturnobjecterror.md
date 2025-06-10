# ICReturnObjectError

**Framework**: ImageCaptureCore  
**Kind**: struct

An object error returned from ImageCaptureCore.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
struct ICReturnObjectError
```

## Topics

### Error Domain
- [let ICErrorDomain: String](icerrordomain.md)
  An error returned by the ImageCaptureCore framework.
### Error Codes
- [static var codeObjectDoesNotExist: ICReturnObjectError.Code](icreturnobjecterror/codeobjectdoesnotexist.md)
  The object does not exist.
- [static var codeObjectDataOffsetInvalid: ICReturnObjectError.Code](icreturnobjecterror/codeobjectdataoffsetinvalid.md)
  The object data offset is invalid.
- [static var codeObjectCouldNotBeRead: ICReturnObjectError.Code](icreturnobjecterror/codeobjectcouldnotberead.md)
  The object could not be read.
- [static var codeObjectDataEmpty: ICReturnObjectError.Code](icreturnobjecterror/codeobjectdataempty.md)
  The object data is empty.
- [ICReturnObjectError.Code](icreturnobjecterror/code.md)
### Type Properties
- [static var codeObjectDataRequestTooLarge: ICReturnObjectError.Code](icreturnobjecterror/codeobjectdatarequesttoolarge.md)
- [static var errorDomain: String](icreturnobjecterror/errordomain.md)

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
- [struct ICReturnPTPDeviceError](icreturnptpdeviceerror.md)
  A PTP device error returned from ImageCaptureCore.
- [struct ICReturnThumbnailError](icreturnthumbnailerror.md)
  A thumbnail error returned from ImageCaptureCore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icreturnobjecterror)*