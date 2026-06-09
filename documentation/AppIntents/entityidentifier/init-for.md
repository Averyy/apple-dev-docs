# init(for:)

**Framework**: App Intents  
**Kind**: init

Creates an identifier for the specified entity.

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
init<Entity>(for entity: Entity) where Entity : AppEntity
```

#### Discussion

For entities adopting `_SyncableEntity`, this initializer extracts the stable ID:

- **Passthrough case**: If the entity’s ID is already stable (like `UUID`), it’s used as both local and stable ID
- **Mapped case**: If the entity’s ID uses `_SyncableEntityIdentifier`, the stable ID is extracted from the wrapper
- **Custom identifier case**: If the entity’s ID conforms to `_SyncableEntityIdentifierProviding`, the stable ID is extracted via `stableIdentifierString`

The stable ID is used for cross-device entity resolution via Campo session syncing.

## Parameters

- `entity`: The entity for which to create an identifier

## See Also

- [init<Entity>(for: Entity.Type, identifier: Entity.ID)](entityidentifier/init(for:identifier:).md)
  Creates an `EntityIdentifier` representing an instance of the specified entity type backed by the specified identifier value.
- [init?(activityIdentifier: String)](entityidentifier/init(activityidentifier:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityidentifier/init(for:))*