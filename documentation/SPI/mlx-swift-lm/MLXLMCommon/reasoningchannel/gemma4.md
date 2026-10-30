---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningchannel/gemma4"
framework: "mlx-swift-lm/MLXLMCommon"
---

# gemma4

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Type Property

Gemma 4: `<|channel>thought\n ... <channel|>` carries reasoning.

## Declaration

```swift
static let gemma4: ReasoningChannel
```

## Discussion

No shipped template wraps the answer in a channel, so `content` is listed defensively: it costs nothing and keeps such an answer out of the thought stream if one ever appears.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningchannel/gemma4)*