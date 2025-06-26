# CellularService

**Framework**: LiveCommunicationKit  
**Kind**: struct

Struct representing an account which can be used to dial a call

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct CellularService
```

## Topics

### Operators
- [static func == (CellularService, CellularService) -> Bool](cellularservice/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](cellularservice/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](cellularservice/hashvalue.md)
  The hash value.
- [let id: UUID](cellularservice/id-swift.property.md)
  The unique identifier for this account
- [let label: String](cellularservice/label.md)
  The user-visible label for this account…
### Instance Methods
- [func encode(to: any Encoder) throws](cellularservice/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](cellularservice/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [CellularService.ID](cellularservice/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [Equatable Implementations](cellularservice/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/cellularservice)*