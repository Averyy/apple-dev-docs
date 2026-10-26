---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatetokenlogprobabilities/toplogprobabilities"
framework: "mlx-swift-lm/MLXLMCommon"
---

# topLogProbabilities

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

The most likely vocabulary tokens in descending log-probability order.

## Declaration

```swift
let topLogProbabilities: [GenerateTokenLogProbability]
```

#### Discussion

This can include [`chosen`](./chosen.md) when the selected token is among the requested top candidates.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatetokenlogprobabilities/toplogprobabilities)*