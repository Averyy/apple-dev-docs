---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llamamodel/chatconventionsproviding-implementations"
framework: "mlx-swift-lm/MLXLLM"
---

# ChatConventionsProviding Implementations

**Framework**: mlx-swift-lm/MLXLLM  
**Role**: API Collection

## Topics

### Instance Properties
- [var reasoningConfig: ReasoningConfig?](./reasoningconfig.md)
- [var toolCallFormat: ToolCallFormat?](./toolcallformat.md)
  Llama 3 uses an inline `<|python_tag|>` JSON format; Llama 1/2 have no tool-call convention. The distinction is not in `model_type` alone, so it comes from two secondary signals in the checkpoint’s own configuration.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llamamodel/chatconventionsproviding-implementations)*