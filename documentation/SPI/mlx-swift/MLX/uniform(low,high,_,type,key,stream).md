---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/uniform(low:high:_:type:key:stream:)"
framework: "mlx-swift/MLX"
---

# uniform(low:high:_:type:key:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Generate uniformly distributed random numbers between `low` and `high`.

## Declaration

```swift
func uniform(low: some ScalarOrArray, high: some ScalarOrArray, _ shape: (some Collection<Int>)? = [Int]?.none, type: (some HasDType & BinaryFloatingPoint).Type = Float.self, key: (some RandomStateOrKey)? = MLXArray?.none, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

The values are sampled uniformly in the half-open interval `[lb, ub)`. The lower and upper bound can be scalars or arrays and must be broadcastable to the optional `shape` (it will be the shape of the `lb` if not specified).

```swift
let key = MLXRandom.key(0)

// generate an array of two Float values, one in the range 0 ..< 10
// and one in the range 10 ..< 100
let value = MLXRandom.uniform(low: [0, 10], high: [10, 100], key: key)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/uniform(low:high:_:type:key:stream:))*