---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/presencepenaltycontext"
framework: "mlx-swift-lm/MLXLMCommon"
---

# PresencePenaltyContext

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Processor that applies an additive presence penalty to tokens in a recent context window.

## Declaration

```swift
struct PresencePenaltyContext
```

## Overview

The penalty is applied once per unique token via scatter-write (writing the same value to the same index multiple times is idempotent).

## Topics

### Initializers
- [init(presencePenalty: Float, presenceContextSize: Int)](./presencepenaltycontext/init%28presencepenalty,presencecontextsize%29.md)
### Instance Methods
- [func didSample(token: MLXArray)](./presencepenaltycontext/didsample%28token%29.md)
- [func process(logits: MLXArray) -> MLXArray](./presencepenaltycontext/process%28logits%29.md)
- [func prompt(MLXArray)](./presencepenaltycontext/prompt%28_%29.md)
### Default Implementations
- [LogitProcessor Implementations](./presencepenaltycontext/logitprocessor-implementations.md)

## Relationships

### Conforms To
- [LogitProcessor](./logitprocessor.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/presencepenaltycontext)*