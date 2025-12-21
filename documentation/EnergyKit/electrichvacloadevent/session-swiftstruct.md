# ElectricHVACLoadEvent.Session

**Framework**: EnergyKit  
**Kind**: struct

A session that tracks the event.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
struct Session
```

#### Overview

A session starts when a device transitions from idle to consuming electricity. It’s active when consuming electricity. It ends when the device stops consuming electricity.

## Topics

### Creating a session
- [init(id: UUID, state: ElectricHVACLoadEvent.Session.State, guidanceState: ElectricHVACLoadEvent.Session.GuidanceState)](electrichvacloadevent/session-swift.struct/init(id:state:guidancestate:).md)
  Creates an electrical load event session.
### Getting the session information
- [let id: UUID](electrichvacloadevent/session-swift.struct/id.md)
  The unique identifier for the session.
- [let state: ElectricHVACLoadEvent.Session.State](electrichvacloadevent/session-swift.struct/state-swift.property.md)
  The state of the session.
- [ElectricHVACLoadEvent.Session.State](electrichvacloadevent/session-swift.struct/state-swift.enum.md)
  The state of the session.
### Identifying the guidance state
- [ElectricHVACLoadEvent.Session.GuidanceState](electrichvacloadevent/session-swift.struct/guidancestate-swift.struct.md)
  Identifies the provided guidance and its usability by the load device
- [let guidanceState: ElectricHVACLoadEvent.Session.GuidanceState](electrichvacloadevent/session-swift.struct/guidancestate-swift.property.md)
  Identifies the provided guidance and its usability by the load device

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(timestamp: Date, measurement: ElectricHVACLoadEvent.ElectricalMeasurement, session: ElectricHVACLoadEvent.Session, deviceID: String)](electrichvacloadevent/init(timestamp:measurement:session:deviceid:).md)
  Creates an electric HVAC load event.
- [ElectricHVACLoadEvent.ElectricalMeasurement](electrichvacloadevent/electricalmeasurement.md)
  A description of the electricity consumed by a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/session-swift.struct)*