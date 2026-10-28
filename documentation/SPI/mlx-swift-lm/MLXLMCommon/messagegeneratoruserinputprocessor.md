---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/messagegeneratoruserinputprocessor"
framework: "mlx-swift-lm/MLXLMCommon"
---

# MessageGeneratorUserInputProcessor

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Applies a configured message generator before delegating input processing.

## Declaration

```swift
struct MessageGeneratorUserInputProcessor
```

## Overview

This lets a model configuration override a VLM processor’s built-in generator without changing the processor implementation.

> ❗ **Important**: The override fully replaces the model’s own generator, including any image/video placeholder content that generator would emit. A text-only generator on a VLM configuration therefore loses media conditioning: Qwen-family processors throw on the placeholder-count mismatch, others silently ignore the attached media.

## Topics

### Initializers
- [init(processor: any UserInputProcessor, messageGenerator: any MessageGenerator)](./messagegeneratoruserinputprocessor/init%28processor,messagegenerator%29.md)
### Instance Methods
- [func prepare(input: UserInput) async throws -> LMInput](./messagegeneratoruserinputprocessor/prepare%28input%29.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- [UserInputProcessor](./userinputprocessor.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/messagegeneratoruserinputprocessor)*