---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chainedlogitprocessor"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ChainedLogitProcessor

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Processor that applies multiple [`LogitProcessor`](./logitprocessor.md) instances in order.

## Declaration

```swift
struct ChainedLogitProcessor
```

#### Overview

[`logitProcessor(parameters:)`](./generationcomponents/logitprocessor%28parameters%29.md) uses this to compose the built-in [`PenaltyProcessor`](./penaltyprocessor.md) with a processor from [`logitProcessorFactory`](./generationcomponents/logitprocessorfactory.md). It can also be used directly to combine several custom processors into one.

## Topics

### Initializers
- [init(processors: [any LogitProcessor])](./chainedlogitprocessor/init%28processors%29.md)
### Instance Methods
- [func copy() -> ChainedLogitProcessor](./chainedlogitprocessor/copy%28%29.md)
- [func didEmit(token: Int)](./chainedlogitprocessor/didemit%28token%29.md)
- [func didSample(token: MLXArray)](./chainedlogitprocessor/didsample%28token%29.md)
- [func finalizeGeneration()](./chainedlogitprocessor/finalizegeneration%28%29.md)
- [func process(logits: MLXArray) -> MLXArray](./chainedlogitprocessor/process%28logits%29.md)
- [func prompt(MLXArray)](./chainedlogitprocessor/prompt%28_%29.md)
### Default Implementations
- [LogitProcessor Implementations](./chainedlogitprocessor/logitprocessor-implementations.md)

## Relationships

### Conforms To
- [LogitProcessor](./logitprocessor.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chainedlogitprocessor)*