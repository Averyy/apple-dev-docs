# configurations

**Framework**: RealityKit  
**Kind**: property

The alternative configurations that are available in a set.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var configurations: [String : Entity.ConfigurationCatalog.Configuration] { get }
```

#### Discussion

The keys are configuration IDs, and the values are the corresponding configurations.

## See Also

- [var defaultConfiguration: Entity.ConfigurationCatalog.Configuration](entity/configurationcatalog/configurationset/defaultconfiguration.md)
  The default configuration, if you don’t explicitly set one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/configurationcatalog/configurationset/configurations)*