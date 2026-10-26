---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/prompt-swift.enum"
framework: "mlx-swift-lm/MLXLMCommon"
---

# UserInput.Prompt

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Representation of a prompt or series of messages (conversation).

## Declaration

```swift
enum Prompt
```

#### Overview

This may be a single string with a user prompt or a series of back and forth responses representing a conversation.

## Topics

### Enumeration Cases
- [UserInput.Prompt.chat(_:)](./prompt-swift.enum/chat%28_%29.md)
  Model-agnostic structured chat (series of messages)
- [UserInput.Prompt.messages(_:)](./prompt-swift.enum/messages%28_%29.md)
  Model-specific array of dictionaries
- [UserInput.Prompt.text(_:)](./prompt-swift.enum/text%28_%29.md)
  A single string
### Instance Properties
- [var description: String](./prompt-swift.enum/description.md)

## Relationships

### Conforms To
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/prompt-swift.enum)*