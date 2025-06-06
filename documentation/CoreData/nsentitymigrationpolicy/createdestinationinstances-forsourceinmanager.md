# createDestinationInstances(forSource:in:manager:)

**Framework**: Core Data  
**Kind**: method

Creates the destination instance(s) for a given source instance.

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
func createDestinationInstances(forSource sInstance: NSManagedObject, in mapping: NSEntityMapping, manager: NSMigrationManager) throws
```

#### Discussion

This method is invoked by the migration manager on each source instance (as specified by the [`sourceExpression`](nsentitymapping/sourceexpression.md) in the mapping) to create the corresponding destination instance(s). It also associates the source and destination instances by calling `NSMigrationManager`’s [`associate(sourceInstance:withDestinationInstance:for:)`](nsmigrationmanager/associate(sourceinstance:withdestinationinstance:for:).md) method.

##### Special Considerations

If you override this method and do not invoke `super`, you must invoke `NSMigrationManager`’s [`associate(sourceInstance:withDestinationInstance:for:)`](nsmigrationmanager/associate(sourceinstance:withdestinationinstance:for:).md) to associate the source and destination instances as required. .

## Parameters

- `sInstance`: The source instance for which to create destination instances.
- `mapping`: The mapping object in use.
- `manager`: The migration manager performing the migration.

## See Also

- [func begin(NSEntityMapping, with: NSMigrationManager) throws](nsentitymigrationpolicy/begin(_:with:).md)
  Sets up state information before the start of a given entity mapping.
- [func endInstanceCreation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](nsentitymigrationpolicy/endinstancecreation(formapping:manager:).md)
  Indicates the end of the instance creation stage for the specified entity mapping, and the precursor to the next migration stage.
- [func createRelationships(forDestination: NSManagedObject, in: NSEntityMapping, manager: NSMigrationManager) throws](nsentitymigrationpolicy/createrelationships(fordestination:in:manager:).md)
  Constructs the relationships between the newly-created destination instances.
- [func endRelationshipCreation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](nsentitymigrationpolicy/endrelationshipcreation(formapping:manager:).md)
  Indicates the end of the relationship creation stage for the specified entity mapping.
- [func performCustomValidation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](nsentitymigrationpolicy/performcustomvalidation(formapping:manager:).md)
  Provides the option to perform custom validation on migrated objects during the validation stage of the entity migration policy.
- [func end(NSEntityMapping, manager: NSMigrationManager) throws](nsentitymigrationpolicy/end(_:manager:).md)
  Performs cleanup at the end of the migration, from any phase of the mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/createdestinationinstances(forsource:in:manager:))*