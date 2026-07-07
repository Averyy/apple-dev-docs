# EntityIdentifier

**Framework**: App Intents  
**Kind**: struct

A type that uniquely identifies a specific instance of an app entity.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
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

#### Cross Device Stable Identifiers

For entities that adopt `_SyncableEntity`, the framework automatically extracts stable identifiers for cross-device session syncing:

- **Passthrough case**: If your entity’s ID is already stable across devices (like server UUIDs), just adopt `_SyncableEntity` with no other changes. The framework uses your ID as both the local and stable identifier.
- **Mapped case**: If your entity has different local and stable identifiers, use `_SyncableEntityIdentifier` as your ID type. The framework extracts the stable ID from the wrapper.
- **Custom identifier case**: If your entity uses a custom ID type that conforms to `_SyncableEntityIdentifierProviding`, the framework extracts the stable ID via the protocol’s `stableIdentifierString` property.

Apps never interact with `EntityIdentifier.stableIdentifier` directly - they work with their entity’s ID type (plain types like `UUID`, `_SyncableEntityIdentifier` for mapped IDs, or custom types conforming to `_SyncableEntityIdentifierProviding`).

The stable identifier is NOT used for equality or hashing - two `EntityIdentifier` instances are equal if they have the same type and local identifier, regardless of stable identifier value.

## Topics

### Creating an entity identifier
- [init<Entity>(for: Entity)](entityidentifier/init(for:).md)
  Creates an identifier for the specified entity.
- [init<Entity>(for: Entity.Type, identifier: Entity.ID)](entityidentifier/init(for:identifier:).md)
  Creates an `EntityIdentifier` representing an instance of the specified entity type backed by the specified identifier value.
- [init?(activityIdentifier: String)](entityidentifier/init(activityidentifier:).md)
### Getting the identifier details
- [let identifier: String](entityidentifier/identifier.md)
  Value uniquely identifying the entity instance within its type.
- [let entityType: any AppEntity.Type](entityidentifier/entitytype.md)
  The type of `AppEntity` represented by this identifier
- [static let valueMaximumLength: Int](entityidentifier/valuemaximumlength.md)
  Maximum allowed length for the `identifier` value. This is a constraint imposed by the system and thus forces us to truncate the identifier if it exceeds the maximum length.
### Operators
- [static func == (EntityIdentifier, EntityIdentifier) -> Bool](entityidentifier/==(_:_:).md)
  Compares two entity identifiers for equality.
### Instance Methods
- [func hash(into: inout Hasher)](entityidentifier/hash(into:).md)
  Hashes the entity identifier.
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
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol EntityIdentifierConvertible](entityidentifierconvertible.md)
  An interface for converting between an entity’s identifier and its string representation.
- [struct FileEntityIdentifier](fileentityidentifier.md)
  An identifier for an app entity that refers to a document or other file.
- [protocol PersistentlyIdentifiable](persistentlyidentifiable.md)
  Defines a string that uniquely identifies a type. This is useful for maintaining the identity of a type, even when its type name is changed.
- [struct SyncableEntityIdentifier](syncableentityidentifier.md)
  A type-safe wrapper you use to specify different local and stable identifiers for an entity.
- [struct AttributedEntityIdentifier](attributedentityidentifier.md)
  A unique identifier for an app entity instance within an application.
- [struct AttributedTypeIdentifier](attributedtypeidentifier.md)
  A unique identifier for an app entity or transient app entity type within an application bundle.
- [protocol AppEntityAnnotatable](appentityannotatable.md)
  An interface that system types adopt and use to manage their relationship to app entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityidentifier)*