---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generateparameters/seed"
framework: "mlx-swift-lm/MLXLMCommon"
---

# seed

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Optional seed for reproducible sampling. When set, the sampler’s RNG (`TopPSampler` / `CategoricalSampler`) is seeded deterministically, so the same `(seed, prompt, parameters)` produces the same sampled tokens. `nil` ⇒ the sampler is seeded from system entropy (the prior default). Inert at `temperature == 0` (argmax has no RNG).

## Declaration

```swift
var seed: UInt64?
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generateparameters/seed)*