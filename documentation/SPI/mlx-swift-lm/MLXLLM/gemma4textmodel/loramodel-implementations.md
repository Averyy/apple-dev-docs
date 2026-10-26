---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gemma4textmodel/loramodel-implementations"
framework: "mlx-swift-lm/MLXLLM"
---

# LoRAModel Implementations

**Framework**: mlx-swift-lm/MLXLLM  
**Role**: API Collection

## Topics

### Instance Properties
- [var loraDefaultKeys: [String]](./loradefaultkeys.md)
- [var loraLayers: [Module]](./loralayers.md)
  Decoder layers, not just attention: LoRA keys are matched against the children of each returned module, so `mlp.*` targets only resolve when the layer itself is returned (as Gemma3Text / Qwen35 / Llama do).
- [var loraMetadata: LoRAModelMetadata](./lorametadata.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gemma4textmodel/loramodel-implementations)*