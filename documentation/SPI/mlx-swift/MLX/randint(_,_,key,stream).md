---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/randint(_:_:key:stream:)"
framework: "mlx-swift/MLX"
---

# randInt(_:_:key:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Generate random integers from the given interval using a `RangeExpression<Int>`.

## Declaration

```swift
func randInt(_ range: Range<some HasDType & BinaryInteger>, _ shape: some Collection<Int> = [], key: (some RandomStateOrKey)? = MLXArray?.none, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

The values are sampled with equal probability from the integers in half-open interval `[low, high)`. The lower and upper bound can be scalars or arrays and must be roadcastable to `shape`.

```swift
let key = MLXRandom.key(0)

// generate a single random int
let value = MLXRandom.randInt(0 ..< 100, key: key).item(Int.self)

// generate an array of shape [50] random Int32
let array = MLXRandom.randInt(Int32(0) ..< 100, [50], key: key)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/randint(_:_:key:stream:))*