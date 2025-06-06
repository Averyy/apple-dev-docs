# kCFMessagePortTransportError

**Framework**: Core Foundation  
**Kind**: var

An error occurred trying to send the message.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var kCFMessagePortTransportError: Int32 { get }
```

## See Also

- [var kCFMessagePortSuccess: Int32](kcfmessageportsuccess.md)
  The message was successfully sent and, if a reply was expected, a reply was received.
- [var kCFMessagePortSendTimeout: Int32](kcfmessageportsendtimeout.md)
  The message could not be sent before the send timeout.
- [var kCFMessagePortReceiveTimeout: Int32](kcfmessageportreceivetimeout.md)
  No reply was received before the receive timeout.
- [var kCFMessagePortIsInvalid: Int32](kcfmessageportisinvalid.md)
  The message could not be sent because the message port is invalid.
- [var kCFMessagePortBecameInvalidError: Int32](kcfmessageportbecameinvaliderror.md)
  The message port was invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfmessageporttransporterror)*