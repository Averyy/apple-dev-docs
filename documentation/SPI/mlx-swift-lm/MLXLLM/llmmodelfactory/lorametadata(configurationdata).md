---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmmodelfactory/lorametadata(configurationdata:)"
framework: "mlx-swift-lm/MLXLLM"
---

# loraMetadata(configurationData:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Instance Method

Returns the model’s LoRA metadata from its configuration without loading weights.

## Declaration

```swift
func loraMetadata(configurationData: Data) async throws -> LoRAModelMetadata?
```

## Mentions

- [Using a Model](../using-model.md)

#### Discussion

The registered model architecture is instantiated so custom `LoRAModel.loraDefaultKeys` implementations remain authoritative. No checkpoint files are read.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmmodelfactory/lorametadata(configurationdata:))*