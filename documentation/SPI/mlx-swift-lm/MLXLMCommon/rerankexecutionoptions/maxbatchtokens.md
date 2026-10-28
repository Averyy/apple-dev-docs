---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankexecutionoptions/maxbatchtokens"
framework: "mlx-swift-lm/MLXLMCommon"
---

# maxBatchTokens

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Maximum number of token slots in one model forward pass.

## Declaration

```swift
var maxBatchTokens: Int
```

## Discussion

For pairwise models this bounds `batchSize * paddedSequenceLength`. For listwise models it bounds the complete query-and-document prompt.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rerankexecutionoptions/maxbatchtokens)*