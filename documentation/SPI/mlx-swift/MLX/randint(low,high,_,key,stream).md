---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/randint(low:high:_:key:stream:)"
framework: "mlx-swift/MLX"
---

# randInt(low:high:_:key:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Generate random integers from the given interval (`low:` and `high:`).

## Declaration

```swift
func randInt(low: some ScalarOrArray, high: some ScalarOrArray, _ shape: (some Collection<Int>)? = [Int]?.none, key: (some RandomStateOrKey)? = MLXArray?.none, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

The values are sampled with equal probability from the integers in half-open interval `[lb, ub)`. The lower and upper bound can be scalars or arrays and must be roadcastable to `shape`.

```swift
let key = MLXRandom.key(0)

// generate an array of Int values, one in the range 0 ..< 10
// and one in the range 10 ..< 100
let array = MLXRandom.randInt(low: [0, 10], high: [10, 100], key: key)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/randint(low:high:_:key:stream:))*