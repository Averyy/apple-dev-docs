---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/frequencypenaltycontext"
framework: "mlx-swift-lm/MLXLMCommon"
---

# FrequencyPenaltyContext

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Processor that applies an additive frequency penalty to tokens in a recent context window.

## Declaration

```swift
struct FrequencyPenaltyContext
```

## Overview

Frequency counting is performed on GPU via `scatter_add` to build a histogram of token occurrences, avoiding CPU←GPU synchronization.

## Topics

### Initializers
- [init(frequencyPenalty: Float, frequencyContextSize: Int)](./frequencypenaltycontext/init%28frequencypenalty,frequencycontextsize%29.md)
### Instance Methods
- [func didSample(token: MLXArray)](./frequencypenaltycontext/didsample%28token%29.md)
- [func process(logits: MLXArray) -> MLXArray](./frequencypenaltycontext/process%28logits%29.md)
- [func prompt(MLXArray)](./frequencypenaltycontext/prompt%28_%29.md)
### Default Implementations
- [LogitProcessor Implementations](./frequencypenaltycontext/logitprocessor-implementations.md)

## Relationships

### Conforms To
- [LogitProcessor](./logitprocessor.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/frequencypenaltycontext)*