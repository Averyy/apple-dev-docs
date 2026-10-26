---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loramodel/loralayers"
framework: "mlx-swift-lm/MLXLMCommon"
---

# loraLayers

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Return the layers to apply LoRA adapters to.

## Declaration

```swift
var loraLayers: [Module] { get }
```

#### Discussion

Typically, this includes all transformer layers. Must be defined explicitly since we can’t unify it across all models.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loramodel/loralayers)*