---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/paligemmaprocessor"
framework: "mlx-swift-lm/MLXVLM"
---

# PaliGemmaProcessor

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

PaliGemma VLM `UserInputProcessor`.

## Declaration

```swift
struct PaliGemmaProcessor
```

#### Overview

This is meant to be used with [`PaliGemma`](./paligemma.md) and is typically created by [`VLMModelFactory`](./vlmmodelfactory.md).

## Topics

### Initializers
- [init(PaliGemmaProcessorConfiguration, tokenizer: any Tokenizer)](./paligemmaprocessor/init%28_,tokenizer%29.md)
### Instance Methods
- [func prepare(input: UserInput) throws -> LMInput](./paligemmaprocessor/prepare%28input%29.md)

## Relationships

### Conforms To
- MLXLMCommon.UserInputProcessor
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/paligemmaprocessor)*