---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatconventionsproviding"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ChatConventionsProviding

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

A model’s chat conventions: how it encodes tool calls and how it reasons.

## Declaration

```swift
protocol ChatConventionsProviding
```

## Overview

This knowledge lives with the model definition rather than in a centralized `model_type` table. [`LanguageModel`](./languagemodel.md) conforms with `nil` defaults, so the model factories read `model.toolCallFormat` / `model.reasoningConfig` directly. A model opts in by overriding either property in an extension.

For conventions that are not model-intrinsic (anything keyed on the repo id, such as DeepSeek-R1-Distill), register a [`ChatConventionsResolving`](./chatconventionsresolving.md) with [`ChatConventionsRegistry`](./chatconventionsregistry.md) instead. Resolvers take precedence over a model’s own declaration; see [`ChatConventionsRegistry`](./chatconventionsregistry.md) for the full resolution order.

## Topics

### Instance Properties
- [var reasoningConfig: ReasoningConfig?](./chatconventionsproviding/reasoningconfig.md)
  The model’s reasoning protocol, or `nil` for non-reasoning models.
- [var toolCallFormat: ToolCallFormat?](./chatconventionsproviding/toolcallformat.md)
  The tool-call format this model emits, or `nil` for the JSON default.

## Relationships

### Inherited By
- [LanguageModel](./languagemodel.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatconventionsproviding)*