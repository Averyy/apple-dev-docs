---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen35textconfiguration"
framework: "mlx-swift-lm/MLXLLM"
---

# Qwen35TextConfiguration

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct Qwen35TextConfiguration
```

## Topics

### Initializers
- [init(from: Decoder) throws](./qwen35textconfiguration/init%28from%29.md)
### Instance Properties
- [var attentionHeads: Int](./qwen35textconfiguration/attentionheads.md)
- [var headDim: Int?](./qwen35textconfiguration/headdim.md)
- [var hiddenLayers: Int](./qwen35textconfiguration/hiddenlayers.md)
- [var hiddenSize: Int](./qwen35textconfiguration/hiddensize.md)
- [var intermediateSize: Int](./qwen35textconfiguration/intermediatesize.md)
- [var kvHeads: Int](./qwen35textconfiguration/kvheads.md)
- [var linearConvKernelDim: Int](./qwen35textconfiguration/linearconvkerneldim.md)
- [var linearKeyHeadDim: Int](./qwen35textconfiguration/linearkeyheaddim.md)
- [var linearNumKeyHeads: Int](./qwen35textconfiguration/linearnumkeyheads.md)
- [var linearNumValueHeads: Int](./qwen35textconfiguration/linearnumvalueheads.md)
- [var linearValueHeadDim: Int](./qwen35textconfiguration/linearvalueheaddim.md)
- [var moeIntermediateSize: Int](./qwen35textconfiguration/moeintermediatesize.md)
- [var mtpNumHiddenLayers: Int](./qwen35textconfiguration/mtpnumhiddenlayers.md)
- [var numExperts: Int](./qwen35textconfiguration/numexperts.md)
- [var numExpertsPerTok: Int](./qwen35textconfiguration/numexpertspertok.md)
- [var resolvedLayerTypes: [String]](./qwen35textconfiguration/resolvedlayertypes.md)
  The attention kind of each layer, `"linear_attention"` or `"full_attention"`.
- [var sharedExpertIntermediateSize: Int](./qwen35textconfiguration/sharedexpertintermediatesize.md)
- [var vocabularySize: Int](./qwen35textconfiguration/vocabularysize.md)
### Default Implementations
- [Encodable Implementations](./qwen35textconfiguration/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen35textconfiguration)*