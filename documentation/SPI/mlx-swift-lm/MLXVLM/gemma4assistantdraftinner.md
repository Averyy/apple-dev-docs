---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4assistantdraftinner"
framework: "mlx-swift-lm/MLXVLM"
---

# Gemma4AssistantDraftInner

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

The drafter’s inner module — mirrors the Python `_DraftInner` so weight keys (`model.embed_tokens.weight`, `model.layers.N.*`, `model.norm.weight`) load without remapping.

## Declaration

```swift
final class Gemma4AssistantDraftInner
```

## Overview

Class is public so it can appear as a property type on [`Gemma4AssistantDraftModel`](./gemma4assistantdraftmodel.md); members are internal because they reference internal-scoped Gemma 4 building blocks (`Gemma4TextDecoderLayer`, `Gemma4RMSNormZeroShift`).

## Topics

### Initializers
- [init(Gemma4TextConfiguration)](./gemma4assistantdraftinner/init%28_%29.md)
### Instance Properties
- [let config: Gemma4TextConfiguration](./gemma4assistantdraftinner/config.md)

## Relationships

### Inherits From
- MLXNN.Module
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4assistantdraftinner)*