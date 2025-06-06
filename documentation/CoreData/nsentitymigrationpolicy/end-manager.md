# end(_:manager:)

**Framework**: Core Data  
**Kind**: method

Performs cleanup at the end of the migration, from any phase of the mapping.

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
func end(_ mapping: NSEntityMapping, manager: NSMigrationManager) throws
```

#### Discussion

This is the end to the given entity mapping. You can implement this method to perform any clean-up at the end of the migration (from any of the three phases of the mapping).

## Parameters

- `mapping`: The mapping object in use.
- `manager`: The migration manager performing the migration.

## See Also

- [func begin(NSEntityMapping, with: NSMigrationManager) throws](nsentitymigrationpolicy/begin(_:with:).md)
  Sets up state information before the start of a given entity mapping.
- [func createDestinationInstances(forSource: NSManagedObject, in: NSEntityMapping, manager: NSMigrationManager) throws](nsentitymigrationpolicy/createdestinationinstances(forsource:in:manager:).md)
  Creates the destination instance(s) for a given source instance.
- [func endInstanceCreation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](nsentitymigrationpolicy/endinstancecreation(formapping:manager:).md)
  Indicates the end of the instance creation stage for the specified entity mapping, and the precursor to the next migration stage.
- [func createRelationships(forDestination: NSManagedObject, in: NSEntityMapping, manager: NSMigrationManager) throws](nsentitymigrationpolicy/createrelationships(fordestination:in:manager:).md)
  Constructs the relationships between the newly-created destination instances.
- [func endRelationshipCreation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](nsentitymigrationpolicy/endrelationshipcreation(formapping:manager:).md)
  Indicates the end of the relationship creation stage for the specified entity mapping.
- [func performCustomValidation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](nsentitymigrationpolicy/performcustomvalidation(formapping:manager:).md)
  Provides the option to perform custom validation on migrated objects during the validation stage of the entity migration policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/end(_:manager:))*