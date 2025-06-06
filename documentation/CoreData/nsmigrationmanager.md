# NSMigrationManager

**Framework**: Core Data  
**Kind**: class

A migration manager instance that performs a migration of data from one persistent store to another using a given mapping model.

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
class NSMigrationManager
```

## Topics

### Creating a Migration Manager
- [init(sourceModel: NSManagedObjectModel, destinationModel: NSManagedObjectModel)](nsmigrationmanager/init(sourcemodel:destinationmodel:).md)
  Initializes a migration manager instance with given source and destination models.
### Getting the Manager’s Configuration
- [var destinationContext: NSManagedObjectContext](nsmigrationmanager/destinationcontext.md)
  The managed object context the migration manager uses for writing the destination persistent store.
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
### Customizing the Manager
- [var userInfo: [AnyHashable : Any]?](nsmigrationmanager/userinfo.md)
  The user info for the migration manager.
- [var usesStoreSpecificMigrationManager: Bool](nsmigrationmanager/usesstorespecificmigrationmanager.md)
  A Boolean value that indicates whether the migration manager tries to use a store specific migration manager to perform the  migration.
### Managing Sources and Destinations
- [func associate(sourceInstance: NSManagedObject, withDestinationInstance: NSManagedObject, for: NSEntityMapping)](nsmigrationmanager/associate(sourceinstance:withdestinationinstance:for:).md)
  Associates a given source managed object instance with an array of destination instances for a given property mapping.
- [func destinationInstances(forEntityMappingName: String, sourceInstances: [NSManagedObject]?) -> [NSManagedObject]](nsmigrationmanager/destinationinstances(forentitymappingname:sourceinstances:).md)
  Returns the managed object instances created in the destination store for the named entity mapping for the given array of source instances.
- [func sourceInstances(forEntityMappingName: String, destinationInstances: [NSManagedObject]?) -> [NSManagedObject]](nsmigrationmanager/sourceinstances(forentitymappingname:destinationinstances:).md)
  Returns the managed object instances in the source store used to create the given destination instances for the passed in property mapping.
### Performing a Migration
- [func migrateStore(from: URL, type: NSPersistentStore.StoreType, options: [AnyHashable : Any]?, mapping: NSMappingModel, to: URL, type: NSPersistentStore.StoreType, options: [AnyHashable : Any]?) throws](nsmigrationmanager/migratestore(from:type:options:mapping:to:type:options:).md)
  Migrates the source store to the destination using the specified mapping model.
- [func migrateStore(from: URL, sourceType: String, options: [AnyHashable : Any]?, with: NSMappingModel?, toDestinationURL: URL, destinationType: String, destinationOptions: [AnyHashable : Any]?) throws](nsmigrationmanager/migratestore(from:sourcetype:options:with:todestinationurl:destinationtype:destinationoptions:).md)
  Migrates the store at a given source URL to the store at a given destination URL, performing all of the mappings specified in a given mapping model.
### Monitoring a Migration’s Progress
- [var migrationProgress: Float](nsmigrationmanager/migrationprogress.md)
  A number between `0` and `1` that indicates the proportion of completeness of the migration.
- [var currentEntityMapping: NSEntityMapping](nsmigrationmanager/currententitymapping.md)
  The entity mapping currently being processed.
### Aborting a Migration
- [func cancelMigrationWithError(any Error)](nsmigrationmanager/cancelmigrationwitherror(_:).md)
  Cancels the migration with a given error.
- [func reset()](nsmigrationmanager/reset.md)
  Resets the association tables for the migration.
### Deprecated
- [Deprecated Symbols](nsmigrationmanager-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

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

- [class NSMappingModel](nsmappingmodel.md)
  A model instance that specifies how to map a model from a source to a destination managed object model.
- [class NSEntityMapping](nsentitymapping.md)
  A mapping instance that specifies how to map an entity from a source to a destination managed object model.
- [class NSEntityMigrationPolicy](nsentitymigrationpolicy.md)
  A policy instance that customizes the migration process for an entity mapping.
- [enum NSEntityMappingType](nsentitymappingtype.md)
  The types for mapping an entity between a source model and a destination model.
- [class NSPropertyMapping](nspropertymapping.md)
  A mapping instance that specifies in a model how to map from a property in a source entity to a property in a destination entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmigrationmanager)*