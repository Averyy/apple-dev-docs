---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/qwenreasoningprotocol"
framework: "mlx-swift-lm/MLXLMCommon"
---

# QwenReasoningProtocol

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Qwen-family reasoning protocol declarations.

## Declaration

```swift
enum QwenReasoningProtocol
```

#### Overview

Model-specific wire behavior lives here rather than in [`ReasoningConfig`](./reasoningconfig.md). The generic configuration only describes a protocol; this adapter decides which Qwen families have a validated hard-budget transition.

## Topics

### Type Properties
- [static let qwen3: ReasoningConfig](./qwenreasoningprotocol/qwen3.md)
  The original hybrid Qwen3 protocol and its published budget transition.
- [static let tagged: ReasoningConfig](./qwenreasoningprotocol/tagged.md)
  Qwen-compatible `<think>` tags and tool-call boundary, without claiming that a hard-budget transition is safe for the model.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/qwenreasoningprotocol)*