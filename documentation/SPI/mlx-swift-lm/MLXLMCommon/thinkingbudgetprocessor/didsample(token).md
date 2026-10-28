---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetprocessor/didsample(token:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# didSample(token:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Records a sampled token, deferring the CPU←GPU read when it is safe.

## Declaration

```swift
mutating func didSample(token: MLXArray)
```

## Discussion

The newest `MLXArray` has not been evaluated yet: `item(_:)` on it blocks until the current forward pass finishes, which idles the GPU for every subsequent graph build. Holding it back for one step makes boundary detection lag by one token — unobservable while no decision can be taken inside the lag window. Once the budget comes within `ThinkingBudgetPlan.exactTrackingWindow` tokens the processor drains completely, accepting one stall per token, and stays exact through the forced transition. After the reasoning span closes it stops reading tokens altogether.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetprocessor/didsample(token:))*