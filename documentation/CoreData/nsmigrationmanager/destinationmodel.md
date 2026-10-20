# destinationModel

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The destination model for the migration manager.

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
var destinationModel: NSManagedObjectModel { get }
```

```objc
@property (strong, readonly) NSManagedObjectModel * destinationModel;
```

## See Also

### Related Documentation
- [init(sourceModel: NSManagedObjectModel, destinationModel: NSManagedObjectModel)](./init%28sourcemodel,destinationmodel%29.md)
  Initializes a migration manager instance with given source and destination models.
### Getting the Manager’s Configuration
- [var destinationContext: NSManagedObjectContext](./destinationcontext.md)
  The managed object context the migration manager uses for writing the destination persistent store.
- [var mappingModel: NSMappingModel](./mappingmodel.md)
  The mapping model for the migration manager.
- [var sourceContext: NSManagedObjectContext](./sourcecontext.md)
  The managed object context the migration manager uses for reading the source persistent store.
- [var sourceModel: NSManagedObjectModel](./sourcemodel.md)
  The source model for the migration manager.
- [func destinationEntity(for: NSEntityMapping) -> NSEntityDescription?](./destinationentity%28for%29.md)
  Returns the entity description for the destination entity of a given entity mapping.
- [func sourceEntity(for: NSEntityMapping) -> NSEntityDescription?](./sourceentity%28for%29.md)
  Returns the entity description for the source entity of a given entity mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationmanager/destinationmodel)*