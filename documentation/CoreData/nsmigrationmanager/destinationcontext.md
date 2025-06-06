# destinationContext

**Framework**: Core Data  
**Kind**: property

The managed object context the migration manager uses for writing the destination persistent store.

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
var destinationContext: NSManagedObjectContext { get }
```

#### Discussion

This context is created on demand as part of the initialization of the Core Data stacks used for migration.

## See Also

- [var destinationModel: NSManagedObjectModel](nsmigrationmanager/destinationmodel.md)
  The destination model for the migration manager.
- [var mappingModel: NSMappingModel](nsmigrationmanager/mappingmodel.md)
  The mapping model for the migration manager.
- [var sourceContext: NSManagedObjectContext](nsmigrationmanager/sourcecontext.md)
  The managed object context the migration manager uses for reading the source persistent store.
- [var sourceModel: NSManagedObjectModel](nsmigrationmanager/sourcemodel.md)
  The source model for the migration manager.
- [func destinationEntity(for: NSEntityMapping) -> NSEntityDescription?](nsmigrationmanager/destinationentity(for:).md)
  Returns the entity description for the destination entity of a given entity mapping.
- [func sourceEntity(for: NSEntityMapping) -> NSEntityDescription?](nsmigrationmanager/sourceentity(for:).md)
  Returns the entity description for the source entity of a given entity mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationmanager/destinationcontext)*