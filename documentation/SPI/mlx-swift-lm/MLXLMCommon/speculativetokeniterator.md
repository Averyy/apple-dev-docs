---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativetokeniterator"
framework: "mlx-swift-lm/MLXLMCommon"
---

# SpeculativeTokenIterator

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Generator of tokens using speculative decoding.

## Declaration

```swift
struct SpeculativeTokenIterator
```

## Overview

This is typically used via a call to [`generate(input:cache:state:parameters:context:draftModel:draftCache:numDraftTokens:components:wiredMemoryTicket:tools:)`](./generate%28input,cache,state,parameters,context,draftmodel,draftcache,numdrafttokens,components,wiredmemoryticket,tools%29.md) returning `AsyncStream<Generation>`.

To use it directly:

```swift
let generateParameters: GenerateParameters
let input: LMInput
let mainModel: LanguageModel
let draftModel: LanguageModel

let iterator = try SpeculativeTokenIterator(
    input: input, mainModel: mainModel, draftModel: draftModel,
    parameters: generateParameters, numDraftTokens: 2)

for token in iterator {
    ...
}
```

Tokens are integers that can be passed through a `Tokenizer` or [`StreamingDetokenizer`](./streamingdetokenizer.md) to produce Strings.

Port of `speculative_generate_step()` from https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/generate.py

## Topics

### Initializers
- [init(input: LMInput, mainModel: any LanguageModel, draftModel: any LanguageModel, mainCache: [KVCache]?, draftCache: [KVCache]?, mainState: LMOutput.State?, parameters: GenerateParameters, numDraftTokens: Int, components: GenerationComponents) throws](./speculativetokeniterator/init%28input,mainmodel,draftmodel,maincache,draftcache,mainstate,parameters,numdrafttokens,components%29.md)
  Initialize a `SpeculativeTokenIterator` with the given input.
### Instance Properties
- [var evictedTokenCount: Int](./speculativetokeniterator/evictedtokencount.md)
- [let maxTokens: Int?](./speculativetokeniterator/maxtokens.md)
- [var promptPrefillTime: TimeInterval](./speculativetokeniterator/promptprefilltime.md)
- [var reasoningTokenCount: Int?](./speculativetokeniterator/reasoningtokencount.md)
- [var speculativeDecodingTelemetry: SpeculativeDecodingTelemetry?](./speculativetokeniterator/speculativedecodingtelemetry.md)
- [var state: LMOutput.State?](./speculativetokeniterator/state.md)
  Model state carried by the main model, as [`state`](./tokeniterator/state.md).
- [var tokenCount: Int](./speculativetokeniterator/tokencount.md)
### Instance Methods
- [func discardGeneratedToken()](./speculativetokeniterator/discardgeneratedtoken%28%29.md)
- [func next() -> Int?](./speculativetokeniterator/next%28%29.md)
- [func recordEmittedToken(Int)](./speculativetokeniterator/recordemittedtoken%28_%29.md)
### Default Implementations
- [Sequence Implementations](./speculativetokeniterator/sequence-implementations.md)
- [TokenIteratorProtocol Implementations](./speculativetokeniterator/tokeniteratorprotocol-implementations.md)

## Relationships

### Conforms To
- Swift.IteratorProtocol
- Swift.Sequence
- [TokenIteratorProtocol](./tokeniteratorprotocol.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativetokeniterator)*