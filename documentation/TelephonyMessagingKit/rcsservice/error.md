# RCSService.Error

**Framework**: TelephonyMessagingKit  
**Kind**: enum

A type to define errors that can occur when performing RCS operations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
enum Error
```

## Topics

### Identifying errors
- [RCSService.Error.serviceUnavailable](rcsservice/error/serviceunavailable.md)
  The service is unavailable.
- [RCSService.Error.invalidArgument](rcsservice/error/invalidargument.md)
  A method call provided an invalid argument.
- [RCSService.Error.decodingFailed](rcsservice/error/decodingfailed.md)
  Decoding an incoming RCS message failed.
- [RCSService.Error.notSupported](rcsservice/error/notsupported.md)
  The operation isn’t supported.
- [RCSService.Error.unknown](rcsservice/error/unknown.md)
  An unknown problem caused the error.
- [RCSService.Error.temporaryError](rcsservice/error/temporaryerror.md)
  The operation failed temporarily.
- [RCSService.Error.permanentError](rcsservice/error/permanenterror.md)
  The operation failed permanently.
- [RCSService.Error.internalError](rcsservice/error/internalerror.md)
  The framework encountered an unknown internal error.
- [RCSService.Error.notFound](rcsservice/error/notfound.md)
  A required resource wasn’t found.
- [RCSService.Error.maximumSizeExceeded](rcsservice/error/maximumsizeexceeded.md)
  The RCS message exceeded the maximum allowed size.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/error)*