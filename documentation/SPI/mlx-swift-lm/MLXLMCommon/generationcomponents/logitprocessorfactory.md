---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationcomponents/logitprocessorfactory"
framework: "mlx-swift-lm/MLXLMCommon"
---

# logitProcessorFactory

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Optional factory producing a custom [`LogitProcessor`](../logitprocessor.md) that is composed after the built-in penalty processor, see [`logitProcessor(parameters:)`](./logitprocessor%28parameters%29.md).

## Declaration

```swift
var logitProcessorFactory: (@Sendable () -> any LogitProcessor)?
```

#### Discussion

This lets custom logit processing – for example grammar-constrained or otherwise structured decoding – ride any parameters-driven API, including [`ChatSession`](../chatsession.md) and the parameters-based [`TokenIterator`](../tokeniterator.md) initializers.

This is a factory rather than a stored [`LogitProcessor`](../logitprocessor.md) because processors are stateful (see [`didSample(token:)`](../logitprocessor/didsample%28token%29.md)): it is invoked once per generation so each generation gets a fresh instance and state cannot leak across generations. A `@Sendable` closure also keeps `GenerationComponents` `Sendable`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationcomponents/logitprocessorfactory)*