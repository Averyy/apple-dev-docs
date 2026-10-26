---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4unifiedprocessor"
framework: "mlx-swift-lm/MLXVLM"
---

# Gemma4UnifiedProcessor

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct Gemma4UnifiedProcessor
```

## Topics

### Initializers
- [init(Gemma4UnifiedProcessorConfiguration, tokenizer: any Tokenizer)](./gemma4unifiedprocessor/init%28_,tokenizer%29.md)
### Instance Methods
- [func prepare(input: UserInput) async throws -> LMInput](./gemma4unifiedprocessor/prepare%28input%29.md)
- [func preprocess(images: [CIImage], processing: UserInput.Processing?) throws -> (pixels: MLXArray, positionIds: MLXArray, tokenCounts: [Int], frames: [THW])](./gemma4unifiedprocessor/preprocess%28images,processing%29.md)

## Relationships

### Conforms To
- MLXLMCommon.UserInputProcessor
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/gemma4unifiedprocessor)*