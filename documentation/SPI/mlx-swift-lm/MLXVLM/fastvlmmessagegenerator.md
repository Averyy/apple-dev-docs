---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/fastvlmmessagegenerator"
framework: "mlx-swift-lm/MLXVLM"
---

# FastVLMMessageGenerator

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

This message generator adheres to the following format:

## Declaration

```swift
struct FastVLMMessageGenerator
```

#### Overview

- Image precedes text content
- Empty system messages are removed - the chat template applies a default one in this case

## Topics

### Initializers
- [init()](./fastvlmmessagegenerator/init%28%29.md)
### Instance Methods
- [func generate(message: Chat.Message) -> MLXLMCommon.Message](./fastvlmmessagegenerator/generate%28message%29.md)
- [func generate(messages: [Chat.Message]) -> [MLXLMCommon.Message]](./fastvlmmessagegenerator/generate%28messages%29.md)
### Default Implementations
- [MessageGenerator Implementations](./fastvlmmessagegenerator/messagegenerator-implementations.md)

## Relationships

### Conforms To
- MLXLMCommon.MessageGenerator
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/fastvlmmessagegenerator)*