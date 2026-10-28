# NSEntityMigrationPolicy

**Framework**: Core Data  
**Kind**: class  
**Role**: Class

A policy instance that customizes the migration process for an entity mapping.

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
class NSEntityMigrationPolicy
```

```objc
@interface NSEntityMigrationPolicy : NSObject
```

## Overview

You set the policy for an entity mapping by passing the name of the migration policy class as the argument to [`entityMigrationPolicyClassName`](./nsentitymapping/entitymigrationpolicyclassname.md). Typically, you specify the name in the Xcode mapping model editor.

## Topics

### Customizing Stages of the Mapping Life Cycle
- [func begin(NSEntityMapping, with: NSMigrationManager) throws](./nsentitymigrationpolicy/begin%28_,with%29.md)
  Sets up state information before the start of a given entity mapping.
- [func createDestinationInstances(forSource: NSManagedObject, in: NSEntityMapping, manager: NSMigrationManager) throws](./nsentitymigrationpolicy/createdestinationinstances%28forsource,in,manager%29.md)
  Creates the destination instance(s) for a given source instance.
- [func endInstanceCreation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](./nsentitymigrationpolicy/endinstancecreation%28formapping,manager%29.md)
  Indicates the end of the instance creation stage for the specified entity mapping, and the precursor to the next migration stage.
- [func createRelationships(forDestination: NSManagedObject, in: NSEntityMapping, manager: NSMigrationManager) throws](./nsentitymigrationpolicy/createrelationships%28fordestination,in,manager%29.md)
  Constructs the relationships between the newly-created destination instances.
- [func endRelationshipCreation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](./nsentitymigrationpolicy/endrelationshipcreation%28formapping,manager%29.md)
  Indicates the end of the relationship creation stage for the specified entity mapping.
- [func performCustomValidation(forMapping: NSEntityMapping, manager: NSMigrationManager) throws](./nsentitymigrationpolicy/performcustomvalidation%28formapping,manager%29.md)
  Provides the option to perform custom validation on migrated objects during the validation stage of the entity migration policy.
- [func end(NSEntityMapping, manager: NSMigrationManager) throws](./nsentitymigrationpolicy/end%28_,manager%29.md)
  Performs cleanup at the end of the migration, from any phase of the mapping.
### Constants
- [let NSMigrationManagerKey: String](./nsmigrationmanagerkey.md)
  Key for the migration manager.
- [let NSMigrationSourceObjectKey: String](./nsmigrationsourceobjectkey.md)
  Key for the source object.
- [let NSMigrationDestinationObjectKey: String](./nsmigrationdestinationobjectkey.md)
  Key for the destination object.
- [let NSMigrationEntityMappingKey: String](./nsmigrationentitymappingkey.md)
  Key for the entity mapping object.
- [let NSMigrationPropertyMappingKey: String](./nsmigrationpropertymappingkey.md)
  Key for the property mapping object.
- [let NSMigrationEntityPolicyKey: String](./nsmigrationentitypolicykey.md)
  Key for the entity migration policy object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Entity Mapping
- [class NSMigrationManager](./nsmigrationmanager.md)
  A migration manager instance that performs a migration of data from one persistent store to another using a given mapping model.
- [class NSMappingModel](./nsmappingmodel.md)
  A model instance that specifies how to map a model from a source to a destination managed object model.
- [class NSEntityMapping](./nsentitymapping.md)
  A mapping instance that specifies how to map an entity from a source to a destination managed object model.
- [enum NSEntityMappingType](./nsentitymappingtype.md)
  The types for mapping an entity between a source model and a destination model.
- [class NSPropertyMapping](./nspropertymapping.md)
  A mapping instance that specifies in a model how to map from a property in a source entity to a property in a destination entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymigrationpolicy)*