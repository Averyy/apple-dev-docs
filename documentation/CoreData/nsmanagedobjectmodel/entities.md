# entities

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The entities in the model.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var entities: [NSEntityDescription] { get set }
```

```objc
@property (strong) NSArray<NSEntityDescription *> * entities;
```

## Discussion

Entities are instances of [`NSEntityDescription`](../nsentitydescription.md).

### Special Considerations

Setting the entities for an object model raises an exception if the object model has been used by an object graph manager.

## See Also

### Managing entities and configurations
- [var entitiesByName: [String : NSEntityDescription]](./entitiesbyname.md)
  The entities of the model, keyed by name.
- [var configurations: [String]](./configurations.md)
  All the available configuration names of the model.
- [func entities(forConfigurationName: String?) -> [NSEntityDescription]?](./entities%28forconfigurationname%29.md)
  Returns the entities of the model for a specified configuration.
- [func setEntities([NSEntityDescription], forConfigurationName: String)](./setentities%28_,forconfigurationname%29.md)
  Associates the specified entities with the model using the given configuration name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/entities)*