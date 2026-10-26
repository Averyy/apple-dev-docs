---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4configuration"
framework: "mlx-swift-lm/MLXVLM"
---

# Gemma4Configuration

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

Configuration of the Gemma 4 audio encoder (`model_type: gemma4_audio`).

## Declaration

```swift
struct Gemma4Configuration
```

## Topics

### Initializers
- [init(from: any Swift.Decoder) throws](./gemma4configuration/init%28from%29.md)
### Instance Properties
- [let audioTokenId: Int?](./gemma4configuration/audiotokenid.md)
- [let boiTokenId: Int](./gemma4configuration/boitokenid.md)
- [let eoiTokenId: Int?](./gemma4configuration/eoitokenid.md)
- [var hiddenSize: Int](./gemma4configuration/hiddensize.md)
- [let imageTokenId: Int](./gemma4configuration/imagetokenid.md)
- [let modelType: String](./gemma4configuration/modeltype.md)
- [var padTokenId: Int](./gemma4configuration/padtokenid.md)
- [let quantization: BaseConfiguration.Quantization?](./gemma4configuration/quantization.md)
- [let textConfiguration: Gemma4TextConfiguration](./gemma4configuration/textconfiguration.md)
- [let tieWordEmbeddings: Bool](./gemma4configuration/tiewordembeddings.md)
- [let videoTokenId: Int?](./gemma4configuration/videotokenid.md)
- [let visionConfiguration: Gemma4VisionConfiguration](./gemma4configuration/visionconfiguration.md)
- [let visionSoftTokensPerImage: Int](./gemma4configuration/visionsofttokensperimage.md)
- [let visionSoftTokensPerVideoFrame: Int](./gemma4configuration/visionsofttokenspervideoframe.md)
- [var vocabularySize: Int](./gemma4configuration/vocabularysize.md)
### Default Implementations
- [Encodable Implementations](./gemma4configuration/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4configuration)*