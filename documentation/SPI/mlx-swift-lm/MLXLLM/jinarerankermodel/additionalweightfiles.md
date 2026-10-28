---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/jinarerankermodel/additionalweightfiles"
framework: "mlx-swift-lm/MLXLLM"
---

# additionalWeightFiles

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: property  
**Role**: Instance Property

`jinaai/jina-reranker-v3-mlx` keeps the projector in `projector.safetensors`, which neither the conventional `model*.safetensors` names nor `model.safetensors.index.json` select, so it has to be requested by name – as the checkpoint’s own `rerank.py` does.

## Declaration

```swift
var additionalWeightFiles: [String] { get }
```

## Discussion

`jinaai/jina-reranker-v3` packages the same model with the projector in its single `model.safetensors` and ships no such file. A name that is not present is ignored, so the declaration costs that layout nothing.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/jinarerankermodel/additionalweightfiles)*