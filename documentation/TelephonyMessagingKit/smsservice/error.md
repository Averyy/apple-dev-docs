# SMSService.Error

**Framework**: TelephonyMessagingKit  
**Kind**: enum

A type to define errors that can occur when performing SMS operations.

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
- [SMSService.Error.notSupported](smsservice/error/notsupported.md)
  The operation isn’t supported.
- [SMSService.Error.permanentFailure](smsservice/error/permanentfailure.md)
  The operation failed permanently.
- [SMSService.Error.temporaryFailure](smsservice/error/temporaryfailure.md)
  The operation failed temporarily.
- [SMSService.Error.unknown](smsservice/error/unknown.md)
  An unknown problem caused the error.
### Encoding and decoding
- [init(from: any Decoder) throws](smsservice/error/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](smsservice/error/encode(to:).md)
  Encodes this value into the given encoder.
### Hashing
- [func hash(into: inout Hasher)](smsservice/error/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](smsservice/error/hashvalue.md)
  The hash value.
### Comparing errors
- [static func == (SMSService.Error, SMSService.Error) -> Bool](smsservice/error/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](smsservice/error/equatable-implementations.md)
- [Error Implementations](smsservice/error/error-implementations.md)
- [LocalizedError Implementations](smsservice/error/localizederror-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice/error)*