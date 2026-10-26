---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationcomponents/logitprocessor(parameters:model:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# logitProcessor(parameters:model:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

As [`logitProcessor(parameters:)`](./logitprocessor%28parameters%29.md), additionally masking the token ids the model suppresses – declared through [`SuppressedTokensProviding`](../suppressedtokensproviding.md) or read from its `generation_config.json`.

## Declaration

```swift
func logitProcessor(parameters: GenerateParameters, model: any LanguageModel) -> LogitProcessor?
```

#### Discussion

Suppression runs last so that no processor composed before it can reintroduce a masked id – for multimodal placeholder tokens, emitting one is never valid output.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationcomponents/logitprocessor(parameters:model:))*