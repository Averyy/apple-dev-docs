---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/uniform(low:high:_:dtype:key:stream:)"
framework: "mlx-swift/MLXRandom"
---

# uniform(low:high:_:dtype:key:stream:)

**Framework**: mlx-swift/MLXRandom  
**Kind**: func  
**Role**: Function

Generate uniformly distributed random numbers between `low` and `high` with a given `DType`.

> **Deprecated**: uniform is now available in the main MLX module

## Declaration

```swift
func uniform(low: any ScalarOrArray, high: any ScalarOrArray, _ shape: [Int]? = nil, dtype: DType = .float32, key: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

The values are sampled uniformly in the half-open interval `[lb, ub)`. The lower and upper bound can be scalars or arrays and must be broadcastable to the optional `shape` (it will be the shape of the `lb` if not specified).

```swift
let key = MLXRandom.key(0)

// generate an array of two Float values, one in the range 0 ..< 10
// and one in the range 10 ..< 100
let value = MLXRandom.uniform(low: [0, 10], high: [10, 100], key: key)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/uniform(low:high:_:dtype:key:stream:))*