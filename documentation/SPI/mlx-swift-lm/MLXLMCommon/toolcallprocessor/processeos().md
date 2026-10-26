---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallprocessor/processeos()"
framework: "mlx-swift-lm/MLXLMCommon"
---

# processEOS()

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Process end-of-sequence, parsing any buffered content as tool call(s).

## Declaration

```swift
func processEOS()
```

#### Discussion

Call this when generation ends (e.g., on EOS token) to handle formats whose end tag is never delivered as text (e.g., Mistral where `</s>` is intercepted at the token ID level).

For formats with end tags that appear in the text stream, the buffer will already be empty at generation end, making this a no-op.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallprocessor/processeos())*