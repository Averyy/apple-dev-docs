---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconfiguration/messagegenerator"
framework: "mlx-swift-lm/MLXLMCommon"
---

# messageGenerator

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Overrides the [`MessageGenerator`](../messagegenerator.md) the model would otherwise supply.

## Declaration

```swift
var messageGenerator: (any MessageGenerator)?
```

## Discussion

A model class is shared by every checkpoint of its model type, so a fine-tune that needs a different chat-template shape cannot express that on the model itself without affecting its siblings – e.g. TranslateGemma, which loads through the same `gemma3` text path as plain Gemma 3. Set this on the registry entry (or by the caller) instead. `nil` keeps the model’s own default.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconfiguration/messagegenerator)*