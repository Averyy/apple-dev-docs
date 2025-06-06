# init(forStoreWith:model:)

**Framework**: Core Data  
**Kind**: init

Creates a Core Spotlight delegate with the specified store description and managed object model.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
convenience init(forStoreWith description: NSPersistentStoreDescription, model: NSManagedObjectModel)
```

## Parameters

- `description`: An object that describes the persistent store that contains the entities to index.
- `model`: The managed object model that contains the definitions of the entities to index.

## See Also

- [init(forStoreWith: NSPersistentStoreDescription, coordinator: NSPersistentStoreCoordinator)](nscoredatacorespotlightdelegate/init(forstorewith:coordinator:).md)
  Creates a Core Spotlight delegate with the specified store description and coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/init(forstorewith:model:))*