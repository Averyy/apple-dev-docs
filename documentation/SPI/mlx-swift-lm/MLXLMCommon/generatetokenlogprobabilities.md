---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatetokenlogprobabilities"
framework: "mlx-swift-lm/MLXLMCommon"
---

# GenerateTokenLogProbabilities

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Log-probability details for one generated token.

## Declaration

```swift
struct GenerateTokenLogProbabilities
```

#### Overview

These values match Python MLX-LM’s `GenerationResponse.logprobs`: they normalize the post-processor logits before temperature or sampler filters are applied.

## Topics

### Initializers
- [init(chosen: GenerateTokenLogProbability, topLogProbabilities: [GenerateTokenLogProbability])](./generatetokenlogprobabilities/init%28chosen,toplogprobabilities%29.md)
### Instance Properties
- [let chosen: GenerateTokenLogProbability](./generatetokenlogprobabilities/chosen.md)
  The token selected by the sampler and its log probability.
- [let topLogProbabilities: [GenerateTokenLogProbability]](./generatetokenlogprobabilities/toplogprobabilities.md)
  The most likely vocabulary tokens in descending log-probability order.
### Default Implementations
- [Equatable Implementations](./generatetokenlogprobabilities/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatetokenlogprobabilities)*