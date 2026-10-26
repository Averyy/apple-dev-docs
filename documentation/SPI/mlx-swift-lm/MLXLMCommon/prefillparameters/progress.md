---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/progress"
framework: "mlx-swift-lm/MLXLMCommon"
---

# progress

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Called after each prefill chunk with `(processedPositions, totalPositions)`.

## Declaration

```swift
var progress: (@Sendable (_ processed: Int, _ total: Int) -> Void)?
```

#### Discussion

Positions are the units the model prefills: prompt tokens for text models, merged embedding positions (after image expansion) for VLMs. A terminal `(total, total)` is delivered once the prompt is fully consumed, for every model — including those that prefill in a single forward. Because chunks are pipelined with `asyncEval`, intermediate calls report graph submission, slightly ahead of GPU completion.

The closure is retained for as long as the containing parameters (e.g. by a stored `GenerateParameters`) — capture weakly anything long-lived.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/progress)*