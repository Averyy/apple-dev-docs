# ElectricVehicleLoadEvent.Session.State

**Framework**: EnergyKit  
**Kind**: enum  
**Role**: Enumeration

The state of the session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
enum State
```

## Overview

When a device transitions from from idle to consuming or generating electricity, it must create a load event with [`ElectricVehicleLoadEvent.Session.State.begin`](./state-swift.enum/begin.md). As it reports events, it sends load events with [`ElectricVehicleLoadEvent.Session.State.active`](./state-swift.enum/active.md). Once idle, it closes the session with [`ElectricVehicleLoadEvent.Session.State.end`](./state-swift.enum/end.md).

## Topics

### Enumeration Cases
- [ElectricVehicleLoadEvent.Session.State.active](./state-swift.enum/active.md)
  A state that represents all electricity consumption or production events with active states.
- [ElectricVehicleLoadEvent.Session.State.begin](./state-swift.enum/begin.md)
  A state that represents the start of the session.
- [ElectricVehicleLoadEvent.Session.State.end](./state-swift.enum/end.md)
  A state that represents the end of the session.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Creating a load event
- [init(id: UUID, state: ElectricVehicleLoadEvent.Session.State, guidanceState: ElectricVehicleLoadEvent.Session.GuidanceState)](./init%28id,state,guidancestate%29.md)
  Creates an electrical load event session.
- [let guidanceState: ElectricVehicleLoadEvent.Session.GuidanceState](./guidancestate-swift.property.md)
  Identifies the provided guidance and its usability by the load device
- [let id: UUID](./id.md)
  The unique identifier for the session.
- [let state: ElectricVehicleLoadEvent.Session.State](./state-swift.property.md)
  The state of the session.
- [ElectricVehicleLoadEvent.Session.GuidanceState](./guidancestate-swift.struct.md)
  Identifies the provided guidance and its usability by the load device


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/session-swift.struct/state-swift.enum)*