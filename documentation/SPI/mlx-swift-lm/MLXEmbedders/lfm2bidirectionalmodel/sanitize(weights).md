---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/lfm2bidirectionalmodel/sanitize(weights:)"
framework: "mlx-swift-lm/MLXEmbedders"
---

# sanitize(weights:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: method  
**Role**: Instance Method

Weights from `convert.py` are already `model.`-prefixed (and the ColBERT head is the bare key `dense.weight`), so this only applies the depthwise Conv1d transpose guard — `(O, 1, K)` -> `(O, K, 1)` — for robustness against weights re-converted straight from Hugging Face. It must NOT blanket-prepend `model.` (that would corrupt `dense.weight`).

## Declaration

```swift
func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/lfm2bidirectionalmodel/sanitize(weights:))*