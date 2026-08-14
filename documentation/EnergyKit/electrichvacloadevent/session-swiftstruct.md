# ElectricHVACLoadEvent.Session

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
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let id: UUID](electrichvacloadevent/id.md)
  The unique identifier of the electrical load event.
- [let timestamp: Date](electrichvacloadevent/timestamp.md)
  The timestamp for when the event occurred.
- [let session: ElectricHVACLoadEvent.Session](electrichvacloadevent/session-swift.property.md)
  The session information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/session-swift.struct)*