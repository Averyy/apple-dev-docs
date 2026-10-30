---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nemotronhconfiguration"
framework: "mlx-swift-lm/MLXLLM"
---

# NemotronHConfiguration

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct NemotronHConfiguration
```

## Topics

### Initializers
- [init(from: Decoder) throws](./nemotronhconfiguration/init%28from%29.md)
- [init(vocabSize: Int, hiddenSize: Int, numHiddenLayers: Int, numAttentionHeads: Int, numKeyValueHeads: Int, mambaNumHeads: Int, mambaHeadDim: Int, ssmStateSize: Int, convKernel: Int, nGroups: Int, intermediateSize: Int, moeIntermediateSize: Int, moeSharedExpertIntermediateSize: Int, nRoutedExperts: Int, numExpertsPerTok: Int, hybridOverridePattern: String, layerNormEpsilon: Float, attentionBias: Bool, mambaProjBias: Bool, mlpBias: Bool, useBias: Bool, useConvBias: Bool, tieWordEmbeddings: Bool, ropeTheta: Float, headDim: Int?, nSharedExperts: Int?, nGroup: Int, topkGroup: Int, normTopkProb: Bool, routedScalingFactor: Float, timeStepLimitMin: Float, timeStepLimitMax: Float)](./nemotronhconfiguration/init%28vocabsize_hiddensize_numhiddenlayers_numattentionheads_numkeyvalueheads_mambanumheads_mambaheaddim_ssmstatesize_convkernel_ngroups_intermediatesize_moeintermediatesize_moesharedexpertintermediatesize_nroutedexpert-160d1368.md)
  Memberwise initializer for testing
### Instance Properties
- [var attentionBias: Bool](./nemotronhconfiguration/attentionbias.md)
- [var blockConfigs: [NemotronHBlockConfig]?](./nemotronhconfiguration/blockconfigs.md)
- [var convKernel: Int](./nemotronhconfiguration/convkernel.md)
- [var headDim: Int?](./nemotronhconfiguration/headdim.md)
- [var hiddenSize: Int](./nemotronhconfiguration/hiddensize.md)
- [var hybridOverridePattern: String](./nemotronhconfiguration/hybridoverridepattern.md)
- [var intermediateSize: Int](./nemotronhconfiguration/intermediatesize.md)
- [var layerNormEpsilon: Float](./nemotronhconfiguration/layernormepsilon.md)
- [var mambaHeadDim: Int](./nemotronhconfiguration/mambaheaddim.md)
- [var mambaNumHeads: Int](./nemotronhconfiguration/mambanumheads.md)
- [var mambaProjBias: Bool](./nemotronhconfiguration/mambaprojbias.md)
- [var mlpBias: Bool](./nemotronhconfiguration/mlpbias.md)
- [var modelType: String](./nemotronhconfiguration/modeltype.md)
- [var moeIntermediateSize: Int](./nemotronhconfiguration/moeintermediatesize.md)
- [var moeLatentSize: Int?](./nemotronhconfiguration/moelatentsize.md)
- [var moeSharedExpertIntermediateSize: Int](./nemotronhconfiguration/moesharedexpertintermediatesize.md)
- [var nGroup: Int](./nemotronhconfiguration/ngroup.md)
- [var nGroups: Int](./nemotronhconfiguration/ngroups.md)
- [var nRoutedExperts: Int](./nemotronhconfiguration/nroutedexperts.md)
- [var nSharedExperts: Int?](./nemotronhconfiguration/nsharedexperts.md)
- [var normTopkProb: Bool](./nemotronhconfiguration/normtopkprob.md)
- [var numAttentionHeads: Int](./nemotronhconfiguration/numattentionheads.md)
- [var numExpertsPerTok: Int](./nemotronhconfiguration/numexpertspertok.md)
- [var numHiddenLayers: Int](./nemotronhconfiguration/numhiddenlayers.md)
- [var numKeyValueHeads: Int](./nemotronhconfiguration/numkeyvalueheads.md)
- [var ropeTheta: Float](./nemotronhconfiguration/ropetheta.md)
- [var routedScalingFactor: Float](./nemotronhconfiguration/routedscalingfactor.md)
- [var ssmStateSize: Int](./nemotronhconfiguration/ssmstatesize.md)
- [var tieWordEmbeddings: Bool](./nemotronhconfiguration/tiewordembeddings.md)
- [var timeStepLimitMax: Float](./nemotronhconfiguration/timesteplimitmax.md)
- [var timeStepLimitMin: Float](./nemotronhconfiguration/timesteplimitmin.md)
- [var topkGroup: Int](./nemotronhconfiguration/topkgroup.md)
- [var useBias: Bool](./nemotronhconfiguration/usebias.md)
- [var useConvBias: Bool](./nemotronhconfiguration/useconvbias.md)
- [var vocabSize: Int](./nemotronhconfiguration/vocabsize.md)
### Instance Methods
- [func layerConfiguration(Int) -> NemotronHConfiguration](./nemotronhconfiguration/layerconfiguration%28_%29.md)
  The configuration for layer `index`, with any `block_configs` overrides applied.
### Default Implementations
- [Encodable Implementations](./nemotronhconfiguration/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/nemotronhconfiguration)*