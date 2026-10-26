---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatecompletioninfo/accepteddrafttokens"
framework: "mlx-swift-lm/MLXLMCommon"
---

# acceptedDraftTokens

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Total tokens accepted by the target across all speculation rounds in this stream, or nil for non-MTP iterators. The acceptance rate is `Double(acceptedDraftTokens) / Double(proposedDraftTokens)` when both are non-nil and proposed > 0.

## Declaration

```swift
let acceptedDraftTokens: Int?
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatecompletioninfo/accepteddrafttokens)*