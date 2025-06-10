# ElectricVehicleLoadEvent.Session.State

**Framework**: EnergyKit  
**Kind**: enum

The state of the session.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
enum State
```

#### Overview

When a device transitions from from idle to consuming or generating electricity, it must create a load event with [`ElectricVehicleLoadEvent.Session.State.begin`](electricvehicleloadevent/session-swift.struct/state-swift.enum/begin.md). As it reports events, it sends load events with [`ElectricVehicleLoadEvent.Session.State.active`](electricvehicleloadevent/session-swift.struct/state-swift.enum/active.md). Once idle, it closes the session with [`ElectricVehicleLoadEvent.Session.State.end`](electricvehicleloadevent/session-swift.struct/state-swift.enum/end.md).

## Topics

### Operators
- [static func == (ElectricVehicleLoadEvent.Session.State, ElectricVehicleLoadEvent.Session.State) -> Bool](electricvehicleloadevent/session-swift.struct/state-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ElectricVehicleLoadEvent.Session.State.active](electricvehicleloadevent/session-swift.struct/state-swift.enum/active.md)
  A state that represents all electricity consumption or production events with active states.
- [ElectricVehicleLoadEvent.Session.State.begin](electricvehicleloadevent/session-swift.struct/state-swift.enum/begin.md)
  A state that represents the start of the session.
- [ElectricVehicleLoadEvent.Session.State.end](electricvehicleloadevent/session-swift.struct/state-swift.enum/end.md)
  A state that represents the end of the session.
### Initializers
- [init(from: any Decoder) throws](electricvehicleloadevent/session-swift.struct/state-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](electricvehicleloadevent/session-swift.struct/state-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](electricvehicleloadevent/session-swift.struct/state-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](electricvehicleloadevent/session-swift.struct/state-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](electricvehicleloadevent/session-swift.struct/state-swift.enum/equatable-implementations.md)

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