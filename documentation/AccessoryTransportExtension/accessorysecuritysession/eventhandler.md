# AccessorySecuritySession.EventHandler

**Framework**: Accessory Transport Extension  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines methods for handling security session events.

**Availability**:
- iOS 26.5+

## Declaration

```swift
protocol EventHandler
```

## Mentions

- [Receiving iOS notifications on an accessory](../receiving-ios-notifications-on-an-accessory.md)

#### Overview

Implement this protocol to respond to key exchange messages and session invalidation during the cryptographic key exchange process.

## Topics

### Handling security messages
- [func messageReceived(SecurityMessage, completion: (AccessoryMessage.Result) -> Void)](./eventhandler/messagereceived%28_,completion%29.md)
  Handles incoming key material from the system during key exchange.
### Handling session life cycle
- [func sessionInvalidated(error: AccessorySecuritySession.Error?)](./eventhandler/sessioninvalidated%28error%29.md)
  Handles session invalidation.

## See Also

### Handling session events
- [AccessorySecuritySession.Error](./error.md)
  An error that occurs during accessory security-session operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/eventhandler)*