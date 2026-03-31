# AccessoryTransportSession.EventHandler

**Framework**: Accessory Transport Extension  
**Kind**: protocol

A protocol that defines methods for handling transport session events.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
protocol EventHandler
```

#### Overview

Implement this protocol to respond to data events and session invalidation in your transport extension.

## Topics

### Handling the session life cycle
- [func invalidationHandler(error: AccessoryTransportSession.Error?)](accessorytransportsession/eventhandler/invalidationhandler(error:).md)
  Handles session invalidation.
### Instance Methods
- [func messageReceived(TransportMessage, completion: TransportMessage.Completion)](accessorytransportsession/eventhandler/messagereceived(_:completion:).md)
  Message received from the Data Provider. Completion should be called with the result of sending the message to the accessory. If not called, it’s assumed the message was successfully delivered, and will not be re-delivered.
- [func sessionInvalidated(error: AccessoryTransportSession.Error?)](accessorytransportsession/eventhandler/sessioninvalidated(error:).md)
  Session has been invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/eventhandler)*