# init(sourceModel:destinationModel:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Initializes a migration manager instance with given source and destination models.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(sourceModel: NSManagedObjectModel, destinationModel: NSManagedObjectModel)
```

```objc
- (instancetype) initWithSourceModel:(NSManagedObjectModel *) sourceModel destinationModel:(NSManagedObjectModel *) destinationModel;
```

#### Return Value

A migration manager instance initialized to migrate data in a store that uses `sourceModel` to a store that uses `destinationModel`.

#### Discussion

You specify the mapping model in the migration method,  [`migrateStore(from:sourceType:options:with:toDestinationURL:destinationType:destinationOptions:)`](./migratestore%28from,sourcetype,options,with,todestinationurl,destinationtype,destinationoptions%29.md).

##### Special Considerations

This is the designated initializer for `NSMigrationManager`.

Although validation of the models is performed during [`migrateStore(from:sourceType:options:with:toDestinationURL:destinationType:destinationOptions:)`](./migratestore%28from,sourcetype,options,with,todestinationurl,destinationtype,destinationoptions%29.md), as with `NSPersistentStoreCoordinator` once models are added to the migration manager they are immutable and cannot be altered.

## Parameters

- `sourceModel`: The source managed object model for the migration manager.
- `destinationModel`: The destination managed object model for the migration manager.

## See Also

### Related Documentation
- [var destinationModel: NSManagedObjectModel](./destinationmodel.md)
  The destination model for the migration manager.
- [var mappingModel: NSMappingModel](./mappingmodel.md)
  The mapping model for the migration manager.
- [var sourceModel: NSManagedObjectModel](./sourcemodel.md)
  The source model for the migration manager.
- [func migrateStore(from: URL, sourceType: String, options: [AnyHashable : Any]?, with: NSMappingModel?, toDestinationURL: URL, destinationType: String, destinationOptions: [AnyHashable : Any]?) throws](./migratestore%28from,sourcetype,options,with,todestinationurl,destinationtype,destinationoptions%29.md)
  Migrates the store at a given source URL to the store at a given destination URL, performing all of the mappings specified in a given mapping model.
- [Core Data Model Versioning and Data Migration Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/Introduction.html#//apple_ref/doc/uid/TP40004399)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationmanager/init(sourcemodel:destinationmodel:))*