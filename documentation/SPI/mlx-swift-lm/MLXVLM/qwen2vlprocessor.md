---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen2vlprocessor"
framework: "mlx-swift-lm/MLXVLM"
---

# Qwen2VLProcessor

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

Qwen2VL VLM `UserInputProcessor`.

## Declaration

```swift
struct Qwen2VLProcessor
```

## Overview

This is meant to be used with [`Qwen2VL`](./qwen2vl.md) and is typically created by [`VLMModelFactory`](./vlmmodelfactory.md).

## Topics

### Initializers
- [init(Qwen2VLProcessorConfiguration, tokenizer: any Tokenizer)](./qwen2vlprocessor/init%28_,tokenizer%29.md)
### Instance Methods
- [func prepare(input: UserInput) async throws -> LMInput](./qwen2vlprocessor/prepare%28input%29.md)
- [func preprocess(images: [CIImage], processing: UserInput.Processing?) throws -> (MLXArray, THW)](./qwen2vlprocessor/preprocess%28images,processing%29.md)

## Relationships

### Conforms To
- MLXLMCommon.UserInputProcessor
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/qwen2vlprocessor)*