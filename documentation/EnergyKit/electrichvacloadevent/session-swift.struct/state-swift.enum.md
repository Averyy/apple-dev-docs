# ElectricHVACLoadEvent.Session.State

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

When a device transitions from from idle to consuming electricity, it must create a load event with [`ElectricHVACLoadEvent.Session.State.begin`](./state-swift.enum/begin.md). As it reports events, it sends load events with [`ElectricHVACLoadEvent.Session.State.active`](./state-swift.enum/active.md). Once idle, it closes the session with [`ElectricHVACLoadEvent.Session.State.end`](./state-swift.enum/end.md).

## Topics

### Setting session states
- [ElectricHVACLoadEvent.Session.State.active](./state-swift.enum/active.md)
  A state that represents all electricity consumption events with active states.
- [ElectricHVACLoadEvent.Session.State.begin](./state-swift.enum/begin.md)
  A state that represents the start of the session.
- [ElectricHVACLoadEvent.Session.State.end](./state-swift.enum/end.md)
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

### Getting the session information
- [let id: UUID](./id.md)
  The unique identifier for the session.
- [let state: ElectricHVACLoadEvent.Session.State](./state-swift.property.md)
  The state of the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/session-swift.struct/state-swift.enum)*