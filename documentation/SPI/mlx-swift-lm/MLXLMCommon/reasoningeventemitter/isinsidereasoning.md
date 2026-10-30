---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningeventemitter/isinsidereasoning"
framework: "mlx-swift-lm/MLXLMCommon"
---

# isInsideReasoning

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Whether the scanner is currently inside a reasoning span.

## Declaration

```swift
var isInsideReasoning: Bool { get }
```

## Discussion

The generation loop reads this to attribute generated tokens to the reasoning token count (one `.token` = one token), since the emitter itself only sees decoded text, not token IDs.

Reading a channel’s label counts as inside: the channel is open, and the handful of label tokens are metadata that no answer will ever contain.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningeventemitter/isinsidereasoning)*