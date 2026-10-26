---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/apertusmodel/prepare(_:cache:state:windowsize:)"
framework: "mlx-swift-lm/MLXLLM"
---

# prepare(_:cache:state:windowSize:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Instance Method

Inherited from `LanguageModel.prepare(_:cache:state:windowSize:)`.

> **Deprecated**: prefill now defaults to balanced chunking; use prefill.chunking = .remainder for the legacy chunk boundaries

## Declaration

```swift
func prepare(_ input: LMInput, cache: [any KVCache], state: LMOutput.State?, windowSize: Int?) throws -> PrepareResult
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/apertusmodel/prepare(_:cache:state:windowsize:))*