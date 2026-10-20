# MMSService.Error.unknown

**Framework**: TelephonyMessagingKit  
**Kind**: case  
**Role**: Case

An unknown problem caused the error.

**Availability**:
- iOS 26.0+

## Declaration

```swift
case unknown
```

## See Also

### Identifying errors
- [MMSService.Error.notSupported](./notsupported.md)
  The operation isn’t supported.
- [MMSService.Error.invalidRecipient](./invalidrecipient.md)
  The message contained one or more unknown or malformed recipients.
- [MMSService.Error.invalidMessageParts](./invalidmessageparts.md)
  The message conteined one or more unknown or malformed parts.
- [MMSService.Error.internalError](./internalerror.md)
  The framework encountered an unknown internal error.
- [MMSService.Error.mmsNotReady](./mmsnotready.md)
  The framework isn’t ready to send MMS messages.
- [MMSService.Error.mmsNotConfiguredForCarrier](./mmsnotconfiguredforcarrier.md)
  The carrier isn’t currently configured to handle MMS.
- [MMSService.Error.maximumSizeExceeded](./maximumsizeexceeded.md)
  The MMS message exceeded the maximum allowed size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/error/unknown)*