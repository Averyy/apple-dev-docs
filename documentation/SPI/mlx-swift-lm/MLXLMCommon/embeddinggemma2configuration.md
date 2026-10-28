---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/embeddinggemma2configuration"
framework: "mlx-swift-lm/MLXLMCommon"
---

# EmbeddingGemma2Configuration

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Configuration of `google/embeddinggemma-2` (`model_type: embedding_gemma2`).

## Declaration

```swift
struct EmbeddingGemma2Configuration
```

## Overview

Decodes the checkpoint’s `config.json` directly, including the nested `text_config` and the optional `vision_config` and `audio_config`.

## Topics

### Structures
- [EmbeddingGemma2Configuration.Attention](./embeddinggemma2configuration/attention-swift.struct.md)
  One attention head layout per layer: global layers use larger heads and one key/value head.
### Initializers
- [init(from: any Decoder) throws](./embeddinggemma2configuration/init%28from%29.md)
### Instance Properties
- [let attention: [Attention]](./embeddinggemma2configuration/attention-swift.property.md)
- [let attentionHeads: Int](./embeddinggemma2configuration/attentionheads.md)
- [let embeddingDim: Int](./embeddinggemma2configuration/embeddingdim.md)
- [let headDim: Int](./embeddinggemma2configuration/headdim.md)
- [let hiddenLayers: Int](./embeddinggemma2configuration/hiddenlayers.md)
- [let hiddenSize: Int](./embeddinggemma2configuration/hiddensize.md)
- [let intermediateSize: Int](./embeddinggemma2configuration/intermediatesize.md)
- [let kvHeads: Int](./embeddinggemma2configuration/kvheads.md)
- [let layerTypes: [String]](./embeddinggemma2configuration/layertypes.md)
- [let perLayerInputSize: Int](./embeddinggemma2configuration/perlayerinputsize.md)
- [let rmsNormEps: Float](./embeddinggemma2configuration/rmsnormeps.md)
- [let slidingWindow: Int](./embeddinggemma2configuration/slidingwindow.md)
  Radius: a token sees the keys within this distance on both sides.
- [var softTokenIDs: [Int]](./embeddinggemma2configuration/softtokenids.md)
  The image, video and audio placeholders that soft tokens replace.
- [let vocabularySize: Int](./embeddinggemma2configuration/vocabularysize.md)
### Instance Methods
- [func encode(to: any Encoder) throws](./embeddinggemma2configuration/encode%28to%29.md)
- [func selectingEncoders(vision: Bool, audio: Bool) -> EmbeddingGemma2Configuration](./embeddinggemma2configuration/selectingencoders%28vision,audio%29.md)
  Returns a configuration that omits unused modality encoders before weights load.
### Type Properties
- [static let contextLength: Int](./embeddinggemma2configuration/contextlength.md)
  Context window from the model card. `max_position_embeddings` is the RoPE table size, not a usable limit.
### Default Implementations
- [Encodable Implementations](./embeddinggemma2configuration/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/embeddinggemma2configuration)*