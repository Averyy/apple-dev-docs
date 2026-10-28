# deleteAppEntities(ofType:)

**Framework**: Core Spotlight  
**Kind**: method  
**Role**: Instance Method

Deletes all app entities of the specified type from the current index.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
func deleteAppEntities<Entity>(ofType entityType: Entity.Type) async throws where Entity : IndexedEntity
```

## Discussion

This method removes all entities of the specified type from the app’s indexes. You might call this method as a precursor to indexing a new set of entity objects.

## Parameters

- `entityType`: One of your app’s entity types. For example, specify `MyEntity.Type` to delete all instances of `MyEntity` you added to the index.

## See Also

### Indexing app entities
- [func indexAppEntities([some IndexedEntity], priority: Int) async throws](./indexappentities%28_,priority%29.md)
  Indexes one or more app entities and assigns an optional priority to them.
- [func deleteAppEntities<Entity>(identifiedBy: [Entity.ID], ofType: Entity.Type) async throws](./deleteappentities%28identifiedby,oftype%29.md)
  Deletes entities with the specified identifiers and type from the current index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/deleteappentities(oftype:))*