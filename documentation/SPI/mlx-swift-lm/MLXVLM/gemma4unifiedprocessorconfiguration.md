---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4unifiedprocessorconfiguration"
framework: "mlx-swift-lm/MLXVLM"
---

# Gemma4UnifiedProcessorConfiguration

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct Gemma4UnifiedProcessorConfiguration
```

## Topics

### Initializers
- [init(from: any Swift.Decoder) throws](./gemma4unifiedprocessorconfiguration/init%28from%29.md)
### Instance Properties
- [let audioMsPerToken: Int](./gemma4unifiedprocessorconfiguration/audiomspertoken.md)
- [let audioSeqLength: Int](./gemma4unifiedprocessorconfiguration/audioseqlength.md)
- [let audioTokenId: Int](./gemma4unifiedprocessorconfiguration/audiotokenid.md)
- [let boiTokenId: Int](./gemma4unifiedprocessorconfiguration/boitokenid.md)
- [let doNormalize: Bool](./gemma4unifiedprocessorconfiguration/donormalize.md)
- [let doRescale: Bool](./gemma4unifiedprocessorconfiguration/dorescale.md)
- [let doResize: Bool](./gemma4unifiedprocessorconfiguration/doresize.md)
- [let eoiTokenId: Int?](./gemma4unifiedprocessorconfiguration/eoitokenid.md)
- [var fixedSize: CGSize](./gemma4unifiedprocessorconfiguration/fixedsize.md)
- [let imageMean: [CGFloat]](./gemma4unifiedprocessorconfiguration/imagemean.md)
- [var imageMeanTuple: (CGFloat, CGFloat, CGFloat)](./gemma4unifiedprocessorconfiguration/imagemeantuple.md)
- [let imageSeqLength: Int](./gemma4unifiedprocessorconfiguration/imageseqlength.md)
- [let imageStd: [CGFloat]](./gemma4unifiedprocessorconfiguration/imagestd.md)
- [var imageStdTuple: (CGFloat, CGFloat, CGFloat)](./gemma4unifiedprocessorconfiguration/imagestdtuple.md)
- [let imageTokenId: Int](./gemma4unifiedprocessorconfiguration/imagetokenid.md)
- [let maxSoftTokens: Int](./gemma4unifiedprocessorconfiguration/maxsofttokens.md)
- [let modelPatchSize: Int](./gemma4unifiedprocessorconfiguration/modelpatchsize.md)
- [let patchSize: Int](./gemma4unifiedprocessorconfiguration/patchsize.md)
- [let poolingKernelSize: Int](./gemma4unifiedprocessorconfiguration/poolingkernelsize.md)
- [let processorClass: String](./gemma4unifiedprocessorconfiguration/processorclass.md)
- [let rescaleFactor: CGFloat](./gemma4unifiedprocessorconfiguration/rescalefactor.md)
- [let size: Gemma3ProcessorConfiguration.ImageSize?](./gemma4unifiedprocessorconfiguration/size.md)
- [let videoTokenId: Int?](./gemma4unifiedprocessorconfiguration/videotokenid.md)
### Instance Methods
- [func aspectRatioPreservingSize(for: CGSize) throws -> CGSize](./gemma4unifiedprocessorconfiguration/aspectratiopreservingsize%28for%29.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4unifiedprocessorconfiguration)*