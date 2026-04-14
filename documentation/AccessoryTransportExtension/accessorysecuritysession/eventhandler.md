# AccessorySecuritySession.EventHandler

**Framework**: Accessory Transport Extension  
**Kind**: protocol

A protocol that defines methods for handling security session events.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
protocol EventHandler
```

#### Overview

Implement this protocol to respond to key exchange events and session invalidation.

## Topics

### Instance Methods
- [func messageReceived(SecurityMessage, completion: (AccessoryMessage.Result) -> Void)](accessorysecuritysession/eventhandler/messagereceived(_:completion:).md)
  Security message received.
- [func sessionInvalidated(error: AccessorySecuritySession.Error?)](accessorysecuritysession/eventhandler/sessioninvalidated(error:).md)
  Session has been invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorysecuritysession/eventhandler)*