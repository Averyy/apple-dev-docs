# Entity.ConfigurationCatalog

**Framework**: RealityKit  
**Kind**: struct

A collection of alternative representations of an entity you can choose from.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct ConfigurationCatalog
```

#### Overview

A configuration catalog allows you to create an entity from alternative configurations, such as different mesh geometries, levels of detail, or material properties. From these options, you can select the configurations according to how you want that entity to appear.

You can load a configuration catalog from a USD file with variant sets or a `.reality` file with a configuration catalog.

##### Create a Configuration Catalog

To create a configuration catalog with RealityKit, first set up a configuration set for each category you want to represent. A configuration set consists of a name and an array of alternative representations for that category. For example, a configuration set can include different levels of detail or different material representations of an entity.

The following example creates a configuration set for the categories `size` and `color`:

```swift
let configurationSets: [Entity.ConfigurationCatalog.ConfigurationSet] = [
    try Entity.ConfigurationCatalog.ConfigurationSet(
        id: "size",
        configurations: [
            Entity.ConfigurationCatalog.Configuration(id: "small"),
            Entity.ConfigurationCatalog.Configuration(id: "big")
        ],
        defaultConfigurationId: "small"
    ),
    try Entity.ConfigurationCatalog.ConfigurationSet(
        id: "color",
        configurations: [
            Entity.ConfigurationCatalog.Configuration(id: "red"),
            Entity.ConfigurationCatalog.Configuration(id: "green"),
        defaultConfigurationId: "green"
    ),
]
```

Use a configuration combination to associate entities that represent specific configuration choices with a dictionary that describes those selections, as the following example shows:

```swift
let combinations: [Entity.ConfigurationCatalog.ConfigurationCombination] = [
    Entity.ConfigurationCatalog.ConfigurationCombination(
        entity: smallRedEntity,
        configurationSpecifications: ["size" : "small", "color" : "red"]
    ),
    Entity.ConfigurationCatalog.ConfigurationCombination(
        entity: smallGreenEntity,
        configurationSpecifications: ["size" : "small", "color" : "green"]
    ),
    Entity.ConfigurationCatalog.ConfigurationCombination(
        entity: bigRedEntity,
        configurationSpecifications: ["size" : "big", "color" : "red"]
    ),
    Entity.ConfigurationCatalog.ConfigurationCombination(
        entity: bigGreenEntity,
        configurationSpecifications: ["size" : "big", "color" : "green"]
    ),
]
```

Create a catalog from the configuration sets and combinations.

```swift
let configurableEntity = try Entity.ConfigurationCatalog(
   configurationSets: configurationSets,
   combinations: combinations
)
```

Save the catalog to a `.reality` file that your RealityKit app can load.

```swift
try await configurableEntity.write(to: url)
```

##### Load an Entity with a Configuration

The following code example loads a small, red entity from the configuration catalog in the preceding example. The entity initializer looks for the catalog to have configuration sets named `size` and `color`, and the sets to contain configurations named `small` and `red`, respectively.

```swift
func loadSmallRedEntity(from url: URL) async throws -> Entity {
    let catalog = try await Entity.ConfigurationCatalog(from: url)
    return try await Entity(
        from: catalog,
        configurations: ["size": "small", "color": "red"]
    )
}
```

## Topics

### Opening a catalog from a file
- [init(from: URL) async throws](entity/configurationcatalog/init(from:).md)
  Loads a configuration catalog from a USD or reality file.
### Defining configuration choices
- [Entity.ConfigurationCatalog.Configuration](entity/configurationcatalog/configuration.md)
  A type that represents an alternative that you can choose.
- [Entity.ConfigurationCatalog.ConfigurationSet](entity/configurationcatalog/configurationset.md)
  A collection of alternatives to choose from.
- [Entity.ConfigurationCatalog.ConfigurationCombination](entity/configurationcatalog/configurationcombination.md)
  A type that associates an entity with a combination of configurations.
### Querying available configuration choices
- [var configurationSets: [String : Entity.ConfigurationCatalog.ConfigurationSet]](entity/configurationcatalog/configurationsets.md)
  The configuration sets that configure the default prim or entity.
### Saving a configuration catalog to a file
- [func write(to: URL) async throws](entity/configurationcatalog/write(to:).md)
  Writes the configurations of the configuration catalog to a reality file.
### Initializers
- [init(configurationSets:combinations:)](entity/configurationcatalog/init(configurationsets:combinations:).md)
  Creates a configuration catalog from in-memory entities and an array of configuration sets.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [convenience init(from: Entity.ConfigurationCatalog, configurations: [String : String]?) async throws](entity/init(from:configurations:).md)
  Loads an entity from a configuration catalog and a dictionary of configuration choices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/configurationcatalog)*