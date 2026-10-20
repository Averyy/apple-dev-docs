# init(forStoreWith:model:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Creates a Core Spotlight delegate with the specified store description and managed object model.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.13+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`init(forStoreWith:coordinator:)`](./init%28forstorewith,coordinator%29.md) instead.

## Declaration

```swift
convenience init(forStoreWith description: NSPersistentStoreDescription, model: NSManagedObjectModel)
```

```objc
- (instancetype) initForStoreWithDescription:(NSPersistentStoreDescription *) description model:(NSManagedObjectModel *) model;
```

## Parameters

- `description`: An object that describes the persistent store that contains the entities to index.
- `model`: The managed object model that contains the definitions of the entities to index.

## See Also

### Creating a Core Spotlight Delegate
- [init(forStoreWith: NSPersistentStoreDescription, coordinator: NSPersistentStoreCoordinator)](./init%28forstorewith,coordinator%29.md)
  Creates a Core Spotlight delegate with the specified store description and coordinator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscoredatacorespotlightdelegate/init(forstorewith:model:))*