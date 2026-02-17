# deleteAppEntities(identifiedBy:ofType:)

**Framework**: Core Spotlight  
**Kind**: method

Deletes entities with the specified identifiers and type from the current index.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
func deleteAppEntities<Entity>(identifiedBy identifiers: [Entity.ID], ofType type: Entity.Type) async throws where Entity : IndexedEntity
```

#### Discussion

Use this method to remove only the specified entities from the current index. You might call this method as a precursor to indexing a new set of entity objects. To remove all entities of the specified type, call the [`deleteAppEntities(ofType:)`](cssearchableindex/deleteappentities(oftype:).md) method instead.

## Parameters

- `identifiers`: The IDs of the entities you want to delete. Get the identifier value   of an entity from its   property.
- `type`: One of your app’s entity types. For example, specify    to delete entities with the   type in the index.

## See Also

- [func indexAppEntities([some IndexedEntity], priority: Int) async throws](cssearchableindex/indexappentities(_:priority:).md)
  Indexes one or more app entities and assigns an optional priority to them.
- [func deleteAppEntities<Entity>(ofType: Entity.Type) async throws](cssearchableindex/deleteappentities(oftype:).md)
  Deletes all app entities of the specified type from the current index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/deleteappentities(identifiedby:oftype:))*