---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/logitsampler"
framework: "mlx-swift-lm/MLXLMCommon"
---

# LogitSampler

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

A `LogitSampler` is responsible for sampling `logits` produced by a [`LanguageModel`](./languagemodel.md) to produce a token.

## Declaration

```swift
protocol LogitSampler
```

## Overview

See also: [`LogitProcessor`](./logitprocessor.md)

## Topics

### Instance Methods
- [func sample(logits: MLXArray) -> MLXArray](./logitsampler/sample%28logits%29.md)
  Given `logits` produce a new `MLXArray` with the token.

## Relationships

### Conforming Types
- [ArgMaxSampler](./argmaxsampler.md)
- [CategoricalSampler](./categoricalsampler.md)
- [TopPSampler](./toppsampler.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/logitsampler)*