---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/glmocrprocessor"
framework: "mlx-swift-lm/MLXVLM"
---

# GlmOcrProcessor

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

GlmOcr VLM `UserInputProcessor`.

## Declaration

```swift
struct GlmOcrProcessor
```

## Topics

### Initializers
- [init(GlmOcrProcessorConfiguration, tokenizer: any Tokenizer)](./glmocrprocessor/init%28_,tokenizer%29.md)
### Instance Methods
- [func prepare(input: UserInput) async throws -> LMInput](./glmocrprocessor/prepare%28input%29.md)
- [func preprocess(images: [CIImage], processing: UserInput.Processing?) throws -> (MLXArray, THW)](./glmocrprocessor/preprocess%28images,processing%29.md)

## Relationships

### Conforms To
- MLXLMCommon.UserInputProcessor
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/glmocrprocessor)*