# NSCoreDataCoreSpotlightDelegate

**Framework**: Core Data  
**Kind**: class

A set of methods that enable integration with Core Spotlight.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
class NSCoreDataCoreSpotlightDelegate
```

#### Overview

> **Note**:  Core Spotlight integration is only available for persistent stores that have a store type of [`sqlite`](nspersistentstore/storetype/sqlite.md), and which use persistent history tracking. For more information, see [`Consuming relevant store changes`](consuming-relevant-store-changes.md).

 Core Spotlight integration is only available for persistent stores that have a store type of [`sqlite`](nspersistentstore/storetype/sqlite.md), and which use persistent history tracking. For more information, see [`Consuming relevant store changes`](consuming-relevant-store-changes.md).

## Topics

### Creating a Core Spotlight Delegate
- [init(forStoreWith: NSPersistentStoreDescription, coordinator: NSPersistentStoreCoordinator)](nscoredatacorespotlightdelegate/init(forstorewith:coordinator:).md)
  Creates a Core Spotlight delegate with the specified store description and coordinator.
- [convenience init(forStoreWith: NSPersistentStoreDescription, model: NSManagedObjectModel)](nscoredatacorespotlightdelegate/init(forstorewith:model:).md)
  Creates a Core Spotlight delegate with the specified store description and managed object model.
### Configuring the Index
- [var isIndexingEnabled: Bool](nscoredatacorespotlightdelegate/isindexingenabled.md)
  A Boolean value that indicates whether Core Data is currently updating the Core Spotlight index with the persistent store’s entities.
- [func domainIdentifier() -> String](nscoredatacorespotlightdelegate/domainidentifier.md)
  Returns the domain identifier.
- [func indexName() -> String?](nscoredatacorespotlightdelegate/indexname.md)
  Returns the index’s name.
### Managing the Index
- [func attributeSet(for: NSManagedObject) -> CSSearchableItemAttributeSet?](nscoredatacorespotlightdelegate/attributeset(for:).md)
  Returns the searchable attributes for the specified managed object.
- [func deleteSpotlightIndex(completionHandler: ((any Error)?) -> Void)](nscoredatacorespotlightdelegate/deletespotlightindex(completionhandler:).md)
  Deletes all searchable items from the configured index.
- [func startSpotlightIndexing()](nscoredatacorespotlightdelegate/startspotlightindexing.md)
  Starts the indexing of the store’s entities.
- [func stopSpotlightIndexing()](nscoredatacorespotlightdelegate/stopspotlightindexing.md)
  Stops the indexing of the store’s entities.
### Updating the Index
- [static let indexDidUpdateNotification: Notification.Name](nscoredatacorespotlightdelegate/indexdidupdatenotification.md)
  The notification the delegate posts after Spotlight updates the index.
- [func searchableIndex(CSSearchableIndex, reindexAllSearchableItemsWithAcknowledgementHandler: () -> Void)](nscoredatacorespotlightdelegate/searchableindex(_:reindexallsearchableitemswithacknowledgementhandler:).md)
  Reindexes all searchable items and clears any local state.
- [func searchableIndex(CSSearchableIndex, reindexSearchableItemsWithIdentifiers: [String], acknowledgementHandler: () -> Void)](nscoredatacorespotlightdelegate/searchableindex(_:reindexsearchableitemswithidentifiers:acknowledgementhandler:).md)
  Reindexes the searchable items for the specified identifiers.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [let NSCoreDataCoreSpotlightExporter: String](nscoredatacorespotlightexporter.md)
  The key you use to specify your Core Spotlight delegate.
- [Spotlight record keys](spotlight-record-keys.md)
  The keys for the values that exist in Spotlight’s external record files.
- [Showcase App Data in Spotlight](showcase-app-data-in-spotlight.md)
  Index app data so users can find it by using Spotlight search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate)*