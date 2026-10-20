# sourceEntity(for:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns the entity description for the source entity of a given entity mapping.

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
func sourceEntity(for mEntity: NSEntityMapping) -> NSEntityDescription?
```

```objc
- (NSEntityDescription *) sourceEntityForEntityMapping:(NSEntityMapping *) mEntity;
```

#### Return Value

The entity description for the source entity of `mEntity`.

#### Discussion

Entity mappings do not store the actual description objects, but rather the name and version information of the entity.

## Parameters

- `mEntity`: An entity mapping.

## See Also

### Getting the Manager’s Configuration
- [var destinationContext: NSManagedObjectContext](./destinationcontext.md)
  The managed object context the migration manager uses for writing the destination persistent store.
- [var destinationModel: NSManagedObjectModel](./destinationmodel.md)
  The destination model for the migration manager.
- [var mappingModel: NSMappingModel](./mappingmodel.md)
  The mapping model for the migration manager.
- [var sourceContext: NSManagedObjectContext](./sourcecontext.md)
  The managed object context the migration manager uses for reading the source persistent store.
- [var sourceModel: NSManagedObjectModel](./sourcemodel.md)
  The source model for the migration manager.
- [func destinationEntity(for: NSEntityMapping) -> NSEntityDescription?](./destinationentity%28for%29.md)
  Returns the entity description for the destination entity of a given entity mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationmanager/sourceentity(for:))*