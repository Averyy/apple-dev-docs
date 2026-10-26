---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmtyperegistry"
framework: "mlx-swift-lm/MLXLLM"
---

# LLMTypeRegistry

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: enum  
**Role**: Enumeration

Registry of model type, e.g ‘llama’, to functions that can instantiate the model from configuration.

## Declaration

```swift
enum LLMTypeRegistry
```

#### Overview

Typically called via [`loadContainer(from:using:configuration:useLatest:progressHandler:)`](./llmmodelfactory/loadcontainer%28from,using,configuration,uselatest,progresshandler%29.md).

## Topics

### Type Properties
- [static let shared: ModelTypeRegistry<LanguageModel>](./llmtyperegistry/shared.md)
  Shared instance with default model types.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmtyperegistry)*