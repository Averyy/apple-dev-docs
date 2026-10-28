---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokenloophandler/ontoken(_:logprobabilities:emit:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# onToken(_:logProbabilities:emit:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Return `.stop` for semantic generation stops, or `.cancelled` for consumer termination.

## Declaration

```swift
mutating func onToken(_ token: Int, logProbabilities: DeferredTokenLogProbabilities?, emit: (sending Output) -> Bool) -> TokenLoopDisposition
```

## Discussion

`logProbabilities` stays on the GPU until you call [`materialize()`](../deferredtokenlogprobabilities/materialize%28%29.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokenloophandler/ontoken(_:logprobabilities:emit:))*