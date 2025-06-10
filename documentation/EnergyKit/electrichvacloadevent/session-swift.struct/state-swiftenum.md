# ElectricHVACLoadEvent.Session.State

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

When a device transitions from from idle to consuming electricity, it must create a load event with [`ElectricHVACLoadEvent.Session.State.begin`](electrichvacloadevent/session-swift.struct/state-swift.enum/begin.md). As it reports events, it sends load events with [`ElectricHVACLoadEvent.Session.State.active`](electrichvacloadevent/session-swift.struct/state-swift.enum/active.md). Once idle, it closes the session with [`ElectricHVACLoadEvent.Session.State.end`](electrichvacloadevent/session-swift.struct/state-swift.enum/end.md).

## Topics

### Setting session states
- [ElectricHVACLoadEvent.Session.State.active](electrichvacloadevent/session-swift.struct/state-swift.enum/active.md)
  A state that represents all electricity consumption events with active states.
- [ElectricHVACLoadEvent.Session.State.begin](electrichvacloadevent/session-swift.struct/state-swift.enum/begin.md)
  A state that represents the start of the session.
- [ElectricHVACLoadEvent.Session.State.end](electrichvacloadevent/session-swift.struct/state-swift.enum/end.md)
  The end of the session when a load device goes to idle, that is, power/stage returns to zero indicating the load device is no longer consuming or generating electricity A state that represents the end of the session.
### Decoding
- [init(from: any Decoder) throws](electrichvacloadevent/session-swift.struct/state-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (ElectricHVACLoadEvent.Session.State, ElectricHVACLoadEvent.Session.State) -> Bool](electrichvacloadevent/session-swift.struct/state-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](electrichvacloadevent/session-swift.struct/state-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](electrichvacloadevent/session-swift.struct/state-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](electrichvacloadevent/session-swift.struct/state-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](electrichvacloadevent/session-swift.struct/state-swift.enum/equatable-implementations.md)

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

- [let id: UUID](electrichvacloadevent/session-swift.struct/id.md)
  The unique identifier for the session.
- [let state: ElectricHVACLoadEvent.Session.State](electrichvacloadevent/session-swift.struct/state-swift.property.md)
  The state of the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent/session-swift.struct/state-swift.enum)*