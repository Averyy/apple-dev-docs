---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniterator/init(input:model:cache:state:processor:sampler:prefillstepsize:maxtokens:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(input:model:cache:state:processor:sampler:prefillStepSize:maxTokens:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

> **Deprecated**: prefill now defaults to balanced chunking; use prefill.chunking = .remainder for the legacy chunk boundaries

## Declaration

```swift
init(input: LMInput, model: any LanguageModel, cache: [KVCache]? = nil, state: LMOutput.State? = nil, processor: LogitProcessor?, sampler: LogitSampler, prefillStepSize: Int?, maxTokens: Int? = nil) throws
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniterator/init(input:model:cache:state:processor:sampler:prefillstepsize:maxtokens:))*