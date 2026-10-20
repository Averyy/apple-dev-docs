# configurations

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

All the available configuration names of the model.

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
var configurations: [String] { get }
```

```objc
@property (strong, readonly) NSArray<NSString *> * configurations;
```

## See Also

### Managing entities and configurations
- [var entities: [NSEntityDescription]](./entities.md)
  The entities in the model.
- [var entitiesByName: [String : NSEntityDescription]](./entitiesbyname.md)
  The entities of the model, keyed by name.
- [func entities(forConfigurationName: String?) -> [NSEntityDescription]?](./entities%28forconfigurationname%29.md)
  Returns the entities of the model for a specified configuration.
- [func setEntities([NSEntityDescription], forConfigurationName: String)](./setentities%28_,forconfigurationname%29.md)
  Associates the specified entities with the model using the given configuration name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/configurations)*