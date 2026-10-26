---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4assistantmaskedembedder/callasfunction(_:tiedembedding:)"
framework: "mlx-swift-lm/MLXVLM"
---

# callAsFunction(_:tiedEmbedding:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Instance Method

Centroid-routed sparse logits. Port of mlx-vlm `MaskedEmbedder.__call__`

## Declaration

```swift
func callAsFunction(_ hiddenStates: MLXArray, tiedEmbedding: Embedding) -> MLXArray
```

#### Discussion

- `_selected_logits` (`masked_embedder.py`): score the `numCentroids` clusters, expand the top-K, score only those tokens against the tied embedding, and scatter back to full vocab with unselected positions pushed below the selected minimum so they lose argmax/softmax. `tiedEmbedding` is the drafter’s tied token embedding *module*, not its raw `.weight`: gathering through the module’s forward returns dense `[N, H]` rows for a plain `Embedding` and dequantized rows for a `QuantizedEmbedding` (whose `.weight` is packed `[vocab, H·bits/32]` and cannot be reshaped to `H`). Every mlx-community E-series drafter ships quantized, so this must handle both.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4assistantmaskedembedder/callasfunction(_:tiedembedding:))*