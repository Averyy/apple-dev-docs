---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/stepdecay(_:decayrate:stepsize:)"
framework: "mlx-swift/MLXOptimizers"
---

# stepDecay(_:decayRate:stepSize:)

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: func  
**Role**: Function

Make a step-decay schedule: `initial * decayRate ** (step / stepSize)`.

## Declaration

```swift
func stepDecay(_ initial: Float, decayRate: Float, stepSize: Int) -> (Int) -> Float
```

## Parameters

- `initial`: Initial value
- `decayRate`: Multiplicative factor to decay by
- `stepSize`: Decay every `stepSize` steps


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/stepdecay(_:decayrate:stepsize:))*