---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/abstractmodelregistry"
framework: "mlx-swift-lm/MLXLMCommon"
---

# AbstractModelRegistry

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class AbstractModelRegistry
```

## Topics

### Initializers
- [init()](./abstractmodelregistry/init%28%29.md)
  Creates an empty registry.
- [init(modelConfigurations: [ModelConfiguration])](./abstractmodelregistry/init%28modelconfigurations%29.md)
  Creates a new registry with from given model configurations.
### Instance Properties
- [var models: some Collection<ModelConfiguration> & Sendable](./abstractmodelregistry/models.md)
### Instance Methods
- [func configuration(id: String) -> ModelConfiguration](./abstractmodelregistry/configuration%28id%29.md)
  Returns configuration from [`modelRegistry`](./genericmodelfactory/modelregistry.md).
- [func contains(id: String) -> Bool](./abstractmodelregistry/contains%28id%29.md)
  Returns true if the registry contains a model with the id. Otherwise, false.
- [func register(configurations: [ModelConfiguration])](./abstractmodelregistry/register%28configurations%29.md)

## Relationships

### Inherited By
- [MTPDrafterRegistry](./mtpdrafterregistry.md)
### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/abstractmodelregistry)*