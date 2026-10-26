---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallprocessor/processchunk(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# processChunk(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Process a generated text chunk and extract any tool call content.

## Declaration

```swift
func processChunk(_ chunk: String) -> String?
```

#### Return Value

Regular text that should be displayed (non-tool call content), or `nil` if buffering

## Parameters

- `chunk`: The text chunk to process


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallprocessor/processchunk(_:))*