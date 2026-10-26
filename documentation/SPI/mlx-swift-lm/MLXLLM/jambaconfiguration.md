---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/jambaconfiguration"
framework: "mlx-swift-lm/MLXLLM"
---

# JambaConfiguration

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct JambaConfiguration
```

## Topics

### Initializers
- [init(from: Decoder) throws](./jambaconfiguration/init%28from%29.md)
### Instance Properties
- [var attnLayerOffset: Int](./jambaconfiguration/attnlayeroffset.md)
- [var attnLayerPeriod: Int](./jambaconfiguration/attnlayerperiod.md)
- [var expertLayerOffset: Int](./jambaconfiguration/expertlayeroffset.md)
- [var expertLayerPeriod: Int](./jambaconfiguration/expertlayerperiod.md)
- [var hiddenSize: Int](./jambaconfiguration/hiddensize.md)
- [var intermediateSize: Int](./jambaconfiguration/intermediatesize.md)
- [var layersBlockType: [String]?](./jambaconfiguration/layersblocktype.md)
- [var mambaConvBias: Bool](./jambaconfiguration/mambaconvbias.md)
- [var mambaDConv: Int](./jambaconfiguration/mambadconv.md)
- [var mambaDState: Int](./jambaconfiguration/mambadstate.md)
- [var mambaDtRank: Int?](./jambaconfiguration/mambadtrank.md)
- [var mambaExpand: Int](./jambaconfiguration/mambaexpand.md)
- [var mambaProjBias: Bool](./jambaconfiguration/mambaprojbias.md)
- [var maxPositionEmbeddings: Int](./jambaconfiguration/maxpositionembeddings.md)
- [var modelType: String](./jambaconfiguration/modeltype.md)
- [var numAttentionHeads: Int](./jambaconfiguration/numattentionheads.md)
- [var numExperts: Int](./jambaconfiguration/numexperts.md)
- [var numExpertsPerTok: Int](./jambaconfiguration/numexpertspertok.md)
- [var numHiddenLayers: Int](./jambaconfiguration/numhiddenlayers.md)
- [var numKeyValueHeads: Int](./jambaconfiguration/numkeyvalueheads.md)
- [var rmsNormEps: Float](./jambaconfiguration/rmsnormeps.md)
- [var tieWordEmbeddings: Bool](./jambaconfiguration/tiewordembeddings.md)
- [var vocabSize: Int](./jambaconfiguration/vocabsize.md)
### Default Implementations
- [Encodable Implementations](./jambaconfiguration/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/jambaconfiguration)*