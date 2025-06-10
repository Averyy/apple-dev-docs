# RCSService.Error

**Framework**: TelephonyMessagingKit  
**Kind**: enum

A type to define errors that can occur when performing RCS operations.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
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
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/error/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSService.Error, RCSService.Error) -> Bool](rcsservice/error/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](rcsservice/error/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsservice/error/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](rcsservice/error/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](rcsservice/error/equatable-implementations.md)
- [Error Implementations](rcsservice/error/error-implementations.md)
- [LocalizedError Implementations](rcsservice/error/localizederror-implementations.md)

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