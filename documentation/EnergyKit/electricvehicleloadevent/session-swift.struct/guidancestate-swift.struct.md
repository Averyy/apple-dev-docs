# ElectricVehicleLoadEvent.Session.GuidanceState

**Framework**: EnergyKit  
**Kind**: struct  
**Role**: Structure

Identifies the provided guidance and its usability by the load device

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
struct GuidanceState
```

## Topics

### Initializers
- [init(wasFollowingGuidance: Bool, guidanceToken: UUID)](./guidancestate-swift.struct/init%28wasfollowingguidance,guidancetoken%29.md)
  Initialize the GuidanceState for the [`ElectricVehicleLoadEvent`](../../electricvehicleloadevent.md)
### Instance Properties
- [var guidanceToken: UUID](./guidancestate-swift.struct/guidancetoken.md)
  The guidance token for the guidance that you requested.
- [let wasFollowingGuidance: Bool](./guidancestate-swift.struct/wasfollowingguidance.md)
  A Boolean value that indicates whether the device was applying the electricity guidance at the time of the event.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
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
- [ElectricVehicleLoadEvent.Session.State](./state-swift.enum.md)
  The state of the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/session-swift.struct/guidancestate-swift.struct)*