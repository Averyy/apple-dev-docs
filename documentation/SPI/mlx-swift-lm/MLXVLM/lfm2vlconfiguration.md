---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/lfm2vlconfiguration"
framework: "mlx-swift-lm/MLXVLM"
---

# LFM2VLConfiguration

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

Configuration for [`LFM2VL`](./lfm2vl.md)

## Declaration

```swift
struct LFM2VLConfiguration
```

## Topics

### Structures
- [LFM2VLConfiguration.TextConfiguration](./lfm2vlconfiguration/textconfiguration-swift.struct.md)
- [LFM2VLConfiguration.VisionConfiguration](./lfm2vlconfiguration/visionconfiguration-swift.struct.md)
### Initializers
- [init(from: any Decoder) throws](./lfm2vlconfiguration/init%28from%29.md)
### Instance Properties
- [var doImageSplitting: Bool](./lfm2vlconfiguration/doimagesplitting.md)
- [var downsampleFactor: Int](./lfm2vlconfiguration/downsamplefactor.md)
- [var imageTokenIndex: Int](./lfm2vlconfiguration/imagetokenindex.md)
- [var maxImageTokens: Int](./lfm2vlconfiguration/maximagetokens.md)
- [var maxNumPatches: Int](./lfm2vlconfiguration/maxnumpatches.md)
- [var minImageTokens: Int](./lfm2vlconfiguration/minimagetokens.md)
- [var minTiles: Int](./lfm2vlconfiguration/mintiles.md)
- [let modelType: String](./lfm2vlconfiguration/modeltype.md)
- [var projectorBias: Bool](./lfm2vlconfiguration/projectorbias.md)
- [var projectorHiddenSize: Int](./lfm2vlconfiguration/projectorhiddensize.md)
- [var projectorUseLayernorm: Bool](./lfm2vlconfiguration/projectoruselayernorm.md)
- [let textConfiguration: TextConfiguration](./lfm2vlconfiguration/textconfiguration-swift.property.md)
- [var useThumbnail: Bool](./lfm2vlconfiguration/usethumbnail.md)
- [let visionConfiguration: VisionConfiguration](./lfm2vlconfiguration/visionconfiguration-swift.property.md)
- [var visionFeatureLayer: Int](./lfm2vlconfiguration/visionfeaturelayer.md)
  Which vision encoder layer to use for features. -1 means use all layers (default).
### Default Implementations
- [Encodable Implementations](./lfm2vlconfiguration/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/lfm2vlconfiguration)*