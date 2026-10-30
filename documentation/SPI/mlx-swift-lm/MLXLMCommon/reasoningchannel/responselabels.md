---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningchannel/responselabels"
framework: "mlx-swift-lm/MLXLMCommon"
---

# responseLabels

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Labels whose channel carries the answer rather than reasoning.

## Declaration

```swift
var responseLabels: Set<String>
```

## Discussion

Every other label routes to reasoning, which is the safe direction: the text is still delivered, and no scratchpad or raw marker can reach the answer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningchannel/responselabels)*