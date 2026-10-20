# id

**Framework**: EnergyKit  
**Kind**: property  
**Role**: Instance Property

The unique identifier for the session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
let id: UUID
```

## See Also

### Creating a load event
- [init(id: UUID, state: ElectricVehicleLoadEvent.Session.State, guidanceState: ElectricVehicleLoadEvent.Session.GuidanceState)](./init%28id,state,guidancestate%29.md)
  Creates an electrical load event session.
- [let guidanceState: ElectricVehicleLoadEvent.Session.GuidanceState](./guidancestate-swift.property.md)
  Identifies the provided guidance and its usability by the load device
- [let state: ElectricVehicleLoadEvent.Session.State](./state-swift.property.md)
  The state of the session.
- [ElectricVehicleLoadEvent.Session.GuidanceState](./guidancestate-swift.struct.md)
  Identifies the provided guidance and its usability by the load device
- [ElectricVehicleLoadEvent.Session.State](./state-swift.enum.md)
  The state of the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/session-swift.struct/id)*