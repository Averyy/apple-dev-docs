# ElectricVehicleLoadEvent.Session.State

**Framework**: EnergyKit  
**Kind**: enum

The state of the session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
enum State
```

#### Overview

When a device transitions from from idle to consuming or generating electricity, it must create a load event with [`ElectricVehicleLoadEvent.Session.State.begin`](electricvehicleloadevent/session-swift.struct/state-swift.enum/begin.md). As it reports events, it sends load events with [`ElectricVehicleLoadEvent.Session.State.active`](electricvehicleloadevent/session-swift.struct/state-swift.enum/active.md). Once idle, it closes the session with [`ElectricVehicleLoadEvent.Session.State.end`](electricvehicleloadevent/session-swift.struct/state-swift.enum/end.md).

## Topics

### Enumeration Cases
- [ElectricVehicleLoadEvent.Session.State.active](electricvehicleloadevent/session-swift.struct/state-swift.enum/active.md)
  A state that represents all electricity consumption or production events with active states.
- [ElectricVehicleLoadEvent.Session.State.begin](electricvehicleloadevent/session-swift.struct/state-swift.enum/begin.md)
  A state that represents the start of the session.
- [ElectricVehicleLoadEvent.Session.State.end](electricvehicleloadevent/session-swift.struct/state-swift.enum/end.md)
  A state that represents the end of the session.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/session-swift.struct/state-swift.enum)*