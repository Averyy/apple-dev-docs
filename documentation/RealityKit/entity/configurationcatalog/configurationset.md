# Entity.ConfigurationCatalog.ConfigurationSet

**Framework**: RealityKit  
**Kind**: struct

A collection of alternatives to choose from.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct ConfigurationSet
```

#### Overview

For example, a configuration set might contain configurations named `small`, `medium`, and `big` to represent a choice of sizes.

## Topics

### Accessing a configuration set’s name
- [var id: String](entity/configurationcatalog/configurationset/id.md)
  A name that identifies the configuration set.
### Accessing configurations in a configuration set
- [var configurations: [String : Entity.ConfigurationCatalog.Configuration]](entity/configurationcatalog/configurationset/configurations.md)
  The alternative configurations that are available in a set.
- [var defaultConfiguration: Entity.ConfigurationCatalog.Configuration](entity/configurationcatalog/configurationset/defaultconfiguration.md)
  The default configuration, if you don’t explicitly set one.
### Initializers
- [init(id:configurations:defaultConfigurationId:)](entity/configurationcatalog/configurationset/init(id:configurations:defaultconfigurationid:).md)
  Creates a configuration set from an ID, an array of configurations, and a default configuration ID.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Entity.ConfigurationCatalog.Configuration](entity/configurationcatalog/configuration.md)
  A type that represents an alternative that you can choose.
- [Entity.ConfigurationCatalog.ConfigurationCombination](entity/configurationcatalog/configurationcombination.md)
  A type that associates an entity with a combination of configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/configurationcatalog/configurationset)*