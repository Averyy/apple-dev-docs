---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/translategemma3messagegenerator"
framework: "mlx-swift-lm/MLXLLM"
---

# TranslateGemma3MessageGenerator

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: struct  
**Role**: Structure

Message generator for TranslateGemma, Google’s translation fine-tunes of Gemma 3.

## Declaration

```swift
struct TranslateGemma3MessageGenerator
```

## Overview

TranslateGemma’s chat template needs each user turn tagged with `source_lang_code` / `target_lang_code` (ISO 639-1); supply them via `UserInput.additionalContext`. Without those codes this behaves exactly like `DefaultMessageGenerator`.

## Topics

### Initializers
- [init()](./translategemma3messagegenerator/init%28%29.md)
### Instance Methods
- [func generate(from: UserInput) -> [Message]](./translategemma3messagegenerator/generate%28from%29.md)
### Default Implementations
- [MessageGenerator Implementations](./translategemma3messagegenerator/messagegenerator-implementations.md)

## Relationships

### Conforms To
- MLXLMCommon.MessageGenerator
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/translategemma3messagegenerator)*