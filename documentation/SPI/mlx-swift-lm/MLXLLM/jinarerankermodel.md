---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/jinarerankermodel"
framework: "mlx-swift-lm/MLXLLM"
---

# JinaRerankerModel

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: class  
**Role**: Class

Jina reranker v3 listwise model.

## Declaration

```swift
final class JinaRerankerModel
```

## Overview

The checkpoint declares `model_type: qwen3` but `architectures: ["JinaForRanking"]`. It uses Qwen3 hidden states at `<|embed_token|>` and `<|rerank_token|>` positions, projects them with `projector.safetensors`, then scores documents by cosine similarity.

## Topics

### Initializers
- [init(Qwen3Configuration)](./jinarerankermodel/init%28_%29.md)
### Instance Properties
- [var additionalWeightFiles: [String]](./jinarerankermodel/additionalweightfiles.md)
  `jinaai/jina-reranker-v3-mlx` keeps the projector in `projector.safetensors`, which neither the conventional `model*.safetensors` names nor `model.safetensors.index.json` select, so it has to be requested by name – as the checkpoint’s own `rerank.py` does.
- [let kvHeads: [Int]](./jinarerankermodel/kvheads.md)
- [let vocabularySize: Int](./jinarerankermodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./jinarerankermodel/callasfunction%28_,cache%29.md)
- [func callAsFunction(LMInput.Text, cache: [KVCache]?, state: LMOutput.State?) -> LMOutput](./jinarerankermodel/callasfunction%28_,cache,state%29.md)
- [func prepare(LMInput, cache: [KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./jinarerankermodel/prepare%28_,cache,state,prefill%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./jinarerankermodel/sanitize%28weights%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./jinarerankermodel/baselanguagemodel-implementations.md)
- [ChatConventionsProviding Implementations](./jinarerankermodel/chatconventionsproviding-implementations.md)
- [LanguageModel Implementations](./jinarerankermodel/languagemodel-implementations.md)

## Relationships

### Inherits From
- MLXNN.Module
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXLMCommon.AdditionalWeightFilesProviding
- MLXLMCommon.BaseLanguageModel
- MLXLMCommon.ChatConventionsProviding
- MLXLMCommon.KVCacheDimensionProvider
- MLXLMCommon.LanguageModel
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/jinarerankermodel)*