---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mlxnn/module/setloraenabled(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# setLoRAEnabled(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Walk all submodules and set `loraEnabled` on every `LoRALayer` found.

## Declaration

```swift
func setLoRAEnabled(_ enabled: Bool)
```

#### Discussion

This is the generic, always-correct path. For hot loops that toggle the adapter many times per generation (e.g. speculative decoding), cache the `[LoRALayer]` list once and call `loraEnabled = enabled` directly on each — see `NemotronLabsDiffusionModel.setLoRAEnabledFast`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mlxnn/module/setloraenabled(_:))*