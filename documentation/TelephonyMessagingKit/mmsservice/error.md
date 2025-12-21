# MMSService.Error

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Enumeration for errors that can occur when performing MMS operations.

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