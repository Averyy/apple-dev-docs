# AccessoryTransportSession

**Framework**: AccessoryTransportExtension  
**Kind**: class

A class that manages a session between the extension and host process.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
class AccessoryTransportSession
```

## Topics

### Handling a session request
- [AccessoryTransportSession.Request](accessorytransportsession/request.md)
  An incoming session request, which the extension can accept or reject.
### Handling events
- [AccessoryTransportSession.EventHandler](accessorytransportsession/eventhandler.md)
  A protocol that defines methods for handling events for the session.
### Canceling a session
- [func cancel(error: AccessoryTransportSession.Error?)](accessorytransportsession/cancel(error:).md)
  Cancels the session.
- [AccessoryTransportSession.Error](accessorytransportsession/error.md)
  A type that defines errors encountered when using an accessory transport session.
### Describing a session
- [var description: String](accessorytransportsession/description.md)
  A textual representation of this instance.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession)*