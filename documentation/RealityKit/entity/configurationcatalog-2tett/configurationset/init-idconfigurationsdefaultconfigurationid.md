# init(id:configurations:defaultConfigurationId:)

**Framework**: RealityKit  
**Kind**: init

Creates a configuration set from an ID, an array of configurations, and a default configuration ID.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(id: String, configurations: [Entity.ConfigurationCatalog.Configuration], defaultConfigurationId: String? = nil) throws
```

#### Return Value

A configuration set containing the configurations.

## Parameters

- `id`: The ID of the configuration set that’s unique across all other configuration sets.
- `configurations`: An array of configurations you can choose from.   The configuration set stores the array in the    property and doesn’t preserve the order of the array.
- `defaultConfigurationId`: The ID of one of the configuration elements in the    parameter, which is the default configuration the entity initializer   applies if you don’t choose a configuration from the set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/configurationcatalog-2tett/configurationset/init(id:configurations:defaultconfigurationid:))*