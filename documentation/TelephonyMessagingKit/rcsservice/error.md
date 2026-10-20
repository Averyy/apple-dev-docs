# RCSService.Error

**Framework**: TelephonyMessagingKit  
**Kind**: enum  
**Role**: Enumeration

A type to define errors that can occur when performing RCS operations.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum Error
```

## Topics

### Identifying errors
- [RCSService.Error.serviceUnavailable](./error/serviceunavailable.md)
  The service is unavailable.
- [RCSService.Error.invalidArgument](./error/invalidargument.md)
  A method call provided an invalid argument.
- [RCSService.Error.decodingFailed](./error/decodingfailed.md)
  Decoding an incoming RCS message failed.
- [RCSService.Error.notSupported](./error/notsupported.md)
  The operation isn’t supported.
- [RCSService.Error.unknown](./error/unknown.md)
  An unknown problem caused the error.
- [RCSService.Error.temporaryError](./error/temporaryerror.md)
  The operation failed temporarily.
- [RCSService.Error.permanentError](./error/permanenterror.md)
  The operation failed permanently.
- [RCSService.Error.internalError](./error/internalerror.md)
  The framework encountered an unknown internal error.
- [RCSService.Error.notFound](./error/notfound.md)
  A required resource wasn’t found.
- [RCSService.Error.maximumSizeExceeded](./error/maximumsizeexceeded.md)
  The RCS message exceeded the maximum allowed size.
- [RCSService.Error.endToEndEncryptionNotSupported](./error/endtoendencryptionnotsupported.md)
  The operation does not support end-to-end encryption.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/error)*