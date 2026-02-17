# AccessoryTransportSession.EventHandler

**Framework**: Accessory Transport Extension  
**Kind**: protocol

A protocol that defines methods for handling transport session events.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
protocol EventHandler
```

#### Overview

Implement this protocol to respond to data events and session invalidation in your transport extension.

## Topics

### Handling data events
- [func dataEventHandler(event: AccessoryTransportSession.DataEvent)](accessorytransportsession/eventhandler/dataeventhandler(event:).md)
  Handles events that address incoming data destined for the accessory.
### Handling the session life cycle
- [func invalidationHandler(error: AccessoryTransportSession.Error?)](accessorytransportsession/eventhandler/invalidationhandler(error:).md)
  Handles session invalidation.

## See Also

- [AccessoryTransportSession.DataEvent](accessorytransportsession/dataevent.md)
  An enumeration of data events that the transport extension receives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/eventhandler)*