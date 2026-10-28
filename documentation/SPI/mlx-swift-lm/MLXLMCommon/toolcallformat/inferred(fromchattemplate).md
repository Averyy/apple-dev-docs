---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallformat/inferred(fromchattemplate:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# inferred(fromChatTemplate:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Type Method

The dialect a chat template renders, or `nil` when it renders none that is recognized.

## Declaration

```swift
static func inferred(fromChatTemplate template: String) -> ToolCallFormat?
```

## Discussion

This is the last resort for a checkpoint whose architecture does not declare a format: the template is what actually teaches the model how to write a call, so it identifies the dialect even for an unknown model.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallformat/inferred(fromchattemplate:))*