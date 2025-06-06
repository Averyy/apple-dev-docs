# createRelationships(forDestination:in:manager:)

**Framework**: Core Data  
**Kind**: method

Constructs the relationships between the newly-created destination instances.

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
func createRelationships(forDestination dInstance: NSManagedObject, in mapping: NSEntityMapping, manager: NSMigrationManager) throws
```

#### Discussion

You can use this stage to (re)create relationships between migrated objects—you use the association lookup methods on the [`NSMigrationManager`](nsmigrationmanager.md) instance to determine the appropriate relationship targets.

## Parameters

- `dInstance`: The destination instance for which to create relationships.
- `mapping`: The mapping object in use.
- `manager`: The migration manager performing the migration.

## See Also

- [func begin(NSEntityMapping, with: NSMigrationManager) throws](nsentitymigrationpolicy/begin(_:with:).md)
  Sets up state information before the start of a given entity mapping.
- [func createDestinationInstances(forSource: NSManagedObject, in: NSEntityMapping, manager: NSMigrationManager) throws](nsentitymigrationpolicy/createdestinationinstances(forsource:in:manager:).md)
  Creates the destination instance(s) for a given source instance.
- [func endInstanceCreation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](nsentitymigrationpolicy/endinstancecreation(formapping:manager:).md)
  Indicates the end of the instance creation stage for the specified entity mapping, and the precursor to the next migration stage.
- [func endRelationshipCreation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](nsentitymigrationpolicy/endrelationshipcreation(formapping:manager:).md)
  Indicates the end of the relationship creation stage for the specified entity mapping.
- [func performCustomValidation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](nsentitymigrationpolicy/performcustomvalidation(formapping:manager:).md)
  Provides the option to perform custom validation on migrated objects during the validation stage of the entity migration policy.
- [func end(NSEntityMapping, manager: NSMigrationManager) throws](nsentitymigrationpolicy/end(_:manager:).md)
  Performs cleanup at the end of the migration, from any phase of the mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy/createrelationships(fordestination:in:manager:))*