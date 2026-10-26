---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/cosinedecay(_:decaysteps:end:)"
framework: "mlx-swift/MLXOptimizers"
---

# cosineDecay(_:decaySteps:end:)

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: func  
**Role**: Function

Make a cosine-decay schedule. The value is constant (`end`) for steps beyond `decaySteps`.

## Declaration

```swift
func cosineDecay(_ initial: Float, decaySteps: Int, end: Float = 0.0) -> (Int) -> Float
```

## Parameters

- `initial`: Initial value
- `decaySteps`: Number of steps to decay over
- `end`: Final value to decay to (default 0)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/cosinedecay(_:decaysteps:end:))*