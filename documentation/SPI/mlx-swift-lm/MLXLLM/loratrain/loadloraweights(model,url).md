---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/loratrain/loadloraweights(model:url:)"
framework: "mlx-swift-lm/MLXLLM"
---

# loadLoRAWeights(model:url:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Type Method

Load saved LoRA weights into a model that already has matching adapter layers applied.

## Declaration

```swift
static func loadLoRAWeights(model: Module, url: URL) throws
```

#### Discussion

Use `LoRAContainer.from(model:configuration:)` to construct and freeze the adapter layers before calling this method. Set [`completedIterations`](./parameters/completediterations.md) when continuing a run whose `iterations` value is the desired total number of iterations. This restores adapter parameters only; callers that require exact optimizer continuation must persist and restore optimizer state separately. The file must not contain keys that are absent from the model’s adapter structure.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/loratrain/loadloraweights(model:url:))*