# Entity.ConfigurationCatalog.ConfigurationSet

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

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

## Overview

For example, a configuration set might contain configurations named `small`, `medium`, and `big` to represent a choice of sizes.

## Topics

### Creating a configuration set
- [init(id: String, configurations: [Entity.ConfigurationCatalog.Configuration], defaultConfigurationId: String?) throws](./configurationset/init%28id,configurations,defaultconfigurationid%29-5erwz.md)
  Creates a configuration set from an ID, an array of configurations, and a default configuration ID.
- [init(id: String, configurations: [Entity.ConfigurationCatalog.Configuration], defaultConfigurationId: String?) throws](./configurationset/init%28id,configurations,defaultconfigurationid%29-5erwz.md)
  Creates a configuration set from an ID, an array of configurations, and a default configuration ID.
### Accessing a configuration set’s name
- [var id: String](./configurationset/id.md)
  A name that identifies the configuration set.
### Accessing configurations in a configuration set
- [var configurations: [String : Entity.ConfigurationCatalog.Configuration]](./configurationset/configurations.md)
  The alternative configurations that are available in a set.
- [var defaultConfiguration: Entity.ConfigurationCatalog.Configuration](./configurationset/defaultconfiguration.md)
  The default configuration, if you don’t explicitly set one.
### Initializers
- [init(id:configurations:defaultConfigurationId:)](./configurationset/init%28id,configurations,defaultconfigurationid%29.md)
  Creates a configuration set from an ID, an array of configurations, and a default configuration ID.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Identifiable](../../../Swift/identifiable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Defining configuration choices
- [Entity.ConfigurationCatalog.Configuration](./configuration.md)
  A type that represents an alternative that you can choose.
- [Entity.ConfigurationCatalog.ConfigurationCombination](./configurationcombination.md)
  A type that associates an entity with a combination of configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/configurationcatalog/configurationset)*