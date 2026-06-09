# init(for:identifier:)

**Framework**: App Intents  
**Kind**: init

Creates an `EntityIdentifier` representing an instance of the specified entity type backed by the specified identifier value.

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
init<Entity>(for entityType: Entity.Type, identifier: Entity.ID) where Entity : AppEntity
```

#### Discussion

For entity types adopting `_SyncableEntity`, this initializer extracts the stable ID:

- **Passthrough case**: If the ID is already stable (like `UUID`), it’s used as both local and stable ID
- **Mapped case**: If the ID uses `_SyncableEntityIdentifier`, the stable ID is extracted from the wrapper
- **Custom identifier case**: If the ID conforms to `_SyncableEntityIdentifierProviding`, the stable ID is extracted via `stableIdentifierString`

## Parameters

- `entityType`: The type of the entity
- `identifier`: The identifier value for the entity

## See Also

- [init<Entity>(for: Entity)](entityidentifier/init(for:).md)
  Creates an identifier for the specified entity.
- [init?(activityIdentifier: String)](entityidentifier/init(activityidentifier:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityidentifier/init(for:identifier:))*