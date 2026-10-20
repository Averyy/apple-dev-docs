# MMSService.Error

**Framework**: TelephonyMessagingKit  
**Kind**: enum  
**Role**: Enumeration

Enumeration for errors that can occur when performing MMS operations.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum Error
```

## Topics

### Identifying errors
- [MMSService.Error.unknown](./error/unknown.md)
  An unknown problem caused the error.
- [MMSService.Error.notSupported](./error/notsupported.md)
  The operation isn’t supported.
- [MMSService.Error.invalidRecipient](./error/invalidrecipient.md)
  The message contained one or more unknown or malformed recipients.
- [MMSService.Error.invalidMessageParts](./error/invalidmessageparts.md)
  The message conteined one or more unknown or malformed parts.
- [MMSService.Error.internalError](./error/internalerror.md)
  The framework encountered an unknown internal error.
- [MMSService.Error.mmsNotReady](./error/mmsnotready.md)
  The framework isn’t ready to send MMS messages.
- [MMSService.Error.mmsNotConfiguredForCarrier](./error/mmsnotconfiguredforcarrier.md)
  The carrier isn’t currently configured to handle MMS.
- [MMSService.Error.maximumSizeExceeded](./error/maximumsizeexceeded.md)
  The MMS message exceeded the maximum allowed size.

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

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/error)*