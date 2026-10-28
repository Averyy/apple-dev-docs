---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetprocessor"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ThinkingBudgetProcessor

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

A token-level, protocol-aware reasoning budget.

## Declaration

```swift
struct ThinkingBudgetProcessor
```

## Overview

The processor observes compiled start and end token sequences instead of repeatedly decoding generated text. At the budget boundary it either lets a partially sampled natural end finish, or forces the model-specific [`ReasoningBudgetTransition`](./reasoningbudgettransition.md). Every forced token passes through the normal generation loop and therefore remains coherent with KV cache, history, speculative verification, and the emitted stream.

### Pipelining

`TokenIterator` samples a token, hands it to the processor, and only then calls `asyncEval`, so that the *previous* token is what gets read back on the CPU. Reading the newest token instead would block on the in-flight forward pass and collapse that one-step lookahead — the same hazard `TokenRing` avoids for the penalty processors. This processor therefore keeps the freshest sampled token in flight and only drains it when a budget decision is actually within reach. See [`didSample(token:)`](./thinkingbudgetprocessor/didsample%28token%29.md).

## Topics

### Initializers
- [init(configuration: ThinkingBudgetConfiguration, reasoning: ReasoningConfig, tokenizer: any Tokenizer, diagnosticHandler: (@Sendable (ThinkingBudgetDiagnostic) -> Void)?) throws](./thinkingbudgetprocessor/init%28configuration,reasoning,tokenizer,diagnostichandler%29.md)
  Creates a processor for direct use with a token iterator.
### Instance Properties
- [var didStandDown: Bool](./thinkingbudgetprocessor/didstanddown.md)
  Whether the processor stood down because a sampled token did not match the constraint it had applied.
### Instance Methods
- [func didEmit(token: Int)](./thinkingbudgetprocessor/didemit%28token%29.md)
- [func didSample(token: MLXArray)](./thinkingbudgetprocessor/didsample%28token%29.md)
  Records a sampled token, deferring the CPU←GPU read when it is safe.
- [func finalizeGeneration()](./thinkingbudgetprocessor/finalizegeneration%28%29.md)
- [func process(logits: MLXArray) -> MLXArray](./thinkingbudgetprocessor/process%28logits%29.md)
- [func prompt(MLXArray)](./thinkingbudgetprocessor/prompt%28_%29.md)
### Default Implementations
- [LogitProcessor Implementations](./thinkingbudgetprocessor/logitprocessor-implementations.md)

## Relationships

### Conforms To
- [LogitProcessor](./logitprocessor.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetprocessor)*