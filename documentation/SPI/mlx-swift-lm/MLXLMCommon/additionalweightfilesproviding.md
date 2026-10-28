---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/additionalweightfilesproviding"
framework: "mlx-swift-lm/MLXLMCommon"
---

# AdditionalWeightFilesProviding

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Weight files a model needs that no naming convention or `model.safetensors.index.json` selects.

## Declaration

```swift
protocol AdditionalWeightFilesProviding
```

## Overview

A checkpoint can ship weights in a file that neither the conventional `model*.safetensors` names nor its own index cover: `jinaai/jina-reranker-v3-mlx` keeps its reranking head in `projector.safetensors` and maps only the transformer shards in its index, so the head is never read and the model fails to load. The reference implementation has the same gap and closes it the same way – the checkpoint’s `rerank.py` loads that file by name.

Conform a model to this protocol to name those files. Being explicit rather than widening the selection is what keeps unrelated weights out: a stray tensor whose name a model’s `sanitize(weights:)` rewrites is loaded silently rather than reported.

## Topics

### Instance Properties
- [var additionalWeightFiles: [String]](./additionalweightfilesproviding/additionalweightfiles.md)
  File names, relative to the model directory.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/additionalweightfilesproviding)*