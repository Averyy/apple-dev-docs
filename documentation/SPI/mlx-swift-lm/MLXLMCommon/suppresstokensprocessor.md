---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/suppresstokensprocessor"
framework: "mlx-swift-lm/MLXLMCommon"
---

# SuppressTokensProcessor

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Processor that masks a fixed set of token IDs to `-inf` so they can never be sampled.

## Declaration

```swift
struct SuppressTokensProcessor
```

## Overview

Port of `SuppressTokensLogitsProcessor` from Hugging Face `transformers`, which is driven by `suppress_tokens` in `generation_config.json`.

## Topics

### Initializers
- [init?(tokenIds: Set<Int>)](./suppresstokensprocessor/init%28tokenids%29.md)
  Create a processor masking the given token IDs.
### Instance Methods
- [func didSample(token: MLXArray)](./suppresstokensprocessor/didsample%28token%29.md)
- [func process(logits: MLXArray) -> MLXArray](./suppresstokensprocessor/process%28logits%29.md)
- [func prompt(MLXArray)](./suppresstokensprocessor/prompt%28_%29.md)
### Default Implementations
- [LogitProcessor Implementations](./suppresstokensprocessor/logitprocessor-implementations.md)

## Relationships

### Conforms To
- [LogitProcessor](./logitprocessor.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/suppresstokensprocessor)*