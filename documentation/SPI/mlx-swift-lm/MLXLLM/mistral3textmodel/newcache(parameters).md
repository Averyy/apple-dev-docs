---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/mistral3textmodel/newcache(parameters:)"
framework: "mlx-swift-lm/MLXLLM"
---

# newCache(parameters:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Instance Method

Create appropriate caches for each layer type.

## Declaration

```swift
func newCache(parameters: GenerateParameters?) throws -> [KVCache]
```

#### Discussion

Sliding-window layers use the smaller of the architecture window and `GenerateParameters.maxKVSize`; full-attention layers use the requested limit.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/mistral3textmodel/newcache(parameters:))*