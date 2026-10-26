---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loramodelmetadata"
framework: "mlx-swift-lm/MLXLMCommon"
---

# LoRAModelMetadata

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Metadata describing where a model applies LoRA adapters.

## Declaration

```swift
struct LoRAModelMetadata
```

## Topics

### Initializers
- [init(layerCount: Int, defaultKeys: [String])](./loramodelmetadata/init%28layercount,defaultkeys%29.md)
### Instance Properties
- [let defaultKeys: [String]](./loramodelmetadata/defaultkeys.md)
  Default module paths, relative to each LoRA layer, that receive adapters.
- [let layerCount: Int](./loramodelmetadata/layercount.md)
  Number of model layers that support LoRA adapters.
### Default Implementations
- [Equatable Implementations](./loramodelmetadata/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loramodelmetadata)*