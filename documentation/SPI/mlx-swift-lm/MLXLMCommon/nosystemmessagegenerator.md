---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/nosystemmessagegenerator"
framework: "mlx-swift-lm/MLXLMCommon"
---

# NoSystemMessageGenerator

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Implementation of [`MessageGenerator`](./messagegenerator.md) that produces a `role` and `content` but omits `system` roles.

## Declaration

```swift
struct NoSystemMessageGenerator
```

## Overview

```swift
[
    "role": message.role.rawValue,
    "content": message.content,
]
```

## Topics

### Initializers
- [init()](./nosystemmessagegenerator/init%28%29.md)
### Instance Methods
- [func generate(messages: [Chat.Message]) -> [Message]](./nosystemmessagegenerator/generate%28messages%29.md)
### Default Implementations
- [MessageGenerator Implementations](./nosystemmessagegenerator/messagegenerator-implementations.md)

## Relationships

### Conforms To
- [MessageGenerator](./messagegenerator.md)
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/nosystemmessagegenerator)*