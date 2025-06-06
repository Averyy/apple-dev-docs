# Entity.ConfigurationCatalog.ConfigurationSet

**Framework**: RealityKit  
**Kind**: struct

A collection of alternatives to choose from.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct ConfigurationSet
```

#### Overview

For example, a configuration set might contain configurations named `small`, `medium`, and `big` to represent a choice of sizes.

## Topics

### Creating a configuration set
- [init(id: String, configurations: [Entity.ConfigurationCatalog.Configuration], defaultConfigurationId: String?) throws](entity/configurationcatalog/configurationset/init(id:configurations:defaultconfigurationid:)-8zsfr.md)
  Creates a configuration set from an ID, an array of configurations, and a default configuration ID.
- [init(id: String, configurations: [String : Entity.ConfigurationCatalog.Configuration], defaultConfigurationId: String?) throws](entity/configurationcatalog/configurationset/init(id:configurations:defaultconfigurationid:)-3nxhi.md)
  Creates a configuration set from an ID, a dictionary of configurations, and a default configuration ID.
### Accessing a configuration set’s name
- [var id: String](entity/configurationcatalog/configurationset/id-swift.property.md)
  A name that identifies the configuration set.
### Accessing configurations in a configuration set
- [var configurations: [String : Entity.ConfigurationCatalog.Configuration]](entity/configurationcatalog/configurationset/configurations.md)
  The alternative configurations that are available in a set.
- [var defaultConfiguration: Entity.ConfigurationCatalog.Configuration](entity/configurationcatalog/configurationset/defaultconfiguration.md)
  The default configuration, if you don’t explicitly set one.
### Type Aliases
- [Entity.ConfigurationCatalog.ConfigurationSet.ID](entity/configurationcatalog/configurationset/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Entity.ConfigurationCatalog.Configuration](entity/configurationcatalog/configuration.md)
  A type that represents an alternative that you can choose.
- [Entity.ConfigurationCatalog.ConfigurationCombination](entity/configurationcatalog/configurationcombination.md)
  A type that associates an entity with a combination of configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/configurationcatalog/configurationset)*