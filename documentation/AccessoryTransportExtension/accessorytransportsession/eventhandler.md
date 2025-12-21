# AccessoryTransportSession.EventHandler

**Framework**: AccessoryTransportExtension  
**Kind**: protocol

A protocol that defines methods for handling events for the session.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
protocol EventHandler
```

#### Overview

You provide this type to a session request when handling the [`accept(_:)`](accessorytransportsession/request/accept(_:).md) method.

## Topics

### Handling session cancellation
- [func invalidationHandler(error: AccessoryTransportSession.Error?)](accessorytransportsession/eventhandler/invalidationhandler(error:).md)
  Handles cancellation of the session, in response to a call from the framework.
- [AccessoryTransportSession.Error](accessorytransportsession/error.md)
  A type that defines errors encountered when using an accessory transport session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/eventhandler)*