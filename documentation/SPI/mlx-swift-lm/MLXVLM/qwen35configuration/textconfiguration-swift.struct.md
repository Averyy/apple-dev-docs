---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen35configuration/textconfiguration-swift.struct"
framework: "mlx-swift-lm/MLXVLM"
---

# Qwen35Configuration.TextConfiguration

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct TextConfiguration
```

## Topics

### Initializers
- [init(from: Decoder) throws](./textconfiguration-swift.struct/init%28from%29.md)
### Instance Properties
- [var attentionBias: Bool](./textconfiguration-swift.struct/attentionbias.md)
- [var attentionHeads: Int](./textconfiguration-swift.struct/attentionheads.md)
- [var decoderSparseStep: Int](./textconfiguration-swift.struct/decodersparsestep.md)
- [var fullAttentionInterval: Int](./textconfiguration-swift.struct/fullattentioninterval.md)
- [var headDim: Int?](./textconfiguration-swift.struct/headdim.md)
- [var hiddenLayers: Int](./textconfiguration-swift.struct/hiddenlayers.md)
- [var hiddenSize: Int](./textconfiguration-swift.struct/hiddensize.md)
- [var intermediateSize: Int](./textconfiguration-swift.struct/intermediatesize.md)
- [var kvHeads: Int](./textconfiguration-swift.struct/kvheads.md)
- [var layerTypes: [String]?](./textconfiguration-swift.struct/layertypes.md)
- [var linearConvKernelDim: Int](./textconfiguration-swift.struct/linearconvkerneldim.md)
- [var linearKeyHeadDim: Int](./textconfiguration-swift.struct/linearkeyheaddim.md)
- [var linearNumKeyHeads: Int](./textconfiguration-swift.struct/linearnumkeyheads.md)
- [var linearNumValueHeads: Int](./textconfiguration-swift.struct/linearnumvalueheads.md)
- [var linearValueHeadDim: Int](./textconfiguration-swift.struct/linearvalueheaddim.md)
- [var maxPositionEmbeddings: Int](./textconfiguration-swift.struct/maxpositionembeddings.md)
- [var modelType: String](./textconfiguration-swift.struct/modeltype.md)
- [var moeIntermediateSize: Int](./textconfiguration-swift.struct/moeintermediatesize.md)
- [var mtpNumHiddenLayers: Int](./textconfiguration-swift.struct/mtpnumhiddenlayers.md)
- [var mtpUseDedicatedEmbeddings: Bool](./textconfiguration-swift.struct/mtpusededicatedembeddings.md)
- [var normTopkProb: Bool](./textconfiguration-swift.struct/normtopkprob.md)
- [var numExperts: Int](./textconfiguration-swift.struct/numexperts.md)
- [var numExpertsPerTok: Int](./textconfiguration-swift.struct/numexpertspertok.md)
- [var partialRotaryFactor: Float](./textconfiguration-swift.struct/partialrotaryfactor.md)
- [var rmsNormEps: Float](./textconfiguration-swift.struct/rmsnormeps.md)
- [var ropeParameters: [String : StringOrNumber]?](./textconfiguration-swift.struct/ropeparameters.md)
- [var ropeTheta: Float](./textconfiguration-swift.struct/ropetheta.md)
- [var sharedExpertIntermediateSize: Int](./textconfiguration-swift.struct/sharedexpertintermediatesize.md)
- [var tieWordEmbeddings: Bool](./textconfiguration-swift.struct/tiewordembeddings.md)
- [var vocabularySize: Int](./textconfiguration-swift.struct/vocabularysize.md)
### Default Implementations
- [Encodable Implementations](./textconfiguration-swift.struct/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen35configuration/textconfiguration-swift.struct)*