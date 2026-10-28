---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loracontainer/from(model:configuration:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# from(model:configuration:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Type Method

Creates a `LoRAContainer` by applying the configuration to a compatible `LanguageModel`.

## Declaration

```swift
static func from(model: LanguageModel, configuration: LoRAConfiguration = .init()) throws -> LoRAContainer
```

## Discussion

Note:  This function freezes the model base weights and applies LoRA layers to it.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loracontainer/from(model:configuration:))*