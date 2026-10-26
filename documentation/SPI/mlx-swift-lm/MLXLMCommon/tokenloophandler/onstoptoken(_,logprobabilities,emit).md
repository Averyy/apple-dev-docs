---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokenloophandler/onstoptoken(_:logprobabilities:emit:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# onStopToken(_:logProbabilities:emit:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called when `includeStopToken` is true or [`receivesStopTokens`](./receivesstoptokens.md) is true and a stop token was hit.

## Declaration

```swift
mutating func onStopToken(_ token: Int, logProbabilities: DeferredTokenLogProbabilities?, emit: (sending Output) -> Bool) -> TokenLoopDisposition
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokenloophandler/onstoptoken(_:logprobabilities:emit:))*