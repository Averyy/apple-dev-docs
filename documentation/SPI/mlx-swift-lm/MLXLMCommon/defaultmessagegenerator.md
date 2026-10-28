---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/defaultmessagegenerator"
framework: "mlx-swift-lm/MLXLMCommon"
---

# DefaultMessageGenerator

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Default implementation of [`MessageGenerator`](./messagegenerator.md) that produces `role` and `content`, plus `name`, `tool_call_id`, and `tool_calls` when present.

## Declaration

```swift
struct DefaultMessageGenerator
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
- [init()](./defaultmessagegenerator/init%28%29.md)
### Default Implementations
- [MessageGenerator Implementations](./defaultmessagegenerator/messagegenerator-implementations.md)

## Relationships

### Conforms To
- [MessageGenerator](./messagegenerator.md)
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/defaultmessagegenerator)*