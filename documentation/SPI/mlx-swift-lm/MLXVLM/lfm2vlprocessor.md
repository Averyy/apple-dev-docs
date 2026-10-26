---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/lfm2vlprocessor"
framework: "mlx-swift-lm/MLXVLM"
---

# LFM2VLProcessor

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

LFM2 VL VLM `UserInputProcessor`.

## Declaration

```swift
struct LFM2VLProcessor
```

#### Overview

This is meant to be used with [`LFM2VL`](./lfm2vl.md) and is typically created by [`VLMModelFactory`](./vlmmodelfactory.md).

## Topics

### Initializers
- [init(LFM2VLProcessorConfiguration, tokenizer: any Tokenizer)](./lfm2vlprocessor/init%28_,tokenizer%29.md)
### Instance Methods
- [func prepare(input: UserInput) async throws -> LMInput](./lfm2vlprocessor/prepare%28input%29.md)

## Relationships

### Conforms To
- MLXLMCommon.UserInputProcessor
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/lfm2vlprocessor)*