# NSPropertyMapping

**Framework**: Core Data  
**Kind**: class  
**Role**: Class

A mapping instance that specifies in a model how to map from a property in a source entity to a property in a destination entity.

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
class NSPropertyMapping
```

```objc
@interface NSPropertyMapping : NSObject
```

## Topics

### Managing Mapping Attributes
- [var name: String?](./nspropertymapping/name.md)
  The name of the property in the destination entity for the property mapping.
- [var valueExpression: NSExpression?](./nspropertymapping/valueexpression.md)
  The value expression for the property mapping.
- [var userInfo: [AnyHashable : Any]?](./nspropertymapping/userinfo.md)
  The user info for the property mapping.

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
- [class NSEntityMigrationPolicy](./nsentitymigrationpolicy.md)
  A policy instance that customizes the migration process for an entity mapping.
- [enum NSEntityMappingType](./nsentitymappingtype.md)
  The types for mapping an entity between a source model and a destination model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspropertymapping)*