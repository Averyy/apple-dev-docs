---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/randint(low:high:_:type:key:stream:)"
framework: "mlx-swift/MLXRandom"
---

# randInt(low:high:_:type:key:stream:)

**Framework**: mlx-swift/MLXRandom  
**Kind**: func  
**Role**: Function

Generate random integers from the given interval (`low:` and `high:`) with a given type, e.g. `Int8.self`.

> **Deprecated**: randInt is now available in the main MLX module

## Declaration

```swift
func randInt<T>(low: any ScalarOrArray, high: any ScalarOrArray, _ shape: [Int]? = nil, type: T.Type, key: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray where T : HasDType, T : BinaryInteger
```

#### Discussion

The values are sampled with equal probability from the integers in half-open interval `[lb, ub)`. The lower and upper bound can be scalars or arrays and must be roadcastable to `shape`.  The integer results will be of the given `type`.

```swift
let key = MLXRandom.key(0)

// generate an array of Int8 values, one in the range 0 ..< 10
// and one in the range 10 ..< 100
let array = MLXRandom.randInt(low: [0, 10], high: [10, 100], type: Int8.self, key: key)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/randint(low:high:_:type:key:stream:))*