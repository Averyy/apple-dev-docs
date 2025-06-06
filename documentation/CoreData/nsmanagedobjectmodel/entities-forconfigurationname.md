# entities(forConfigurationName:)

**Framework**: Core Data  
**Kind**: method

Returns the entities of the model for a specified configuration.

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
func entities(forConfigurationName configuration: String?) -> [NSEntityDescription]?
```

#### Return Value

An array containing the entities of the receiver for the configuration specified by `configuration`.

## Parameters

- `configuration`: The name of a configuration in the receiver.

## See Also

- [var entities: [NSEntityDescription]](nsmanagedobjectmodel/entities.md)
  The entities in the model.
- [var entitiesByName: [String : NSEntityDescription]](nsmanagedobjectmodel/entitiesbyname.md)
  The entities of the model, keyed by name.
- [var configurations: [String]](nsmanagedobjectmodel/configurations.md)
  All the available configuration names of the model.
- [func setEntities([NSEntityDescription], forConfigurationName: String)](nsmanagedobjectmodel/setentities(_:forconfigurationname:).md)
  Associates the specified entities with the model using the given configuration name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/entities(forconfigurationname:))*