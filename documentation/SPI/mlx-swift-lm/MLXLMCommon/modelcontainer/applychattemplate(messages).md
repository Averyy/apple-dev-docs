---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/applychattemplate(messages:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# applyChatTemplate(messages:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Apply chat template to messages and return token IDs.

> **Deprecated**: Use applyChatTemplate directly on tokenizer

## Declaration

```swift
func applyChatTemplate(messages: [[String : String]]) async throws -> [Int]
```

#### Return Value

Array of token IDs

## Parameters

- `messages`: Array of message dictionaries with “role” and “content” keys


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/applychattemplate(messages:))*