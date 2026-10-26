---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/mamba2model/prepare(_:cache:state:prefill:)"
framework: "mlx-swift-lm/MLXLLM"
---

# prepare(_:cache:state:prefill:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Instance Method

Default prepare step for [`LLMModel`](../llmmodel.md).

## Declaration

```swift
func prepare(_ input: LMInput, cache: [KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult
```

#### Discussion

Evaluates the prompt into the cache in chunks of at most `PrefillParameters.stepSize` (default 512), leaving one token for the `TokenIterator`’s first forward. With `PrefillParameters.Chunking.balanced` (the default) the chunks are equal-sized, so no forward is a small remainder paying full attention cost against the whole prompt.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/mamba2model/prepare(_:cache:state:prefill:))*