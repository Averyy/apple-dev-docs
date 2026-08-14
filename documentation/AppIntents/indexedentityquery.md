# IndexedEntityQuery

**Framework**: App Intents  
**Kind**: protocol

An interface that adds Spotlight reindexing support to your entity query.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol IndexedEntityQuery : EntityQuery where Self.Entity : IndexedEntity
```

## Mentions

- [Making app entities available in Spotlight](making-app-entities-available-in-spotlight.md)
- [Defining app entities for your custom data types](defining-app-entities-for-your-custom-data-types.md)

#### Overview

Adopt this protocol in query types for app entities that you donate to your app’s Spotlight index using the [`indexAppEntities(_:priority:)`](https://developer.apple.com/documentation/corespotlight/cssearchableindex/indexappentities(_:priority:)) method. When the system encounters an issue with an app’s index, it can ask that app to reindex its content. During reindexing, the system calls the methods of this protocol if your query type supports the protocol. If your type doesn’t support the protocol, Spotlight continues to ask your app’s [`CSSearchableIndexDelegate`](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate) object to reindex any content. Similarly, if you donated an entity by associating it with a [`CSSearchableItem`](https://developer.apple.com/documentation/corespotlight/cssearchableitem) type, Spotlight uses your [`CSSearchableIndexDelegate`](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate) object.

Implement the methods of this protocol and use them to retrieve the specified entities and donate them again to Spotlight. The following example shows the implementation of this protocol for a photos app. The methods fetch the requested app entities and donate them again using the app’s preferred searchable index.

```swift
struct PhotoQuery: IndexedEntityQuery {
    func reindexEntities(for identifiers: [PhotoEntity.ID], indexDescription: CSSearchableIndexDescription) async throws {
        let photos = try await photoStore.fetch(ids: identifiers)
        try await CSSearchableIndex(name: “MyPhotosApp”).indexAppEntities(photos)
    }

    func reindexAllEntities(indexDescription: CSSearchableIndexDescription) async throws {
        let allPhotos = try await photoStore.fetchAll()
        try await CSSearchableIndex(name: “MyPhotosApp”).indexAppEntities(allPhotos)
    }
}
```

For more information about indexing your app entites, see [`Making app entities available in Spotlight`](making-app-entities-available-in-spotlight.md).

## Topics

### Instance Methods
- [func reindexAllEntities(indexDescription: CSSearchableIndexDescription) async throws](indexedentityquery/reindexallentities(indexdescription:).md)
  Reindexes all entities in the app index with the specified characteristics.
- [func reindexEntities(for: [Self.Entity.ID], indexDescription: CSSearchableIndexDescription) async throws](indexedentityquery/reindexentities(for:indexdescription:).md)
  Reindexes a specific subset of app entities within an index.

## Relationships

### Inherits From
- [DynamicOptionsProvider](dynamicoptionsprovider.md)
- [EntityQuery](entityquery.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol IndexedEntity](indexedentity.md)
  An interface that allows you to include an entity in your app’s Spotlight index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/indexedentityquery)*