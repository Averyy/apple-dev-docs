# CellularServiceState

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that contains information about a cellular service.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct CellularServiceState
```

## Topics

### Accessing state properties
- [let id: CellularServiceID](cellularservicestate/id-swift.property.md)
  The cellular service identifier associated with this instance.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [let label: String](cellularservicestate/label.md)
  The label for a service, as set by the person using the device.
### Encoding and decoding
- [init(from: any Decoder) throws](cellularservicestate/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (CellularServiceState, CellularServiceState) -> Bool](cellularservicestate/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](cellularservicestate/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](cellularservicestate/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](cellularservicestate/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [CellularServiceState.ID](cellularservicestate/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [Equatable Implementations](cellularservicestate/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var cellularServices: [CellularServiceState]](telephonymessagingsession/cellularservices.md)
  An array of cellular services available on the system.
- [var cellularServiceStateUpdates: some AsyncSequence<CellularServiceState, Never>](telephonymessagingsession/cellularservicestateupdates.md)
  An asynchronous sequence of cellular service state updates produced by this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/cellularservicestate)*