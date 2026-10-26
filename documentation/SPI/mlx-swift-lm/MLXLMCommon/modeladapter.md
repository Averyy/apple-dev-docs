---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladapter"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelAdapter

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Protocol defining an adapter that can modify a `LanguageModel`.

## Declaration

```swift
protocol ModelAdapter : Sendable
```

## Topics

### Instance Methods
- [func fuse(with: LanguageModel) throws](./modeladapter/fuse%28with%29.md)
  Permanently fuses the adapter into the specified model.
- [func load(into: LanguageModel) throws](./modeladapter/load%28into%29.md)
  Loads the adapter into the specified model.
- [func unload(from: LanguageModel)](./modeladapter/unload%28from%29.md)
  Unloads the adapter from the specified model.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [LoRAContainer](./loracontainer.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladapter)*