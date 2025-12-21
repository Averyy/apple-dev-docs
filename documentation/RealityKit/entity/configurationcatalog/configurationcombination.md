# Entity.ConfigurationCatalog.ConfigurationCombination

**Framework**: RealityKit  
**Kind**: struct

A type that associates an entity with a combination of configurations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct ConfigurationCombination
```

## Topics

### Creating a configuration combination
- [init(entity: Entity, configurationSpecifications: [String : String])](entity/configurationcatalog/configurationcombination/init(entity:configurationspecifications:).md)
  Creates a configuration combination from an entity and a configuration dictionary.
### Accessing values
- [let entity: Entity](entity/configurationcatalog/configurationcombination/entity.md)
  The entity that represents the configuration choices.
- [let configurationSpecifications: [String : String]](entity/configurationcatalog/configurationcombination/configurationspecifications.md)
  A dictionary that associates IDs of configuration sets to IDs of configurations.

## See Also

- [Entity.ConfigurationCatalog.Configuration](entity/configurationcatalog/configuration.md)
  A type that represents an alternative that you can choose.
- [Entity.ConfigurationCatalog.ConfigurationSet](entity/configurationcatalog/configurationset.md)
  A collection of alternatives to choose from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/configurationcatalog/configurationcombination)*