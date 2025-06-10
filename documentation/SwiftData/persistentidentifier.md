# PersistentIdentifier

**Framework**: SwiftData  
**Kind**: struct

A type that describes the aggregate identity of a SwiftData model.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct PersistentIdentifier
```

#### Overview

> **Note**: Decoded [`PersistentIdentifier`](persistentidentifier.md) and identifiers created by the [`DefaultStore`](defaultstore.md) are not considered equivalent.

## Topics

### Accessing identity information
- [let id: PersistentIdentifier.ID](persistentidentifier/id-swift.property.md)
  The value that uniquely identifies the associated model within the containing store.
- [PersistentIdentifier.ID](persistentidentifier/id-swift.struct.md)
  A type that represents the stable identity of a SwiftData model.
- [var storeIdentifier: String?](persistentidentifier/storeidentifier.md)
  The identifier of the store that contains the associated model.
- [var entityName: String](persistentidentifier/entityname.md)
  The entity name for the associated model.
### Encoding and decoding
- [func encode(to: any Encoder) throws](persistentidentifier/encode(to:).md)
  Encodes this value into the given encoder.
- [init(from: any Decoder) throws](persistentidentifier/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Hashing
- [func hash(into: inout Hasher)](persistentidentifier/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing identifiers
- [static func == (PersistentIdentifier, PersistentIdentifier) -> Bool](persistentidentifier/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (PersistentIdentifier, PersistentIdentifier) -> Bool](persistentidentifier/_(_:_:).md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
### Instance Properties
- [var hashValue: Int](persistentidentifier/hashvalue.md)
  The hash value.
### Type Methods
- [static func identifier<T>(for: String, entityName: String, primaryKey: T) throws -> PersistentIdentifier](persistentidentifier/identifier(for:entityname:primarykey:).md)
### Default Implementations
- [Comparable Implementations](persistentidentifier/comparable-implementations.md)
- [Equatable Implementations](persistentidentifier/equatable-implementations.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var persistentModelID: PersistentIdentifier](persistentmodel/persistentmodelid.md)
- [var modelContext: ModelContext?](persistentmodel/modelcontext.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/persistentidentifier)*