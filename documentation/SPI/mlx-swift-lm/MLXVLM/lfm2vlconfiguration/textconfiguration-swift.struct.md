---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/lfm2vlconfiguration/textconfiguration-swift.struct"
framework: "mlx-swift-lm/MLXVLM"
---

# LFM2VLConfiguration.TextConfiguration

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct TextConfiguration
```

## Topics

### Initializers
- [init(from: any Decoder) throws](./textconfiguration-swift.struct/init%28from%29.md)
### Instance Properties
- [let attentionHeads: Int](./textconfiguration-swift.struct/attentionheads.md)
- [var blockAutoAdjustFFDim: Bool](./textconfiguration-swift.struct/blockautoadjustffdim.md)
- [var blockDim: Int](./textconfiguration-swift.struct/blockdim.md)
- [var blockFFDim: Int](./textconfiguration-swift.struct/blockffdim.md)
  MLP width before auto-adjustment: `block_ff_dim`, else `intermediate_size`.
- [var blockFFNDimMultiplier: Float](./textconfiguration-swift.struct/blockffndimmultiplier.md)
- [var blockMultipleOf: Int](./textconfiguration-swift.struct/blockmultipleof.md)
- [var convBias: Bool](./textconfiguration-swift.struct/convbias.md)
- [var convLCache: Int](./textconfiguration-swift.struct/convlcache.md)
- [var fullAttnIdxs: [Int]](./textconfiguration-swift.struct/fullattnidxs.md)
- [let hiddenLayers: Int](./textconfiguration-swift.struct/hiddenlayers.md)
- [let hiddenSize: Int](./textconfiguration-swift.struct/hiddensize.md)
- [let kvHeads: Int](./textconfiguration-swift.struct/kvheads.md)
- [let modelType: String](./textconfiguration-swift.struct/modeltype.md)
- [var normEps: Float](./textconfiguration-swift.struct/normeps.md)
- [var ropeTheta: Float](./textconfiguration-swift.struct/ropetheta.md)
  `rope_parameters.rope_theta`, else `rope_theta`, else 1e6.
- [let vocabularySize: Int](./textconfiguration-swift.struct/vocabularysize.md)
### Default Implementations
- [Encodable Implementations](./textconfiguration-swift.struct/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/lfm2vlconfiguration/textconfiguration-swift.struct)*