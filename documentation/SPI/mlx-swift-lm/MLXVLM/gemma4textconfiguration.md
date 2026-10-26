---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4textconfiguration"
framework: "mlx-swift-lm/MLXVLM"
---

# Gemma4TextConfiguration

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct Gemma4TextConfiguration
```

## Topics

### Initializers
- [init(from: any Swift.Decoder) throws](./gemma4textconfiguration/init%28from%29.md)
### Instance Properties
- [let attentionHeads: Int](./gemma4textconfiguration/attentionheads.md)
- [let attentionKEqV: Bool](./gemma4textconfiguration/attentionkeqv.md)
- [let enableMoEBlock: Bool](./gemma4textconfiguration/enablemoeblock.md)
- [let finalLogitSoftcapping: Float?](./gemma4textconfiguration/finallogitsoftcapping.md)
- [let globalHeadDim: Int](./gemma4textconfiguration/globalheaddim.md)
- [let globalKVHeads: Int?](./gemma4textconfiguration/globalkvheads.md)
- [let headDim: Int](./gemma4textconfiguration/headdim.md)
- [let hiddenLayers: Int](./gemma4textconfiguration/hiddenlayers.md)
- [let hiddenSize: Int](./gemma4textconfiguration/hiddensize.md)
- [let hiddenSizePerLayerInput: Int](./gemma4textconfiguration/hiddensizeperlayerinput.md)
- [let intermediateSize: Int](./gemma4textconfiguration/intermediatesize.md)
- [let kvHeads: Int](./gemma4textconfiguration/kvheads.md)
- [let layerTypes: [String]](./gemma4textconfiguration/layertypes.md)
- [let maxPositionEmbeddings: Int](./gemma4textconfiguration/maxpositionembeddings.md)
- [let modelType: String](./gemma4textconfiguration/modeltype.md)
- [let moeIntermediateSize: Int?](./gemma4textconfiguration/moeintermediatesize.md)
- [let numExperts: Int?](./gemma4textconfiguration/numexperts.md)
- [let numKVSharedLayers: Int](./gemma4textconfiguration/numkvsharedlayers.md)
- [let rmsNormEps: Float](./gemma4textconfiguration/rmsnormeps.md)
- [let ropeParameters: [String : [String : StringOrNumber]]](./gemma4textconfiguration/ropeparameters.md)
- [let ropeTraditional: Bool](./gemma4textconfiguration/ropetraditional.md)
- [let slidingWindow: Int](./gemma4textconfiguration/slidingwindow.md)
- [let slidingWindowPattern: Int](./gemma4textconfiguration/slidingwindowpattern.md)
- [let tieWordEmbeddings: Bool](./gemma4textconfiguration/tiewordembeddings.md)
- [let topKExperts: Int?](./gemma4textconfiguration/topkexperts.md)
- [let useBidirectionalAttention: String?](./gemma4textconfiguration/usebidirectionalattention.md)
- [let useDoubleWideMLP: Bool](./gemma4textconfiguration/usedoublewidemlp.md)
- [let vocabularySize: Int](./gemma4textconfiguration/vocabularysize.md)
- [let vocabularySizePerLayerInput: Int](./gemma4textconfiguration/vocabularysizeperlayerinput.md)
### Default Implementations
- [Encodable Implementations](./gemma4textconfiguration/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4textconfiguration)*