---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen25vlprocessor"
framework: "mlx-swift-lm/MLXVLM"
---

# Qwen25VLProcessor

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

Qwen2.5VL VLM `UserInputProcessor`.

## Declaration

```swift
struct Qwen25VLProcessor
```

## Overview

This is meant to be used with [`Qwen25VL`](./qwen25vl.md) and is typically created by [`VLMModelFactory`](./vlmmodelfactory.md).

## Topics

### Initializers
- [init(Qwen25VLProcessorConfiguration, tokenizer: any Tokenizer)](./qwen25vlprocessor/init%28_,tokenizer%29.md)
### Instance Methods
- [func prepare(input: UserInput) async throws -> LMInput](./qwen25vlprocessor/prepare%28input%29.md)
- [func preprocess(images: [CIImage], processing: UserInput.Processing?) throws -> (MLXArray, THW)](./qwen25vlprocessor/preprocess%28images,processing%29.md)

## Relationships

### Conforms To
- MLXLMCommon.UserInputProcessor
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen25vlprocessor)*