# ElectricVehicleLoadEvent.Session

**Framework**: EnergyKit  
**Kind**: struct

A session that tracks the event.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct Session
```

#### Overview

A session starts when a device transitions from idle to consuming electricity. It’s active when consuming electricity. It ends when the device stops consuming electricity.

A session must contain events of a single [`ElectricityFlowDirection`](electricityflowdirection.md). If a vehicle supports vehicle-to-grid (V2G), use a separate session for each direction.

## Topics

### Creating a load event
- [init(id: UUID, state: ElectricVehicleLoadEvent.Session.State, guidanceState: ElectricVehicleLoadEvent.Session.GuidanceState)](electricvehicleloadevent/session-swift.struct/init(id:state:guidancestate:).md)
  Creates an electrical load event session.
- [let guidanceState: ElectricVehicleLoadEvent.Session.GuidanceState](electricvehicleloadevent/session-swift.struct/guidancestate-swift.property.md)
  Identifies the provided guidance and its usability by the load device
- [let id: UUID](electricvehicleloadevent/session-swift.struct/id.md)
  The unique identifier for the session.
- [let state: ElectricVehicleLoadEvent.Session.State](electricvehicleloadevent/session-swift.struct/state-swift.property.md)
  The state of the session.
- [ElectricVehicleLoadEvent.Session.GuidanceState](electricvehicleloadevent/session-swift.struct/guidancestate-swift.struct.md)
  Identifies the provided guidance and its usability by the load device
- [ElectricVehicleLoadEvent.Session.State](electricvehicleloadevent/session-swift.struct/state-swift.enum.md)
  The state of the session.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let id: UUID](electricvehicleloadevent/id.md)
  The unique identifier of the electrical load event.
- [let timestamp: Date](electricvehicleloadevent/timestamp.md)
  The timestamp for when the event occurred.
- [let session: ElectricVehicleLoadEvent.Session](electricvehicleloadevent/session-swift.property.md)
  The session information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/session-swift.struct)*