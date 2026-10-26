---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4assistantmaskedembedder"
framework: "mlx-swift-lm/MLXVLM"
---

# Gemma4AssistantMaskedEmbedder

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

Centroid-routed sparse LM head used when `use_ordered_embeddings=true`.

## Declaration

```swift
final class Gemma4AssistantMaskedEmbedder
```

#### Overview

Mirrors mlx-vlm’s `mlx_vlm/speculative/drafters/gemma4_assistant/masked_embedder.py`.

The E-series drafters (`gemma-4-E2B/E4B-it-assistant-bf16`) ship `use_ordered_embeddings=true` and route their logits through this head; the 26B-A4B/31B drafters ship `false` and use the tied `lm_head` matmul instead. The forward is pinned against an independent dense reference by `testMaskedEmbedderSelectedLogitsMatchDense` (no checkpoint required) and exercised end-to-end by the `TEST_E{2,4}B_PAIR`-gated integration tests.

## Topics

### Initializers
- [init(config: Gemma4AssistantConfiguration)](./gemma4assistantmaskedembedder/init%28config%29.md)
### Instance Properties
- [var centroids: Linear](./gemma4assistantmaskedembedder/centroids.md)
- [let hiddenSize: Int](./gemma4assistantmaskedembedder/hiddensize.md)
- [let numCentroids: Int](./gemma4assistantmaskedembedder/numcentroids.md)
- [var tokenOrdering: MLXArray](./gemma4assistantmaskedembedder/tokenordering.md)
- [let topK: Int](./gemma4assistantmaskedembedder/topk.md)
- [let vocabSize: Int](./gemma4assistantmaskedembedder/vocabsize.md)
- [let vocabSizePerCentroid: Int](./gemma4assistantmaskedembedder/vocabsizepercentroid.md)
### Instance Methods
- [func callAsFunction(MLXArray, tiedEmbedding: Embedding) -> MLXArray](./gemma4assistantmaskedembedder/callasfunction%28_,tiedembedding%29.md)
  Centroid-routed sparse logits. Port of mlx-vlm `MaskedEmbedder.__call__`

## Relationships

### Inherits From
- MLXNN.Module
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4assistantmaskedembedder)*