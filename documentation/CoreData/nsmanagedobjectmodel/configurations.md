# configurations

**Framework**: Core Data  
**Kind**: property

All the available configuration names of the model.

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
var configurations: [String] { get }
```

## See Also

- [var entities: [NSEntityDescription]](nsmanagedobjectmodel/entities.md)
  The entities in the model.
- [var entitiesByName: [String : NSEntityDescription]](nsmanagedobjectmodel/entitiesbyname.md)
  The entities of the model, keyed by name.
- [func entities(forConfigurationName: String?) -> [NSEntityDescription]?](nsmanagedobjectmodel/entities(forconfigurationname:).md)
  Returns the entities of the model for a specified configuration.
- [func setEntities([NSEntityDescription], forConfigurationName: String)](nsmanagedobjectmodel/setentities(_:forconfigurationname:).md)
  Associates the specified entities with the model using the given configuration name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/configurations)*