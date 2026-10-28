---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatconventionsresolving"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ChatConventionsResolving

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Resolves a model’s chat conventions from identity signals the model instance cannot see for itself, today the Hugging Face repo id.

## Declaration

```swift
protocol ChatConventionsResolving : Sendable
```

## Overview

[`ChatConventionsProviding`](./chatconventionsproviding.md) covers everything a model knows about itself. Some conventions are not model-intrinsic: DeepSeek-R1-Distill checkpoints report their *base* `model_type` (`qwen2` or `llama`) and are indistinguishable from plain Qwen2.5/Llama by the model alone, so they can only be recognized by repo id.

Register a resolver with [`ChatConventionsRegistry`](./chatconventionsregistry.md) to supply such conventions, including from outside this package. Both requirements are optional; implement only the one that applies.

## Topics

### Instance Methods
- [func reasoningConfig(modelId: String, modelType: String) -> ReasoningConfig?](./chatconventionsresolving/reasoningconfig%28modelid,modeltype%29.md)
  The reasoning protocol for this model id / type, or `nil` to defer.
- [func toolCallFormat(modelId: String, modelType: String) -> ToolCallFormat?](./chatconventionsresolving/toolcallformat%28modelid,modeltype%29.md)
  The tool-call format for this model id / type, or `nil` to defer.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [DeepSeekR1ConventionsResolver](./deepseekr1conventionsresolver.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatconventionsresolving)*