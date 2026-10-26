---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loramodel/loradefaultkeys"
framework: "mlx-swift-lm/MLXLMCommon"
---

# loraDefaultKeys

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Default layer keys to apply LoRA adapters to.

## Declaration

```swift
var loraDefaultKeys: [String] { get }
```

#### Discussion

Used when not specified in `adapter_config.json`. Otherwise, keys from the config are applied.

## Default Implementations

### LoRAModel Implementations
- [var loraDefaultKeys: [String]](./loradefaultkeys-332js.md)
  By default we apply LoRA to all Linear layers. This is aligned with `mlx-lm` Python logic.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loramodel/loradefaultkeys)*