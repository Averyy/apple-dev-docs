# init(for:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

Creates an identifier for the specified entity.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
init<Entity>(for entity: Entity) where Entity : AppEntity
```

#### Discussion

For entities adopting [`SyncableEntity`](../syncableentity.md), this initializer extracts the stable ID:

- **Passthrough case**: If the entity’s ID is already stable (like `UUID`), it’s used as both local and stable ID
- **Mapped case**: If the entity’s ID uses [`SyncableEntityIdentifier`](../syncableentityidentifier.md), the stable ID is extracted from the wrapper

The stable ID is used for cross-device entity resolution via Campo session syncing.

## Parameters

- `entity`: The entity for which to create an identifier

## See Also

### Creating an entity identifier
- [init<Entity>(for: Entity.Type, identifier: Entity.ID)](./init%28for,identifier%29.md)
  Creates an `EntityIdentifier` representing an instance of the specified entity type backed by the specified identifier value.
- [init?(activityIdentifier: String)](./init%28activityidentifier%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityidentifier/init(for:))*