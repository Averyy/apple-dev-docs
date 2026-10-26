---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/truncatednormal(low:high:_:dtype:key:stream:)"
framework: "mlx-swift/MLX"
---

# truncatedNormal(low:high:_:dtype:key:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Generate values from a truncated normal distribution between `low` and `high` with a given `DType`.

## Declaration

```swift
func truncatedNormal(low: some ScalarOrArray, high: some ScalarOrArray, _ shape: (some Collection<Int>)? = [Int]?.none, dtype: DType, key: (some RandomStateOrKey)? = MLXArray?.none, stream: StreamOrDevice = .default) -> MLXArray
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/truncatednormal(low:high:_:dtype:key:stream:))*