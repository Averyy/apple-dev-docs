---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/museglimmertextconfiguration"
framework: "mlx-swift-lm/MLXVLM"
---

# MuseGlimmerTextConfiguration

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct MuseGlimmerTextConfiguration
```

## Topics

### Initializers
- [init(from: Decoder) throws](./museglimmertextconfiguration/init%28from%29.md)
### Instance Properties
- [let attentionBias: Bool](./museglimmertextconfiguration/attentionbias.md)
- [let attentionHeads: Int](./museglimmertextconfiguration/attentionheads.md)
- [let finalLogitSoftcapping: Float](./museglimmertextconfiguration/finallogitsoftcapping.md)
- [let headDimensions: Int](./museglimmertextconfiguration/headdimensions.md)
- [let hiddenLayers: Int](./museglimmertextconfiguration/hiddenlayers.md)
- [let hiddenSize: Int](./museglimmertextconfiguration/hiddensize.md)
- [let intermediateSize: Int](./museglimmertextconfiguration/intermediatesize.md)
- [let kvHeads: Int](./museglimmertextconfiguration/kvheads.md)
- [let layerRopeTheta: [Float]](./museglimmertextconfiguration/layerropetheta.md)
  Per-layer RoPE base. A value of `0` means the layer is NoPE — see `MuseGlimmerTextAttention`.
- [let layerTypes: [String]](./museglimmertextconfiguration/layertypes.md)
  Per-layer attention kind: `sliding_attention` or `full_attention`.
- [let maxPositionEmbeddings: Int](./museglimmertextconfiguration/maxpositionembeddings.md)
- [let modelType: String](./museglimmertextconfiguration/modeltype.md)
- [let outputMultiplier: Float](./museglimmertextconfiguration/outputmultiplier.md)
- [let postNormEps: Float](./museglimmertextconfiguration/postnormeps.md)
- [let qkScaleFactor: Float](./museglimmertextconfiguration/qkscalefactor.md)
- [let rmsNormEps: Float](./museglimmertextconfiguration/rmsnormeps.md)
- [let ropeParameters: [String : StringOrNumber]?](./museglimmertextconfiguration/ropeparameters.md)
- [var ropeTheta: Float](./museglimmertextconfiguration/ropetheta.md)
  Fallback theta used only to construct the (unused) RoPE on NoPE layers.
- [let slidingWindow: Int](./museglimmertextconfiguration/slidingwindow.md)
- [let tieWordEmbeddings: Bool](./museglimmertextconfiguration/tiewordembeddings.md)
- [let vocabularySize: Int](./museglimmertextconfiguration/vocabularysize.md)
### Default Implementations
- [Encodable Implementations](./museglimmertextconfiguration/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/museglimmertextconfiguration)*