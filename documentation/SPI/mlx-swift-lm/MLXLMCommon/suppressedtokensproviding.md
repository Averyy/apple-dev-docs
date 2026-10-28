---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/suppressedtokensproviding"
framework: "mlx-swift-lm/MLXLMCommon"
---

# SuppressedTokensProviding

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

A language model that exposes token IDs that must never be sampled during generation.

## Declaration

```swift
protocol SuppressedTokensProviding : AnyObject
```

## Overview

Multimodal models seed this set with the placeholder token IDs from their configuration (image / audio / video soft tokens and their begin/end markers). Those tokens are prompt-side markers that carry no meaning as generated text, but they can occasionally be sampled if left unmasked and then leak into the output verbatim (e.g. `<audio|>` read aloud by TTS). Model factories additionally merge `suppress_tokens` from `generation_config.json` into this set after the model is created.

Token iterators consult this set at initialization and chain a [`SuppressTokensProcessor`](./suppresstokensprocessor.md) after the parameter-derived processor, masking the corresponding logits to `-inf` before sampling. Only generated tokens are affected; prompt tokens are never modified.

## Topics

### Instance Properties
- [var suppressedTokenIds: Set<Int>](./suppressedtokensproviding/suppressedtokenids.md)
  Token IDs whose logits are masked to `-inf` before sampling.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/suppressedtokensproviding)*