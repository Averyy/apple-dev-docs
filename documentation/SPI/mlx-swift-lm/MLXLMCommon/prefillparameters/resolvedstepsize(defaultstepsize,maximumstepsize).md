---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/resolvedstepsize(defaultstepsize:maximumstepsize:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# resolvedStepSize(defaultStepSize:maximumStepSize:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

The effective step-size ceiling: [`stepSize`](./stepsize.md) if set, else the model’s `defaultStepSize`, clamped to `maximumStepSize` and floored at 1.

## Declaration

```swift
func resolvedStepSize(defaultStepSize: Int = PrefillParameters.defaultStepSize, maximumStepSize: Int? = nil) -> Int
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/resolvedstepsize(defaultstepsize:maximumstepsize:))*