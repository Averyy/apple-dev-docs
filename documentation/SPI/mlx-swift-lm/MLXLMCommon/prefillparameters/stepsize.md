---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/stepsize"
framework: "mlx-swift-lm/MLXLMCommon"
---

# stepSize

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Ceiling on tokens evaluated per prefill forward. `nil` lets each model pick its own default (512 for the generic path; the Gemma 3 text path uses a smaller, tuned chunk).

## Declaration

```swift
var stepSize: Int?
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/stepsize)*