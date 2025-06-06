# sourceModel

**Framework**: Core Data  
**Kind**: property

The source model for the migration manager.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var sourceModel: NSManagedObjectModel { get }
```

## See Also

- [init(sourceModel: NSManagedObjectModel, destinationModel: NSManagedObjectModel)](nsmigrationmanager/init(sourcemodel:destinationmodel:).md)
  Initializes a migration manager instance with given source and destination models.
- [var destinationContext: NSManagedObjectContext](nsmigrationmanager/destinationcontext.md)
  The managed object context the migration manager uses for writing the destination persistent store.
- [var destinationModel: NSManagedObjectModel](nsmigrationmanager/destinationmodel.md)
  The destination model for the migration manager.
- [var mappingModel: NSMappingModel](nsmigrationmanager/mappingmodel.md)
  The mapping model for the migration manager.
- [var sourceContext: NSManagedObjectContext](nsmigrationmanager/sourcecontext.md)
  The managed object context the migration manager uses for reading the source persistent store.
- [func destinationEntity(for: NSEntityMapping) -> NSEntityDescription?](nsmigrationmanager/destinationentity(for:).md)
  Returns the entity description for the destination entity of a given entity mapping.
- [func sourceEntity(for: NSEntityMapping) -> NSEntityDescription?](nsmigrationmanager/sourceentity(for:).md)
  Returns the entity description for the source entity of a given entity mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationmanager/sourcemodel)*