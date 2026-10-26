---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/museglimmerprocessor"
framework: "mlx-swift-lm/MLXVLM"
---

# MuseGlimmerProcessor

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct MuseGlimmerProcessor
```

## Topics

### Initializers
- [init(MuseGlimmerProcessorConfiguration, tokenizer: any Tokenizer)](./museglimmerprocessor/init%28_,tokenizer%29.md)
### Instance Methods
- [func prepare(input: UserInput) async throws -> LMInput](./museglimmerprocessor/prepare%28input%29.md)
- [func preprocess(image: CIImage, processing: UserInput.Processing?) throws -> (MLXArray, THW)](./museglimmerprocessor/preprocess%28image,processing%29.md)
  Resizes, normalizes and patchifies one image.

## Relationships

### Conforms To
- MLXLMCommon.UserInputProcessor
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/museglimmerprocessor)*