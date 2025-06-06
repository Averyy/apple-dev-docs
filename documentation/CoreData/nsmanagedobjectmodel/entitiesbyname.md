# entitiesByName

**Framework**: Core Data  
**Kind**: property

The entities of the model, keyed by name.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var entitiesByName: [String : NSEntityDescription] { get }
```

#### Discussion

Entities are instances of [`NSEntityDescription`](nsentitydescription.md).

## See Also

- [class func entity(forEntityName: String, in: NSManagedObjectContext) -> NSEntityDescription?](nsentitydescription/entity(forentityname:in:).md)
  Returns the entity with the specified name from the managed object model associated with the specified managed object context’s persistent store coordinator.
- [var entities: [NSEntityDescription]](nsmanagedobjectmodel/entities.md)
  The entities in the model.
- [var configurations: [String]](nsmanagedobjectmodel/configurations.md)
  All the available configuration names of the model.
- [func entities(forConfigurationName: String?) -> [NSEntityDescription]?](nsmanagedobjectmodel/entities(forconfigurationname:).md)
  Returns the entities of the model for a specified configuration.
- [func setEntities([NSEntityDescription], forConfigurationName: String)](nsmanagedobjectmodel/setentities(_:forconfigurationname:).md)
  Associates the specified entities with the model using the given configuration name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/entitiesbyname)*