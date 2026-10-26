---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/museglimmerprocessorconfiguration/imageprocessor-swift.struct"
framework: "mlx-swift-lm/MLXVLM"
---

# MuseGlimmerProcessorConfiguration.ImageProcessor

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct ImageProcessor
```

## Topics

### Initializers
- [init(from: Decoder) throws](./imageprocessor-swift.struct/init%28from%29.md)
- [init(patchSize: Int, temporalPatchSize: Int, mergeSize: Int, maxImageTokens: Int, imageMean: [CGFloat], imageStd: [CGFloat])](./imageprocessor-swift.struct/init%28patchsize,temporalpatchsize,mergesize,maximagetokens,imagemean,imagestd%29.md)
  Builds a configuration in code, chiefly so a caller can lower [`maxImageTokens`](./imageprocessor-swift.struct/maximagetokens.md) from the checkpoint’s 4096. See the note in [`preprocess(image:processing:)`](../museglimmerprocessor/preprocess%28image,processing%29.md) on why that budget dominates time-to-first-token.
### Instance Properties
- [let imageMean: [CGFloat]](./imageprocessor-swift.struct/imagemean.md)
- [var imageMeanTuple: (CGFloat, CGFloat, CGFloat)](./imageprocessor-swift.struct/imagemeantuple.md)
- [let imageStd: [CGFloat]](./imageprocessor-swift.struct/imagestd.md)
- [var imageStdTuple: (CGFloat, CGFloat, CGFloat)](./imageprocessor-swift.struct/imagestdtuple.md)
- [let maxImageTokens: Int](./imageprocessor-swift.struct/maximagetokens.md)
- [let mergeSize: Int](./imageprocessor-swift.struct/mergesize.md)
- [let patchSize: Int](./imageprocessor-swift.struct/patchsize.md)
- [let temporalPatchSize: Int](./imageprocessor-swift.struct/temporalpatchsize.md)
### Default Implementations
- [Encodable Implementations](./imageprocessor-swift.struct/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/museglimmerprocessorconfiguration/imageprocessor-swift.struct)*