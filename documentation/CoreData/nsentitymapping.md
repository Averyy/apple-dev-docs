# NSEntityMapping

**Framework**: Core Data  
**Kind**: class

A mapping instance that specifies how to map an entity from a source to a destination managed object model.

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
class NSEntityMapping
```

## Topics

### Managing Source Information
- [var sourceEntityName: String?](nsentitymapping/sourceentityname.md)
  The source entity name for the entity mapping.
- [var sourceEntityVersionHash: Data?](nsentitymapping/sourceentityversionhash.md)
  The version hash of the source entity for the entity mapping.
- [var sourceExpression: NSExpression?](nsentitymapping/sourceexpression.md)
  The source expression for the entity mapping.
### Managing Destination Information
- [var destinationEntityName: String?](nsentitymapping/destinationentityname.md)
  The destination entity name for the entity mapping.
- [var destinationEntityVersionHash: Data?](nsentitymapping/destinationentityversionhash.md)
  The version hash for the destination entity for the entity mapping.
### Managing Mapping Information
- [var name: String!](nsentitymapping/name.md)
  The name of the entity mapping.
- [var mappingType: NSEntityMappingType](nsentitymapping/mappingtype.md)
  The mapping type for the entity mapping.
- [var entityMigrationPolicyClassName: String?](nsentitymapping/entitymigrationpolicyclassname.md)
  The class name of the migration policy for the entity mapping.
- [var attributeMappings: [NSPropertyMapping]?](nsentitymapping/attributemappings.md)
  The array of attribute mappings for the entity mapping.
- [var relationshipMappings: [NSPropertyMapping]?](nsentitymapping/relationshipmappings.md)
  The array of relationship mappings for the entity mapping.
- [var userInfo: [AnyHashable : Any]?](nsentitymapping/userinfo.md)
  The user info dictionary for the entity mapping.
### Constants
- [NSEntityMappingType.undefinedEntityMappingType](nsentitymappingtype/undefinedentitymappingtype.md)
  Specifies that the developer handles destination instance creation.
- [NSEntityMappingType.customEntityMappingType](nsentitymappingtype/customentitymappingtype.md)
  Specifies a custom mapping.
- [NSEntityMappingType.addEntityMappingType](nsentitymappingtype/addentitymappingtype.md)
  Specifies that this is a new entity in the destination model.
- [NSEntityMappingType.removeEntityMappingType](nsentitymappingtype/removeentitymappingtype.md)
  Specifies that this entity is not present in the destination model.
- [NSEntityMappingType.copyEntityMappingType](nsentitymappingtype/copyentitymappingtype.md)
  Specifies that source instances are migrated as-is.
- [NSEntityMappingType.transformEntityMappingType](nsentitymappingtype/transformentitymappingtype.md)
  Specifies that entity exists in source and destination and is mapped.

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

- [class NSMigrationManager](nsmigrationmanager.md)
  A migration manager instance that performs a migration of data from one persistent store to another using a given mapping model.
- [class NSMappingModel](nsmappingmodel.md)
  A model instance that specifies how to map a model from a source to a destination managed object model.
- [class NSEntityMigrationPolicy](nsentitymigrationpolicy.md)
  A policy instance that customizes the migration process for an entity mapping.
- [enum NSEntityMappingType](nsentitymappingtype.md)
  The types for mapping an entity between a source model and a destination model.
- [class NSPropertyMapping](nspropertymapping.md)
  A mapping instance that specifies in a model how to map from a property in a source entity to a property in a destination entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymapping)*