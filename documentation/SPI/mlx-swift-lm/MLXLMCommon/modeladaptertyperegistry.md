---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladaptertyperegistry"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelAdapterTypeRegistry

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class ModelAdapterTypeRegistry
```

## Topics

### Initializers
- [init()](./modeladaptertyperegistry/init%28%29.md)
  Creates an empty registry.
- [init(creators: [String : @Sendable (URL) throws -> any ModelAdapter])](./modeladaptertyperegistry/init%28creators%29.md)
  Creates a registry with given creators.
### Instance Methods
- [func createAdapter(directory: URL, adapterType: String) throws -> ModelAdapter](./modeladaptertyperegistry/createadapter%28directory,adaptertype%29.md)
- [func registerAdapterType(String, creator: @Sendable (URL) throws -> any ModelAdapter)](./modeladaptertyperegistry/registeradaptertype%28_,creator%29.md)
  Add a new model adapter to the type registry.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladaptertyperegistry)*