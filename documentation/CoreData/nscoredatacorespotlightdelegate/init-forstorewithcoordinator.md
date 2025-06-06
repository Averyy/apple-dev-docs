# init(forStoreWith:coordinator:)

**Framework**: Core Data  
**Kind**: init

Creates a Core Spotlight delegate with the specified store description and coordinator.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
init(forStoreWith description: NSPersistentStoreDescription, coordinator psc: NSPersistentStoreCoordinator)
```

#### Discussion

After you initialize a Core Spotlight delegate, call the [`startSpotlightIndexing()`](nscoredatacorespotlightdelegate/startspotlightindexing().md) to begin indexing your store’s contents.

> **Note**:  If you initialize your Core Spotlight delegate using this method, you don’t need to set the [`NSCoreDataCoreSpotlightExporter`](nscoredatacorespotlightexporter.md) option on the specified store description.

 If you initialize your Core Spotlight delegate using this method, you don’t need to set the [`NSCoreDataCoreSpotlightExporter`](nscoredatacorespotlightexporter.md) option on the specified store description.

## Parameters

- `description`: An object that describes the persistent store that contains the entities to index.
- `psc`: The persistent store coordinator, which you initialize with the managed object model that contains the definitions of the entities to index.

## See Also

- [convenience init(forStoreWith: NSPersistentStoreDescription, model: NSManagedObjectModel)](nscoredatacorespotlightdelegate/init(forstorewith:model:).md)
  Creates a Core Spotlight delegate with the specified store description and managed object model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/init(forstorewith:coordinator:))*