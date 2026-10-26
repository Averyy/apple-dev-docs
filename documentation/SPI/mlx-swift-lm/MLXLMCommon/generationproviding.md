---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationproviding"
framework: "mlx-swift-lm/MLXLMCommon"
---

# GenerationProviding

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Provides the base event that a chat session uses to maintain its state.

## Declaration

```swift
protocol GenerationProviding : Sendable
```

## Mentions

- [Observing token log probabilities](./generation-observability.md)

## Topics

### Instance Properties
- [var generation: Generation?](./generationproviding/generation.md)
  A decoded event or completion; `nil` for an observation-only event.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [Generation](./generation.md)
- [LogProbabilityGeneration](./logprobabilitygeneration.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationproviding)*