---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetconfiguration/minimumanswertokencount"
framework: "mlx-swift-lm/MLXLMCommon"
---

# minimumAnswerTokenCount

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Tokens reserved for the final answer after the worst-case transition.

## Declaration

```swift
let minimumAnswerTokenCount: Int
```

## Discussion

Parameter-driven generation rejects a finite `maxTokens` that cannot fit the reasoning budget, transition and this reserve. The default guarantees at least one answer token; applications should choose a larger product- appropriate reserve.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetconfiguration/minimumanswertokencount)*