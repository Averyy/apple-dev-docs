---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationcomponents/logitprocessor(parameters:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# logitProcessor(parameters:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Build the [`LogitProcessor`](../logitprocessor.md) for a single generation.

## Declaration

```swift
func logitProcessor(parameters: GenerateParameters) -> LogitProcessor?
```

#### Discussion

Composes the built-in penalty processor from [`processor()`](../generateparameters/processor%28%29.md) with the custom processor produced by [`logitProcessorFactory`](./logitprocessorfactory.md) (if any). The custom processor runs *after* the penalty processor, matching Python mlx-lm where user `logits_processors` append after `make_logits_processors`.

The factory is invoked here, so a fresh custom processor is produced on every call and stateful processors do not leak state across generations.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationcomponents/logitprocessor(parameters:))*