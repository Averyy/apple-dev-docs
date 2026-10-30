---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningconfig/channel"
framework: "mlx-swift-lm/MLXLMCommon"
---

# channel

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

When non-nil, [`startDelimiter`](./startdelimiter.md) opens a *labeled channel* rather than a reasoning span directly: a role label follows it and decides whether the span is reasoning or the answer. `nil` (the default) is the plain delimiter-pair protocol, e.g. `<think>` … `</think>`.

## Declaration

```swift
var channel: ReasoningChannel?
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningconfig/channel)*