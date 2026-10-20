# endRelationshipCreation(forMapping:manager:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Indicates the end of the relationship creation stage for the specified entity mapping.

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
func endRelationshipCreation(forMapping mapping: NSEntityMapping, manager: NSMigrationManager) throws
```

```objc
- (BOOL) endRelationshipCreationForEntityMapping:(NSEntityMapping *) mapping manager:(NSMigrationManager *) manager error:(NSError **) error;
```

#### Discussion

This method is invoked after [`createRelationships(forDestination:in:manager:)`](./createrelationships%28fordestination,in,manager%29.md); you can override it to clean up state from the creation of relationships, or prepare state for custom validation in [`performCustomValidation(forMapping:manager:)`](./performcustomvalidation%28formapping,manager%29.md).

## Parameters

- `mapping`: The mapping object in use.
- `manager`: The migration manager performing the migration.

## See Also

### Customizing Stages of the Mapping Life Cycle
- [func begin(NSEntityMapping, with: NSMigrationManager) throws](./begin%28_,with%29.md)
  Sets up state information before the start of a given entity mapping.
- [func createDestinationInstances(forSource: NSManagedObject, in: NSEntityMapping, manager: NSMigrationManager) throws](./createdestinationinstances%28forsource,in,manager%29.md)
  Creates the destination instance(s) for a given source instance.
- [func endInstanceCreation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](./endinstancecreation%28formapping,manager%29.md)
  Indicates the end of the instance creation stage for the specified entity mapping, and the precursor to the next migration stage.
- [func createRelationships(forDestination: NSManagedObject, in: NSEntityMapping, manager: NSMigrationManager) throws](./createrelationships%28fordestination,in,manager%29.md)
  Constructs the relationships between the newly-created destination instances.
- [func performCustomValidation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](./performcustomvalidation%28formapping,manager%29.md)
  Provides the option to perform custom validation on migrated objects during the validation stage of the entity migration policy.
- [func end(NSEntityMapping, manager: NSMigrationManager) throws](./end%28_,manager%29.md)
  Performs cleanup at the end of the migration, from any phase of the mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/endrelationshipcreation(formapping:manager:))*