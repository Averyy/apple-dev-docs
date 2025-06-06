# kCFMessagePortSendTimeout

**Framework**: Core Foundation  
**Kind**: var

The message could not be sent before the send timeout.

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
var kCFMessagePortSendTimeout: Int32 { get }
```

## See Also

- [var kCFMessagePortSuccess: Int32](kcfmessageportsuccess.md)
  The message was successfully sent and, if a reply was expected, a reply was received.
- [var kCFMessagePortReceiveTimeout: Int32](kcfmessageportreceivetimeout.md)
  No reply was received before the receive timeout.
- [var kCFMessagePortIsInvalid: Int32](kcfmessageportisinvalid.md)
  The message could not be sent because the message port is invalid.
- [var kCFMessagePortTransportError: Int32](kcfmessageporttransporterror.md)
  An error occurred trying to send the message.
- [var kCFMessagePortBecameInvalidError: Int32](kcfmessageportbecameinvaliderror.md)
  The message port was invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfmessageportsendtimeout)*