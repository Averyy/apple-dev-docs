---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/messagegenerator"
framework: "mlx-swift-lm/MLXLMCommon"
---

# MessageGenerator

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Protocol for something that can convert structured [`Chat.Message`](./chat/message.md) into model specific [`Message`](./message.md) (raw dictionary) format.

## Declaration

```swift
protocol MessageGenerator : Sendable
```

## Overview

Typically this is owned and used by a [`UserInputProcessor`](./userinputprocessor.md):

```swift
public func prepare(input: UserInput) async throws -> LMInput {
    let messages = Qwen2VLMessageGenerator().generate(from: input)
    ...
```

## Topics

### Instance Methods
- [func addToolMetadata(to: inout Message, for: Chat.Message)](./messagegenerator/addtoolmetadata%28to,for%29.md)
  Adds tool-call metadata from a structured message to a raw message dictionary.
- [func generate(from: UserInput) -> [Message]](./messagegenerator/generate%28from%29.md)
  Generates messages from the input.
- [func generate(message: Chat.Message) -> Message](./messagegenerator/generate%28message%29.md)
  Returns `[String: any Sendable]`, aka [`Message`](./message.md).
- [func generate(messages: [Chat.Message]) -> [Message]](./messagegenerator/generate%28messages%29.md)
  Returns array of `[String: any Sendable]` aka [`Message`](./message.md)

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [DefaultMessageGenerator](./defaultmessagegenerator.md)
- [NoSystemMessageGenerator](./nosystemmessagegenerator.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/messagegenerator)*