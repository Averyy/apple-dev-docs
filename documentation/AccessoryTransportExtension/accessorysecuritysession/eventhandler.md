# AccessorySecuritySession.EventHandler

**Framework**: Accessory Transport Extension  
**Kind**: protocol

A protocol that defines methods for handling security session events.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)
- Mac Catalyst 26.5+ (Beta)

## Declaration

```swift
protocol EventHandler
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Overview

Implement this protocol to respond to key exchange messages and session invalidation during the cryptographic key exchange process.

## Topics

### Handling security messages
- [func messageReceived(SecurityMessage, completion: (AccessoryMessage.Result) -> Void)](accessorysecuritysession/eventhandler/messagereceived(_:completion:).md)
  Handles incoming key material from the system during key exchange.
### Handling session lifecycle
- [func sessionInvalidated(error: AccessorySecuritySession.Error?)](accessorysecuritysession/eventhandler/sessioninvalidated(error:).md)
  Handles session invalidation.

## See Also

- [AccessorySecuritySession.Error](accessorysecuritysession/error.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/eventhandler)*