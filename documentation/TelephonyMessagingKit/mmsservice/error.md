# MMSService.Error

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Enumeration for errors that can occur when performing MMS operations.

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
- [MMSService.Error.unknown](mmsservice/error/unknown.md)
  An unknown problem caused the error.
- [MMSService.Error.notSupported](mmsservice/error/notsupported.md)
  The operation isn’t supported.
- [MMSService.Error.invalidRecipient](mmsservice/error/invalidrecipient.md)
  The message contained one or more unknown or malformed recipients.
- [MMSService.Error.invalidMessageParts](mmsservice/error/invalidmessageparts.md)
  The message conteined one or more unknown or malformed parts.
- [MMSService.Error.internalError](mmsservice/error/internalerror.md)
  The framework encountered an unknown internal error.
- [MMSService.Error.mmsNotReady](mmsservice/error/mmsnotready.md)
  The framework isn’t ready to send MMS messages.
- [MMSService.Error.mmsNotConfiguredForCarrier](mmsservice/error/mmsnotconfiguredforcarrier.md)
  The carrier isn’t currently configured to handle MMS.
- [MMSService.Error.maximumSizeExceeded](mmsservice/error/maximumsizeexceeded.md)
  The MMS message exceeded the maximum allowed size.
### Encoding and decoding
- [init(from: any Decoder) throws](mmsservice/error/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](mmsservice/error/encode(to:).md)
  Encodes this value into the given encoder.
### Hashing
- [func hash(into: inout Hasher)](mmsservice/error/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](mmsservice/error/hashvalue.md)
  The hash value.
### Comparing errors
- [static func == (MMSService.Error, MMSService.Error) -> Bool](mmsservice/error/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](mmsservice/error/equatable-implementations.md)
- [Error Implementations](mmsservice/error/error-implementations.md)
- [LocalizedError Implementations](mmsservice/error/localizederror-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/error)*