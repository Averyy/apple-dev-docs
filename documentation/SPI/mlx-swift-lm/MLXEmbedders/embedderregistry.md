---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embedderregistry"
framework: "mlx-swift-lm/MLXEmbedders"
---

# EmbedderRegistry

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: class  
**Role**: Class

Registry of known embedder model configurations.

## Declaration

```swift
class EmbedderRegistry
```

## Topics

### Type Properties
- [static let bge_base: ModelConfiguration](./embedderregistry/bge_base.md)
  BGE Base en v1.5.
- [static let bge_large: ModelConfiguration](./embedderregistry/bge_large.md)
  BGE Large en v1.5.
- [static let bge_m3: ModelConfiguration](./embedderregistry/bge_m3.md)
  BGE-M3 - Multi-lingual, Multi-functional, Multi-granularity.
- [static let bge_micro: ModelConfiguration](./embedderregistry/bge_micro.md)
  BGE Micro v2 (TaylorAI) - optimized for extremely low latency.
- [static let bge_reranker_v2_m3: ModelConfiguration](./embedderregistry/bge_reranker_v2_m3.md)
  BGE Reranker v2 M3 - multilingual encoder reranker.
- [static let bge_small: ModelConfiguration](./embedderregistry/bge_small.md)
  BGE Small en v1.5.
- [static let embeddinggemma2: ModelConfiguration](./embedderregistry/embeddinggemma2.md)
  EmbeddingGemma 2 with text, vision, and audio weights in bfloat16.
- [static let gte_tiny: ModelConfiguration](./embedderregistry/gte_tiny.md)
  GTE Tiny - a small, efficient embedding model.
- [static let lfm2_colbert_350m: ModelConfiguration](./embedderregistry/lfm2_colbert_350m.md)
  LFM2.5 ColBERT 350M — per-token 128-d multi-vectors (MaxSim late interaction).
- [static let lfm2_colbert_350m_4bit: ModelConfiguration](./embedderregistry/lfm2_colbert_350m_4bit.md)
  LFM2.5 ColBERT 350M — 4-bit quantized.
- [static let lfm2_colbert_350m_8bit: ModelConfiguration](./embedderregistry/lfm2_colbert_350m_8bit.md)
  LFM2.5 ColBERT 350M — 8-bit quantized.
- [static let lfm2_embedding_350m: ModelConfiguration](./embedderregistry/lfm2_embedding_350m.md)
  LFM2.5 Embedding 350M — CLS-pooled 1024-d dense vectors (cosine).
- [static let lfm2_embedding_350m_4bit: ModelConfiguration](./embedderregistry/lfm2_embedding_350m_4bit.md)
  LFM2.5 Embedding 350M — 4-bit quantized.
- [static let lfm2_embedding_350m_8bit: ModelConfiguration](./embedderregistry/lfm2_embedding_350m_8bit.md)
  LFM2.5 Embedding 350M — 8-bit quantized.
- [static let minilm_l12: ModelConfiguration](./embedderregistry/minilm_l12.md)
  MiniLM-L12 - a more accurate version of MiniLM.
- [static let minilm_l6: ModelConfiguration](./embedderregistry/minilm_l6.md)
  MiniLM-L6 - the industry-standard small embedding model.
- [static let mixedbread_large: ModelConfiguration](./embedderregistry/mixedbread_large.md)
  Mixedbread AI Large v1.
- [static let multilingual_e5_small: ModelConfiguration](./embedderregistry/multilingual_e5_small.md)
  Multilingual E5 Small - supports over 100 languages.
- [static let nomic_text_v1: ModelConfiguration](./embedderregistry/nomic_text_v1.md)
  Nomic Embed Text v1.
- [static let nomic_text_v1_5: ModelConfiguration](./embedderregistry/nomic_text_v1_5.md)
  Nomic Embed Text v1.5 - supports Matryoshka embeddings.
- [static let qwen3_embedding: ModelConfiguration](./embedderregistry/qwen3_embedding.md)
  Qwen3 Embedding 0.6B - 4-bit quantized version.
- [static let shared: EmbedderRegistry](./embedderregistry/shared.md)
  Shared instance with default model configurations.
- [static let snowflake_lg: ModelConfiguration](./embedderregistry/snowflake_lg.md)
  Snowflake Arctic Embed L.
- [static let snowflake_xs: ModelConfiguration](./embedderregistry/snowflake_xs.md)
  Snowflake Arctic Embed XS.

## Relationships

### Inherits From
- MLXLMCommon.AbstractModelRegistry
### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embedderregistry)*