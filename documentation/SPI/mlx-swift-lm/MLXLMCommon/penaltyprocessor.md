---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/penaltyprocessor"
framework: "mlx-swift-lm/MLXLMCommon"
---

# PenaltyProcessor

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Processor that composes penalty processors in Python mlx-lm order.

## Declaration

```swift
struct PenaltyProcessor
```

## Topics

### Initializers
- [init(repetitionContext: RepetitionContext?, presenceContext: PresencePenaltyContext?, frequencyContext: FrequencyPenaltyContext?)](./penaltyprocessor/init%28repetitioncontext,presencecontext,frequencycontext%29.md)
### Instance Methods
- [func didSample(token: MLXArray)](./penaltyprocessor/didsample%28token%29.md)
- [func process(logits: MLXArray) -> MLXArray](./penaltyprocessor/process%28logits%29.md)
- [func prompt(MLXArray)](./penaltyprocessor/prompt%28_%29.md)
### Default Implementations
- [LogitProcessor Implementations](./penaltyprocessor/logitprocessor-implementations.md)

## Relationships

### Conforms To
- [LogitProcessor](./logitprocessor.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/penaltyprocessor)*