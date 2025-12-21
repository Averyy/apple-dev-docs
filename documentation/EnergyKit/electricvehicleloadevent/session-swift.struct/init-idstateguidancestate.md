# init(id:state:guidanceState:)

**Framework**: EnergyKit  
**Kind**: init

Creates an electrical load event session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
init(id: UUID, state: ElectricVehicleLoadEvent.Session.State, guidanceState: ElectricVehicleLoadEvent.Session.GuidanceState)
```

## Parameters

- `id`: The unique identifier for the session.
- `state`: The state of the session.
- `guidanceState`: Identifies the provided guidance and its usability by the load device

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/session-swift.struct/init(id:state:guidancestate:))*