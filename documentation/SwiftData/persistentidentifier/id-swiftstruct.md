# PersistentIdentifier.ID

**Framework**: SwiftData  
**Kind**: struct

A type that represents the stable identity of a SwiftData model.

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
struct ID
```

## Topics

### Hashing
- [func hash(into: inout Hasher)](persistentidentifier/id-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing IDs
- [static func == (PersistentIdentifier.ID, PersistentIdentifier.ID) -> Bool](persistentidentifier/id-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](persistentidentifier/id-swift.struct/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](persistentidentifier/id-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let id: PersistentIdentifier.ID](persistentidentifier/id-swift.property.md)
  The value that uniquely identifies the associated model within the containing store.
- [var storeIdentifier: String?](persistentidentifier/storeidentifier.md)
  The identifier of the store that contains the associated model.
- [var entityName: String](persistentidentifier/entityname.md)
  The entity name for the associated model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/persistentidentifier/id-swift.struct)*