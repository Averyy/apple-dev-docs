---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/gemma3configuration"
framework: "mlx-swift-lm/MLXEmbedders"
---

# Gemma3Configuration

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: struct  
**Role**: Structure

Configuration for the Gemma 3 model.

## Declaration

```swift
struct Gemma3Configuration
```

## Overview

This structure holds all the hyperparameters required to initialize a `Gemma3ModelBackbone` or an `EmbeddingGemma` model. It supports decoding from standard `config.json` files, including those nested under a `text_config` key.

## Topics

### Initializers
- [init(from: Decoder) throws](./gemma3configuration/init%28from%29.md)
  Initializes a configuration by decoding from the given decoder.
### Instance Properties
- [let attentionHeads: Int](./gemma3configuration/attentionheads.md)
  The number of attention heads.
- [let headDim: Int](./gemma3configuration/headdim.md)
  The dimensionality of each attention head.
- [let hiddenLayers: Int](./gemma3configuration/hiddenlayers.md)
  The number of hidden layers in the transformer.
- [let hiddenSize: Int](./gemma3configuration/hiddensize.md)
  The size of the hidden embeddings.
- [let intermediateSize: Int](./gemma3configuration/intermediatesize.md)
  The dimensionality of the intermediate (feed-forward) layer.
- [let kvHeads: Int](./gemma3configuration/kvheads.md)
  The number of key-value heads for Grouped Query Attention.
- [let maxPositionEmbeddings: Int](./gemma3configuration/maxpositionembeddings.md)
  The maximum sequence length supported by the model.
- [let modelType: String](./gemma3configuration/modeltype.md)
  The architecture identifier (e.g., “gemma3”).
- [let queryPreAttnScalar: Float](./gemma3configuration/querypreattnscalar.md)
  The scalar value used to scale queries before attention.
- [let rmsNormEps: Float](./gemma3configuration/rmsnormeps.md)
  The epsilon value for RMSNorm layers.
- [let ropeLocalBaseFreq: Float](./gemma3configuration/ropelocalbasefreq.md)
  The base frequency for RoPE in sliding window layers.
- [let ropeScaling: [String : StringOrNumber]?](./gemma3configuration/ropescaling.md)
  Optional scaling configuration for RoPE.
- [let ropeTheta: Float](./gemma3configuration/ropetheta.md)
  The base frequency for Rotary Positional Embeddings (RoPE) in global layers.
- [let ropeTraditional: Bool](./gemma3configuration/ropetraditional.md)
  Whether to use traditional RoPE (interleaved) or standard ordering.
- [let slidingWindow: Int](./gemma3configuration/slidingwindow.md)
  The size of the sliding window for attention.
- [let slidingWindowPattern: Int](./gemma3configuration/slidingwindowpattern.md)
  The pattern determining which layers use sliding window vs. global attention.
- [let useBidirectionalAttention: Bool](./gemma3configuration/usebidirectionalattention.md)
  Whether attention is bidirectional, as in EmbeddingGemma. When `true`, sliding layers see `slidingWindow / 2` tokens on each side; when `false`, the layers are causal.
- [let vocabularySize: Int](./gemma3configuration/vocabularysize.md)
  The size of the vocabulary.
### Default Implementations
- [Encodable Implementations](./gemma3configuration/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/gemma3configuration)*