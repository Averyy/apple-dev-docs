---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/logitprocessor"
framework: "mlx-swift-lm/MLXLMCommon"
---

# LogitProcessor

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

A `LogitProcessor` is an optional visitor of `logits`.

## Declaration

```swift
protocol LogitProcessor
```

#### Overview

The [`LogitProcessor`](./logitprocessor.md) is called with the input (prompt) before generating tokens:

```swift
processor?.prompt(input.text.tokens)
```

Then for each token generated it has a chance to adjust the logits:

```swift
logits = processor?.process(logits: logits) ?? logits
let y = sampler.sample(logits: logits)
processor?.didSample(token: y)
```

See also: [`LogitSampler`](./logitsampler.md)

## Topics

### Instance Methods
- [func copy() -> Self](./logitprocessor/copy%28%29.md)
  Returns an independent copy of this processor.
- [func didEmit(token: Int)](./logitprocessor/didemit%28token%29.md)
  Called when a sampled token is emitted by the generation stream.
- [func didSample(token: MLXArray)](./logitprocessor/didsample%28token%29.md)
  Called to provide the sampled token
- [func finalizeGeneration()](./logitprocessor/finalizegeneration%28%29.md)
  Called after the generation stream has emitted its last token.
- [func process(logits: MLXArray) -> MLXArray](./logitprocessor/process%28logits%29.md)
  Called to visit and possibly modify the logits
- [func prompt(MLXArray)](./logitprocessor/prompt%28_%29.md)
  Called before token generation starts with the text tokens of the prompt

## Relationships

### Conforming Types
- [ChainedLogitProcessor](./chainedlogitprocessor.md)
- [FrequencyPenaltyContext](./frequencypenaltycontext.md)
- [PenaltyProcessor](./penaltyprocessor.md)
- [PresencePenaltyContext](./presencepenaltycontext.md)
- [RepetitionContext](./repetitioncontext.md)
- [SuppressTokensProcessor](./suppresstokensprocessor.md)
- [ThinkingBudgetProcessor](./thinkingbudgetprocessor.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/logitprocessor)*