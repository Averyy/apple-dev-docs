---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeltyperegistry/lorametadata(configurationdata:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# loraMetadata(configurationData:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Inspects the registered model’s LoRA layers without loading checkpoint weights.

## Declaration

```swift
func loraMetadata(configurationData: Data) throws -> LoRAModelMetadata?
```

Available when `T` is `any LanguageModel`.

## Discussion

Model construction and metadata access use an independent random state. Returns `nil` if the model does not conform to [`LoRAModel`](../loramodel.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeltyperegistry/lorametadata(configurationdata:))*