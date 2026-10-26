---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/lfm2bidirectionalconfiguration"
framework: "mlx-swift-lm/MLXEmbedders"
---

# LFM2BidirectionalConfiguration

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct LFM2BidirectionalConfiguration
```

## Topics

### Structures
- [LFM2BidirectionalConfiguration.MLXHead](./lfm2bidirectionalconfiguration/mlxhead.md)
  The custom `"mlx"` block that selects the retrieval head and carries the prompt/prefix conventions used by callers (the library does not inject them).
### Initializers
- [init(from: Decoder) throws](./lfm2bidirectionalconfiguration/init%28from%29.md)
### Instance Properties
- [var attnLayerIdxs: [Int]](./lfm2bidirectionalconfiguration/attnlayeridxs.md)
  Indices of the `full_attention` layers (the rest are short-conv layers).
- [let blockAutoAdjustFFDim: Bool](./lfm2bidirectionalconfiguration/blockautoadjustffdim.md)
- [let blockFFDim: Int](./lfm2bidirectionalconfiguration/blockffdim.md)
- [let blockFFNDimMultiplier: Float](./lfm2bidirectionalconfiguration/blockffndimmultiplier.md)
- [let blockMultipleOf: Int](./lfm2bidirectionalconfiguration/blockmultipleof.md)
- [let convBias: Bool](./lfm2bidirectionalconfiguration/convbias.md)
- [let convLCache: Int](./lfm2bidirectionalconfiguration/convlcache.md)
- [var headDim: Int](./lfm2bidirectionalconfiguration/headdim.md)
- [let hiddenSize: Int](./lfm2bidirectionalconfiguration/hiddensize.md)
- [let layerTypes: [String]](./lfm2bidirectionalconfiguration/layertypes.md)
- [let maxPositionEmbeddings: Int?](./lfm2bidirectionalconfiguration/maxpositionembeddings.md)
- [let mlx: MLXHead](./lfm2bidirectionalconfiguration/mlx.md)
- [let normEps: Float](./lfm2bidirectionalconfiguration/normeps.md)
- [let numAttentionHeads: Int](./lfm2bidirectionalconfiguration/numattentionheads.md)
- [let numHiddenLayers: Int](./lfm2bidirectionalconfiguration/numhiddenlayers.md)
- [let numKeyValueHeads: Int](./lfm2bidirectionalconfiguration/numkeyvalueheads.md)
- [let ropeTheta: Float](./lfm2bidirectionalconfiguration/ropetheta.md)
- [let vocabSize: Int](./lfm2bidirectionalconfiguration/vocabsize.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/lfm2bidirectionalconfiguration)*