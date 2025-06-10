# NSEntityMappingType

**Framework**: Core Data  
**Kind**: enum

The types for mapping an entity between a source model and a destination model.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum NSEntityMappingType
```

## Topics

### Enumeration Cases
- [NSEntityMappingType.addEntityMappingType](nsentitymappingtype/addentitymappingtype.md)
  Specifies that this is a new entity in the destination model.
- [NSEntityMappingType.copyEntityMappingType](nsentitymappingtype/copyentitymappingtype.md)
  Specifies that source instances are migrated as-is.
- [NSEntityMappingType.customEntityMappingType](nsentitymappingtype/customentitymappingtype.md)
  Specifies a custom mapping.
- [NSEntityMappingType.removeEntityMappingType](nsentitymappingtype/removeentitymappingtype.md)
  Specifies that this entity is not present in the destination model.
- [NSEntityMappingType.transformEntityMappingType](nsentitymappingtype/transformentitymappingtype.md)
  Specifies that entity exists in source and destination and is mapped.
- [NSEntityMappingType.undefinedEntityMappingType](nsentitymappingtype/undefinedentitymappingtype.md)
  Specifies that the developer handles destination instance creation.
### Initializers
- [init?(rawValue: UInt)](nsentitymappingtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSMigrationManager](nsmigrationmanager.md)
  A migration manager instance that performs a migration of data from one persistent store to another using a given mapping model.
- [class NSMappingModel](nsmappingmodel.md)
  A model instance that specifies how to map a model from a source to a destination managed object model.
- [class NSEntityMapping](nsentitymapping.md)
  A mapping instance that specifies how to map an entity from a source to a destination managed object model.
- [class NSEntityMigrationPolicy](nsentitymigrationpolicy.md)
  A policy instance that customizes the migration process for an entity mapping.
- [class NSPropertyMapping](nspropertymapping.md)
  A mapping instance that specifies in a model how to map from a property in a source entity to a property in a destination entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymappingtype)*