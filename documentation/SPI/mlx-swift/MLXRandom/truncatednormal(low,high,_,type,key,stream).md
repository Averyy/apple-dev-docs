---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/truncatednormal(low:high:_:type:key:stream:)"
framework: "mlx-swift/MLXRandom"
---

# truncatedNormal(low:high:_:type:key:stream:)

**Framework**: mlx-swift/MLXRandom  
**Kind**: func  
**Role**: Function

Generate values from a truncated normal distribution between `low` and `high`.

> **Deprecated**: truncatedNormal is now available in the main MLX module

## Declaration

```swift
func truncatedNormal<T>(low: any ScalarOrArray, high: any ScalarOrArray, _ shape: [Int]? = nil, type: T.Type = Float.self, key: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray where T : HasDType, T : BinaryFloatingPoint
```

#### Discussion

The values are sampled from the truncated normal distribution on the domain `(lower, upper)`. The bounds `lower` and `upper` can be scalars or arrays and must be broadcastable to `shape`.

```swift
let key = MLXRandom.key(0)

// generate an array of two Float values, one in the range 0 ..< 10
// and one in the range 10 ..< 100
let value = MLXRandom.truncatedNormal([0, 10], [10, 100], key: key)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/truncatednormal(low:high:_:type:key:stream:))*