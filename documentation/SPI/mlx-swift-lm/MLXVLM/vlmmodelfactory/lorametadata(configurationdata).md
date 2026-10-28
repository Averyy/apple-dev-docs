---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmmodelfactory/lorametadata(configurationdata:)"
framework: "mlx-swift-lm/MLXVLM"
---

# loraMetadata(configurationData:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Instance Method

Returns the model’s LoRA metadata without loading checkpoint weights or a processor.

## Declaration

```swift
func loraMetadata(configurationData: Data) async throws -> LoRAModelMetadata?
```

## Discussion

Uses the registered model’s `LoRAModel` conformance to select adapter targets.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmmodelfactory/lorametadata(configurationdata:))*