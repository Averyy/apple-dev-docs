# mappingModel

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The mapping model for the migration manager.

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
var mappingModel: NSMappingModel { get }
```

```objc
@property (strong, readonly) NSMappingModel * mappingModel;
```

## See Also

### Related Documentation
- [func migrateStore(from: URL, sourceType: String, options: [AnyHashable : Any]?, with: NSMappingModel?, toDestinationURL: URL, destinationType: String, destinationOptions: [AnyHashable : Any]?) throws](./migratestore%28from,sourcetype,options,with,todestinationurl,destinationtype,destinationoptions%29.md)
  Migrates the store at a given source URL to the store at a given destination URL, performing all of the mappings specified in a given mapping model.
### Getting the Manager’s Configuration
- [var destinationContext: NSManagedObjectContext](./destinationcontext.md)
  The managed object context the migration manager uses for writing the destination persistent store.
- [var destinationModel: NSManagedObjectModel](./destinationmodel.md)
  The destination model for the migration manager.
- [var sourceContext: NSManagedObjectContext](./sourcecontext.md)
  The managed object context the migration manager uses for reading the source persistent store.
- [var sourceModel: NSManagedObjectModel](./sourcemodel.md)
  The source model for the migration manager.
- [func destinationEntity(for: NSEntityMapping) -> NSEntityDescription?](./destinationentity%28for%29.md)
  Returns the entity description for the destination entity of a given entity mapping.
- [func sourceEntity(for: NSEntityMapping) -> NSEntityDescription?](./sourceentity%28for%29.md)
  Returns the entity description for the source entity of a given entity mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationmanager/mappingmodel)*