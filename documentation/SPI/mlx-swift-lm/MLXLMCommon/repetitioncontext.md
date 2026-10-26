---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/repetitioncontext"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RepetitionContext

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Processor that implements a `repetitionPenalty`.

## Declaration

```swift
struct RepetitionContext
```

## Topics

### Initializers
- [init(repetitionPenalty: Float, repetitionContextSize: Int)](./repetitioncontext/init%28repetitionpenalty,repetitioncontextsize%29.md)
### Instance Methods
- [func didSample(token: MLXArray)](./repetitioncontext/didsample%28token%29.md)
- [func process(logits: MLXArray) -> MLXArray](./repetitioncontext/process%28logits%29.md)
- [func prompt(MLXArray)](./repetitioncontext/prompt%28_%29.md)
### Default Implementations
- [LogitProcessor Implementations](./repetitioncontext/logitprocessor-implementations.md)

## Relationships

### Conforms To
- [LogitProcessor](./logitprocessor.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/repetitioncontext)*