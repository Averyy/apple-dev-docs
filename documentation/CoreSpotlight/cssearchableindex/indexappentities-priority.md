# indexAppEntities(_:priority:)

**Framework**: Core Spotlight  
**Kind**: method

Indexes one or more app entities and assigns an optional priority to them.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
func indexAppEntities(_ appEntities: [some IndexedEntity], priority: Int = 0) async throws
```

#### Discussion

Use this method to index the [`AppEntity`](https://developer.apple.com/documentation/AppIntents/AppEntity) instances you create for your app’s content. For each object in `appEntities`, Spotlight identifies the indexable content and adds it to your app’s index. However, the indexing process isn’t recursive, and this method doesn’t index any child entities contained inside your entity objects. To index both parent and child entities, you must add each object separately to the `appEntities` parameter.

Indexing your app’s entities has some specific benefits. If your app also provides [`OpenIntent`](https://developer.apple.com/documentation/AppIntents/OpenIntent) types for its entities, Spotlight can use those types to open your app and display an entity’s content when someone selects it in search results.

Call this method as an alternative to creating and indexing [`CSSearchableItem`](cssearchableitem.md) types for your content. If you index a searchable item and entity for the same content, Spotlight creates separate entries for each one in your app’s index. If you want to use your existing code to create searchable items, you can call the [`associateAppEntity(_:priority:)`](cssearchableitemattributeset/associateappentity(_:priority:).md) method to associate an entity with each of your items. Doing so gives you the same benefits as indexing the entity on its own, without creating multiple entries for the item in the app’s index.

## Parameters

- `appEntities`: One or more app entities you want to donate to Spotlight. Each entity must conform to the [`IndexedEntity`](https://developer.apple.com/documentation/AppIntents/IndexedEntity) protocol.
- `priority`: The importance of these donated items relative to your app’s other items. If you don’t specify a priority, this method assigns a priority of 0 to the items. Specify a higher number to prioritize the entities over other items you add to the index. The App Intents system uses priorities to determine what items to show in suggestions and other places.

## See Also

- [func deleteAppEntities<Entity>(ofType: Entity.Type) async throws](cssearchableindex/deleteappentities(oftype:).md)
  Deletes all app entities of the specified type from the current index.
- [func deleteAppEntities<Entity>(identifiedBy: [Entity.ID], ofType: Entity.Type) async throws](cssearchableindex/deleteappentities(identifiedby:oftype:).md)
  Deletes entities with the specified identifiers and type from the current index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/indexappentities(_:priority:))*