---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationtransformer"
framework: "mlx-swift-lm/MLXLMCommon"
---

# GenerationTransformer

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Configures a chat request and composes its per-pass token handlers.

## Declaration

```swift
protocol GenerationTransformer : Sendable
```

## Mentions

- [Observing token log probabilities](./generation-observability.md)

#### Overview

A session may run several generation passes when it dispatches tools. Keep request configuration here and decoding state in the handler created for each pass.

## Topics

### Associated Types
- [associatedtype Handler : TokenLoopHandler](./generationtransformer/handler.md)
### Instance Methods
- [func configure(inout GenerateParameters)](./generationtransformer/configure%28_%29.md)
  Configures a request-local copy of the session’s generation parameters.
- [func makeHandler(wrapping: TextToolTokenLoopHandler) -> Handler](./generationtransformer/makehandler%28wrapping%29.md)
  Creates a fresh handler on each pass, including automatic tool restarts.
### Type Properties
- [static var text: Self](./generationtransformer/text.md)
  Use the standard text/tool handler without changing generation parameters.
### Type Methods
- [static func logProbabilities(topCount: Int) -> Self](./generationtransformer/logprobabilities%28topcount%29.md)
  Observe chosen-token log probabilities and, optionally, the top candidates.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [LogProbabilityGenerationTransformer](./logprobabilitygenerationtransformer.md)
- [TextGenerationTransformer](./textgenerationtransformer.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationtransformer)*