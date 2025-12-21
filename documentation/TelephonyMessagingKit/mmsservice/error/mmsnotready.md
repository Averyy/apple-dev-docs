# MMSService.Error.mmsNotReady

**Framework**: TelephonyMessagingKit  
**Kind**: case

The framework isn’t ready to send MMS messages.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
case mmsNotReady
```

#### Discussion

You can handle this error by making another attempt to send the MMS message later.

## See Also

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
- [MMSService.Error.mmsNotConfiguredForCarrier](mmsservice/error/mmsnotconfiguredforcarrier.md)
  The carrier isn’t currently configured to handle MMS.
- [MMSService.Error.maximumSizeExceeded](mmsservice/error/maximumsizeexceeded.md)
  The MMS message exceeded the maximum allowed size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/error/mmsnotready)*