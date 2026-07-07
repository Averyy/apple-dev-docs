# SyncableEntityIdentifier

**Framework**: App Intents  
**Kind**: struct

A type-safe wrapper you use to specify different local and stable identifiers for an entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct SyncableEntityIdentifier<LocalID, StableID> where LocalID : EntityIdentifierConvertible, LocalID : Sendable, StableID : EntityIdentifierConvertible, StableID : Sendable
```

## Mentions

- [Defining app entities for your custom data types](defining-app-entities-for-your-custom-data-types.md)

#### Overview

Use this structure if you maintain separate local and stable identifiers in one of your entity types. Assign this structure to the `id` property of your entity and use the value in the [`local`](syncableentityidentifier/local.md) property to refer to the entity in your code. The system uses the [`stable`](syncableentityidentifier/stable.md) value to refer to the same entity during operations that occur on another device.

When referring to an entity in your code, you can refer to this type directly. The following example shows an entity that uses this type for its identifier. The query object for the entity similarly refers to this type directly in methods.

```swift
struct Photo: AppEntity, SyncableEntity {
    var id: SyncableEntityIdentifier<String, String>
    var creationDate: Date
}

struct PhotoQuery: EntityQuery {
    func entities(for ids: [SyncableEntityIdentifier<String, String>]) async throws -> [Photo] {
        // Works everywhere - queries, entities, helper functions
    }
}
```

For additional information about how to use this type, see [`SyncableEntity`](syncableentity.md).

## Topics

### Initializers
- [init(id: LocalID)](syncableentityidentifier/init(id:).md)
  Creates an identifier where the local and stable IDs are identical.
- [init(local: LocalID, stable: StableID)](syncableentityidentifier/init(local:stable:).md)
  Creates an identifier with both local and stable IDs.
### Instance Properties
- [let local: LocalID?](syncableentityidentifier/local.md)
  The identifier you use to refer to the entity on the current device.
- [let stable: StableID?](syncableentityidentifier/stable.md)
  The identifier you use to refer to the entity across devices.
### Default Implementations
- [EntityIdentifierConvertible Implementations](syncableentityidentifier/entityidentifierconvertible-implementations.md)
- [Equatable Implementations](syncableentityidentifier/equatable-implementations.md)
- [Hashable Implementations](syncableentityidentifier/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [EntityIdentifierConvertible](entityidentifierconvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct EntityIdentifier](entityidentifier.md)
  A type that uniquely identifies a specific instance of an app entity.
- [protocol EntityIdentifierConvertible](entityidentifierconvertible.md)
  An interface for converting between an entity’s identifier and its string representation.
- [struct FileEntityIdentifier](fileentityidentifier.md)
  An identifier for an app entity that refers to a document or other file.
- [protocol PersistentlyIdentifiable](persistentlyidentifiable.md)
  Defines a string that uniquely identifies a type. This is useful for maintaining the identity of a type, even when its type name is changed.
- [struct AttributedEntityIdentifier](attributedentityidentifier.md)
  A unique identifier for an app entity instance within an application.
- [struct AttributedTypeIdentifier](attributedtypeidentifier.md)
  A unique identifier for an app entity or transient app entity type within an application bundle.
- [protocol AppEntityAnnotatable](appentityannotatable.md)
  An interface that system types adopt and use to manage their relationship to app entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/syncableentityidentifier)*