# init(configurationSets:combinations:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a configuration catalog from in-memory entities and a dictionary of configuration sets.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
init(configurationSets: [String : Entity.ConfigurationCatalog.ConfigurationSet], combinations: [Entity.ConfigurationCatalog.ConfigurationCombination]) throws
```

**Other overloads**:

```swift
init(configurationSets: [Entity.ConfigurationCatalog.ConfigurationSet], combinations: [Entity.ConfigurationCatalog.ConfigurationCombination]) throws
```

## Return Value

A configuration catalog that maintains the provided entities in memory.

## Parameters

- `configurationSets`: The configuration choices that the configuration catalog presents. Each key needs to match the ID of the configuration set value it maps to.
- `combinations`: The combinations of in-memory entities and configurations that can address them. The keys you use in [`configurationSpecifications`](./configurationcombination/configurationspecifications.md) need to match IDs of configuration sets from the `configurationSets` argument. The values you use in [`configurationSpecifications`](./configurationcombination/configurationspecifications.md) need to match IDs of configurations from the `configurationSets` argument. There needs to be one [`Entity.ConfigurationCatalog.ConfigurationCombination`](./configurationcombination.md) for each possible combination of configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/configurationcatalog/init(configurationsets:combinations:)-6fyur)*