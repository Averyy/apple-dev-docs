---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gemma4textmodel/loralayers"
framework: "mlx-swift-lm/MLXLLM"
---

# loraLayers

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: property  
**Role**: Instance Property

Decoder layers, not just attention: LoRA keys are matched against the children of each returned module, so `mlp.*` targets only resolve when the layer itself is returned (as Gemma3Text / Qwen35 / Llama do).

## Declaration

```swift
var loraLayers: [Module] { get }
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/gemma4textmodel/loralayers)*