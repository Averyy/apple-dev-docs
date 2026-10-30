---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningconfig/gemma4"
framework: "mlx-swift-lm/MLXLMCommon"
---

# gemma4

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Type Property

Gemma 4’s protocol: labeled channels (see [`gemma4`](../reasoningchannel/gemma4.md)), toggled via `enable_thinking`, whose template default is thinking off.

## Declaration

```swift
static let gemma4: ReasoningConfig
```

## Discussion

Shared here rather than spelled per model because four types (text, unified, and the LLM and VLM entry points) declare the same protocol.

Gemma 4’s templates differ in how much they prefill, and the 31B template suppresses the generation prompt entirely after a tool call or tool response. The model then opens the channel itself, so without this config its delimiters reach the caller as literal text.

A tool call opened inside a thought channel ends it, since the model does not always close the channel first.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningconfig/gemma4)*