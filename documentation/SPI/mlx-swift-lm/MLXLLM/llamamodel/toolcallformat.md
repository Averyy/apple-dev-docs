---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llamamodel/toolcallformat"
framework: "mlx-swift-lm/MLXLLM"
---

# toolCallFormat

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: property  
**Role**: Instance Property

Llama 3 uses an inline `<|python_tag|>` JSON format; Llama 1/2 have no tool-call convention. The distinction is not in `model_type` alone, so it comes from two secondary signals in the checkpoint’s own configuration.

## Declaration

```swift
var toolCallFormat: ToolCallFormat? { get }
```

#### Discussion

Gated on `model_type == "llama"` because this class also backs the `mistral` registry entry, and Mistral-Nemo’s vocabulary (131072) would otherwise trip the Llama 3 vocabulary signal.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llamamodel/toolcallformat)*