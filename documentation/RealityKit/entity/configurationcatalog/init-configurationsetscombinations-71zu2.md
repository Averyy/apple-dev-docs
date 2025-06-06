# init(configurationSets:combinations:)

**Framework**: RealityKit  
**Kind**: init

Creates a configuration catalog from in-memory entities and an array of configuration sets.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(configurationSets: [Entity.ConfigurationCatalog.ConfigurationSet], combinations: [Entity.ConfigurationCatalog.ConfigurationCombination]) throws
```

#### Return Value

A configuration catalog that maintains the provided entities in memory.

## Parameters

- `configurationSets`: The configuration choices that the configuration catalog presents.   Each configuration set needs to have a unique ID from all others.   The configuration catalog stores the array as the   dictionary   property and doesn’t preserve its order.
- `combinations`: The combinations of in-memory entities and the configurations that can   address them.   The keys you use in    need to match   IDs of configuration sets from the   argument.   The values you use in    need to match   IDs of configurations from the   argument.   There needs to be one   for each possible combination   of configurations.

## See Also

- [init(configurationSets: [String : Entity.ConfigurationCatalog.ConfigurationSet], combinations: [Entity.ConfigurationCatalog.ConfigurationCombination]) throws](entity/configurationcatalog/init(configurationsets:combinations:)-598zl.md)
  Creates a configuration catalog from in-memory entities and a dictionary of configuration sets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/configurationcatalog/init(configurationsets:combinations:)-71zu2)*