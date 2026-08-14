# ElectricHVACLoadEvent.Session.State

**Framework**: EnergyKit  
**Kind**: enum

The state of the session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
enum State
```

#### Overview

When a device transitions from from idle to consuming electricity, it must create a load event with [`ElectricHVACLoadEvent.Session.State.begin`](electrichvacloadevent/session-swift.struct/state-swift.enum/begin.md). As it reports events, it sends load events with [`ElectricHVACLoadEvent.Session.State.active`](electrichvacloadevent/session-swift.struct/state-swift.enum/active.md). Once idle, it closes the session with [`ElectricHVACLoadEvent.Session.State.end`](electrichvacloadevent/session-swift.struct/state-swift.enum/end.md).

## Topics

### Setting session states
- [ElectricHVACLoadEvent.Session.State.active](electrichvacloadevent/session-swift.struct/state-swift.enum/active.md)
  A state that represents all electricity consumption events with active states.
- [ElectricHVACLoadEvent.Session.State.begin](electrichvacloadevent/session-swift.struct/state-swift.enum/begin.md)
  A state that represents the start of the session.
- [ElectricHVACLoadEvent.Session.State.end](electrichvacloadevent/session-swift.struct/state-swift.enum/end.md)
  A state that represents the end of the session.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let id: UUID](electrichvacloadevent/session-swift.struct/id.md)
  The unique identifier for the session.
- [let state: ElectricHVACLoadEvent.Session.State](electrichvacloadevent/session-swift.struct/state-swift.property.md)
  The state of the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/session-swift.struct/state-swift.enum)*