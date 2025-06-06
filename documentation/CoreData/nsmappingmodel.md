# NSMappingModel

**Framework**: Core Data  
**Kind**: class

A model instance that specifies how to map a model from a source to a destination managed object model.

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
class NSMappingModel
```

## Topics

### Creating a Mapping
- [init?(from: [Bundle]?, forSourceModel: NSManagedObjectModel?, destinationModel: NSManagedObjectModel?)](nsmappingmodel/init(from:forsourcemodel:destinationmodel:).md)
  Returns the mapping model that will translate data from the source to the destination model.
- [class func inferredMappingModel(forSourceModel: NSManagedObjectModel, destinationModel: NSManagedObjectModel) throws -> NSMappingModel](nsmappingmodel/inferredmappingmodel(forsourcemodel:destinationmodel:).md)
  Returns a newly created mapping model that will migrate data from the source to the destination model.
- [init?(contentsOf: URL?)](nsmappingmodel/init(contentsof:).md)
  Returns a mapping model initialized from a given URL.
### Managing Entity Mappings
- [var entityMappings: [NSEntityMapping]!](nsmappingmodel/entitymappings.md)
  The entity mappings for the mapping model.
- [var entityMappingsByName: [String : NSEntityMapping]](nsmappingmodel/entitymappingsbyname.md)
  The entity mappings for the mapping model, keyed by name.

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
- [class NSEntityMapping](nsentitymapping.md)
  A mapping instance that specifies how to map an entity from a source to a destination managed object model.
- [class NSEntityMigrationPolicy](nsentitymigrationpolicy.md)
  A policy instance that customizes the migration process for an entity mapping.
- [enum NSEntityMappingType](nsentitymappingtype.md)
  The types for mapping an entity between a source model and a destination model.
- [class NSPropertyMapping](nspropertymapping.md)
  A mapping instance that specifies in a model how to map from a property in a source entity to a property in a destination entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmappingmodel)*