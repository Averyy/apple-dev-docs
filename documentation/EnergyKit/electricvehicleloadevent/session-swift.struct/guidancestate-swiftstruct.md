# ElectricVehicleLoadEvent.Session.GuidanceState

**Framework**: EnergyKit  
**Kind**: struct

Identifies the provided guidance and its usability by the load device

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
struct GuidanceState
```

## Topics

### Initializers
- [init(wasFollowingGuidance: Bool, guidanceToken: UUID)](electricvehicleloadevent/session-swift.struct/guidancestate-swift.struct/init(wasfollowingguidance:guidancetoken:).md)
  Initialize the GuidanceState for the [`ElectricVehicleLoadEvent`](electricvehicleloadevent.md)
### Instance Properties
- [var guidanceToken: UUID](electricvehicleloadevent/session-swift.struct/guidancestate-swift.struct/guidancetoken.md)
  The guidance token for the guidance that you requested.
- [let wasFollowingGuidance: Bool](electricvehicleloadevent/session-swift.struct/guidancestate-swift.struct/wasfollowingguidance.md)
  A Boolean value that indicates whether the device was applying the electricity guidance at the time of the event.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
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
- [ElectricVehicleLoadEvent.Session.State](electricvehicleloadevent/session-swift.struct/state-swift.enum.md)
  The state of the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/session-swift.struct/guidancestate-swift.struct)*