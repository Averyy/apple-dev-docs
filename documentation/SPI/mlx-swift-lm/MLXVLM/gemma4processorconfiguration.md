---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4processorconfiguration"
framework: "mlx-swift-lm/MLXVLM"
---

# Gemma4ProcessorConfiguration

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct Gemma4ProcessorConfiguration
```

## Topics

### Initializers
- [init(from: any Swift.Decoder) throws](./gemma4processorconfiguration/init%28from%29.md)
### Instance Properties
- [let boiTokenId: Int](./gemma4processorconfiguration/boitokenid.md)
- [let doNormalize: Bool](./gemma4processorconfiguration/donormalize.md)
- [let eoiTokenId: Int?](./gemma4processorconfiguration/eoitokenid.md)
- [let imageMean: [CGFloat]](./gemma4processorconfiguration/imagemean.md)
- [var imageMeanTuple: (CGFloat, CGFloat, CGFloat)](./gemma4processorconfiguration/imagemeantuple.md)
- [let imageSeqLength: Int](./gemma4processorconfiguration/imageseqlength.md)
- [let imageStd: [CGFloat]](./gemma4processorconfiguration/imagestd.md)
- [var imageStdTuple: (CGFloat, CGFloat, CGFloat)](./gemma4processorconfiguration/imagestdtuple.md)
- [let imageTokenId: Int](./gemma4processorconfiguration/imagetokenid.md)
- [let maxSoftTokens: Int](./gemma4processorconfiguration/maxsofttokens.md)
- [let patchSize: Int](./gemma4processorconfiguration/patchsize.md)
- [let poolingKernelSize: Int](./gemma4processorconfiguration/poolingkernelsize.md)
- [let processorClass: String](./gemma4processorconfiguration/processorclass.md)
- [var videoFixedSize: CGSize](./gemma4processorconfiguration/videofixedsize.md)
  Video frames use a smaller square (a multiple of patch_size * pooling_kernel_size = 48) so the vision tower’s leading pooled tokens cover the frame within the ~70-token video budget: 432 → 27x27 patches → 81 pooled tokens, trimmed to `visionSoftTokensPerVideoFrame` (70) in the model.
- [let videoMaxFrames: Int](./gemma4processorconfiguration/videomaxframes.md)
- [let videoSoftTokensPerFrame: Int](./gemma4processorconfiguration/videosofttokensperframe.md)
- [let videoTokenId: Int?](./gemma4processorconfiguration/videotokenid.md)
### Instance Methods
- [func aspectPreservingTargetSize(for: CGSize, budget: Int?) -> CGSize](./gemma4processorconfiguration/aspectpreservingtargetsize%28for,budget%29.md)
  Port of the Python Gemma4ImageProcessor’s aspect-ratio preserving resize: the largest dimensions that (a) stay within the patch budget maxSoftTokens * poolingKernelSize², and (b) keep both sides divisible by poolingKernelSize * patchSize, so the pooling kernel is exact and the pooled grid covers the image fully at any aspect ratio.
- [func encode(to: any Swift.Encoder) throws](./gemma4processorconfiguration/encode%28to%29.md)
- [func softTokenCount(height: Int, width: Int) -> Int](./gemma4processorconfiguration/softtokencount%28height,width%29.md)
  Soft tokens the vision tower produces for an image of the given (already resized) pixel dimensions.
### Default Implementations
- [Encodable Implementations](./gemma4processorconfiguration/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4processorconfiguration)*