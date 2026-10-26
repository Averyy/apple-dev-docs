---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningpromptstrategy/templateflag(key:defaulton:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ReasoningPromptStrategy.templateFlag(key:defaultOn:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

Toggleable via a chat-template keyword argument (e.g. Qwen3’s `enable_thinking`). The `key` is the kwarg name; `defaultOn` is the value used when the caller expresses no preference, matching the model’s own template default.

## Declaration

```swift
case templateFlag(key: String, defaultOn: Bool)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningpromptstrategy/templateflag(key:defaulton:))*