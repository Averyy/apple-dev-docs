# Entity.ConfigurationCatalog.ConfigurationSet

**Framework**: RealityKit  
**Kind**: struct

A collection of alternatives to choose from.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct ConfigurationSet
```

#### Overview

For example, a configuration set might contain configurations named `small`, `medium`, and `big` to represent a choice of sizes.

## Topics

### Initializers
- [init(id:configurations:defaultConfigurationId:)](entity/configurationcatalog-2tett/configurationset/init(id:configurations:defaultconfigurationid:).md)
  Creates a configuration set from an ID, an array of configurations, and a default configuration ID.
### Instance Properties
- [var configurations: [String : Entity.ConfigurationCatalog.Configuration]](entity/configurationcatalog-1b69q/configurationset/configurations.md)
  The alternative configurations that are available in a set.
- [var defaultConfiguration: Entity.ConfigurationCatalog.Configuration](entity/configurationcatalog-1b69q/configurationset/defaultconfiguration.md)
  The default configuration, if you don’t explicitly set one.
- [var id: String](entity/configurationcatalog-1b69q/configurationset/id.md)
  A name that identifies the configuration set.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/configurationcatalog-1b69q/configurationset)*