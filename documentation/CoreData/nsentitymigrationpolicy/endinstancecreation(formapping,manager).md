# endInstanceCreation(forMapping:manager:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Indicates the end of the instance creation stage for the specified entity mapping, and the precursor to the next migration stage.

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
func endInstanceCreation(forMapping mapping: NSEntityMapping, manager: NSMigrationManager) throws
```

```objc
- (BOOL) endInstanceCreationForEntityMapping:(NSEntityMapping *) mapping manager:(NSMigrationManager *) manager error:(NSError **) error;
```

## Discussion

You can override this method to clean up state from the creation of destination or to prepare state for the creation of relationships.

## Parameters

- `mapping`: The mapping object in use.
- `manager`: The migration manager performing the migration.

## See Also

### Customizing Stages of the Mapping Life Cycle
- [func begin(NSEntityMapping, with: NSMigrationManager) throws](./begin%28_,with%29.md)
  Sets up state information before the start of a given entity mapping.
- [func createDestinationInstances(forSource: NSManagedObject, in: NSEntityMapping, manager: NSMigrationManager) throws](./createdestinationinstances%28forsource,in,manager%29.md)
  Creates the destination instance(s) for a given source instance.
- [func createRelationships(forDestination: NSManagedObject, in: NSEntityMapping, manager: NSMigrationManager) throws](./createrelationships%28fordestination,in,manager%29.md)
  Constructs the relationships between the newly-created destination instances.
- [func endRelationshipCreation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](./endrelationshipcreation%28formapping,manager%29.md)
  Indicates the end of the relationship creation stage for the specified entity mapping.
- [func performCustomValidation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](./performcustomvalidation%28formapping,manager%29.md)
  Provides the option to perform custom validation on migrated objects during the validation stage of the entity migration policy.
- [func end(NSEntityMapping, manager: NSMigrationManager) throws](./end%28_,manager%29.md)
  Performs cleanup at the end of the migration, from any phase of the mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/endinstancecreation(formapping:manager:))*