---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loramodel"
framework: "mlx-swift-lm/MLXLMCommon"
---

# LoRAModel

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

## Declaration

```swift
protocol LoRAModel
```

## Topics

### Instance Properties
- [var loraDefaultKeys: [String]](./loramodel/loradefaultkeys.md)
  Default layer keys to apply LoRA adapters to.
- [var loraLayers: [Module]](./loramodel/loralayers.md)
  Return the layers to apply LoRA adapters to.
- [var loraMetadata: LoRAModelMetadata](./loramodel/lorametadata.md)
  Metadata for configuring LoRA without inspecting checkpoint weight names.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loramodel)*