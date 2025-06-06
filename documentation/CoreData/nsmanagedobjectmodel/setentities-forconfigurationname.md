# setEntities(_:forConfigurationName:)

**Framework**: Core Data  
**Kind**: method

Associates the specified entities with the model using the given configuration name.

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
func setEntities(_ entities: [NSEntityDescription], forConfigurationName configuration: String)
```

#### Discussion

This method raises an exception if the receiver has been used by an object graph manager.

## Parameters

- `entities`: An array of instances of  .
- `configuration`: A name for the configuration.

## See Also

- [var entities: [NSEntityDescription]](nsmanagedobjectmodel/entities.md)
  The entities in the model.
- [var entitiesByName: [String : NSEntityDescription]](nsmanagedobjectmodel/entitiesbyname.md)
  The entities of the model, keyed by name.
- [var configurations: [String]](nsmanagedobjectmodel/configurations.md)
  All the available configuration names of the model.
- [func entities(forConfigurationName: String?) -> [NSEntityDescription]?](nsmanagedobjectmodel/entities(forconfigurationname:).md)
  Returns the entities of the model for a specified configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/setentities(_:forconfigurationname:))*