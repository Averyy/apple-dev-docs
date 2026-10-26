---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/logprobabilitygeneration"
framework: "mlx-swift-lm/MLXLMCommon"
---

# LogProbabilityGeneration

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Events from a handler composed with [`LogProbabilityTokenLoopHandler`](./logprobabilitytokenloophandler.md).

## Declaration

```swift
enum LogProbabilityGeneration<Output> where Output : Sendable
```

## Topics

### Enumeration Cases
- [LogProbabilityGeneration.generation(_:)](./logprobabilitygeneration/generation%28_%29.md)
  An event produced by the wrapped handler.
- [case probability(GenerateTokenLogProbabilities)](./logprobabilitygeneration/probability%28_%29.md)
  Log probabilities for one token, emitted before the wrapped handler’s events.
### Instance Properties
- [var logProbabilities: GenerateTokenLogProbabilities?](./logprobabilitygeneration/logprobabilities.md)
  One token’s log probabilities; `nil` for an event from the wrapped handler.
### Default Implementations
- [GenerationProviding Implementations](./logprobabilitygeneration/generationproviding-implementations.md)

## Relationships

### Conforms To
- [GenerationProviding](./generationproviding.md)
- Swift.Copyable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/logprobabilitygeneration)*