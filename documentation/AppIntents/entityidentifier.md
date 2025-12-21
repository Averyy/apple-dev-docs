# EntityIdentifier

**Framework**: App Intents  
**Kind**: struct

A type that uniquely identifies a specific instance of an app entity.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct EntityIdentifier
```

#### Overview

The value used should be unique across all entities of the given type. Entities which are relevant across executions of the application should have stable identifiers that persist across executions.

Entities, by default, conform to the `Identifiable` protocol. Use a type for the `id` that conforms to [`EntityIdentifierConvertible`](entityidentifierconvertible.md). Default implementations for `String`, `UUID` and `Int` are provided.

For example:

```swift
struct Song: AppEntity {
    let id = UUID()
}
```

## Topics

### Creating an entity identifier
- [init<Entity>(for: Entity)](entityidentifier/init(for:).md)
  Creates an identifier for the specified entity
- [init<Entity>(for: Entity.Type, identifier: Entity.ID)](entityidentifier/init(for:identifier:).md)
  Creates an `EntityIdentifier` representing an instance of the specified entity type backed by the specified identifier value.
- [init?(activityIdentifier: String)](entityidentifier/init(activityidentifier:).md)
### Getting the identifier details
- [let identifier: String](entityidentifier/identifier.md)
  Value uniquely identifying the entity instance within its type
- [let entityType: any AppEntity.Type](entityidentifier/entitytype.md)
  The type of `AppEntity` represented by this identifier
- [static let valueMaximumLength: Int](entityidentifier/valuemaximumlength.md)
  Maximum allowed length for the `identifier` value. This is a constraint imposed by the system and thus forces us to truncate the identifier if it exceeds the maximum length.
### Type Aliases
- [EntityIdentifier.Specification](entityidentifier/specification.md)
- [EntityIdentifier.UnwrappedType](entityidentifier/unwrappedtype.md)
- [EntityIdentifier.ValueType](entityidentifier/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: EmptyResolverSpecification<EntityIdentifier>](entityidentifier/defaultresolverspecification.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol PersistentlyIdentifiable](persistentlyidentifiable.md)
  Defines a string that uniquely identifies a type. This is useful for maintaining the identity of a type, even when its type name is changed.
- [protocol EntityIdentifierConvertible](entityidentifierconvertible.md)
  An interface for converting between an entity’s identifier and its string representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityidentifier)*