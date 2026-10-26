---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/logprobabilitygenerationtransformer"
framework: "mlx-swift-lm/MLXLMCommon"
---

# LogProbabilityGenerationTransformer

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Adds ordered per-token log probabilities to a chat request.

## Declaration

```swift
struct LogProbabilityGenerationTransformer
```

## Mentions

- [Observing token log probabilities](./generation-observability.md)

## Topics

### Initializers
- [init(topCount: Int)](./logprobabilitygenerationtransformer/init%28topcount%29.md)
### Instance Properties
- [var topCount: Int](./logprobabilitygenerationtransformer/topcount.md)
  Number of top candidates. Values at or below zero report only the chosen token.
### Instance Methods
- [func configure(inout GenerateParameters)](./logprobabilitygenerationtransformer/configure%28_%29.md)
- [func makeHandler(wrapping: TextToolTokenLoopHandler) -> LogProbabilityTokenLoopHandler<TextToolTokenLoopHandler>](./logprobabilitygenerationtransformer/makehandler%28wrapping%29.md)
### Default Implementations
- [GenerationTransformer Implementations](./logprobabilitygenerationtransformer/generationtransformer-implementations.md)

## Relationships

### Conforms To
- [GenerationTransformer](./generationtransformer.md)
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/logprobabilitygenerationtransformer)*