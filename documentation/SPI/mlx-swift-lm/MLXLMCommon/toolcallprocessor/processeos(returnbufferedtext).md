---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallprocessor/processeos(returnbufferedtext:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# processEOS(returnBufferedText:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Process end-of-sequence and optionally return residual buffered text.

## Declaration

```swift
@discardableResult
func processEOS(returnBufferedText: Bool = true) -> String?
```

#### Return Value

Residual buffered text that should be emitted as regular output, or `nil` when the buffer was fully parsed as tool call content (or when `returnBufferedText` is `false`).

#### Discussion

Use this overload when callers need to preserve non-tool trailing content that remained buffered until generation end.

## Parameters

- `returnBufferedText`: When `true`, returns residual text if no tool call was parsed from the buffered content.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallprocessor/processeos(returnbufferedtext:))*