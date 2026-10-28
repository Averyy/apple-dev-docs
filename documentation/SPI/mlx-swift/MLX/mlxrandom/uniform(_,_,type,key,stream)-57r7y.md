---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/uniform(_:_:type:key:stream:)-57r7y"
framework: "mlx-swift/MLX"
---

# uniform(_:_:type:key:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Generate uniformly distributed random numbers with a `RangeExpression`.

## Declaration

```swift
static func uniform(_ range: Range<some HasDType & Comparable>, _ shape: some Collection<Int> = [], type: (some HasDType & BinaryFloatingPoint).Type = Float.self, key: (some RandomStateOrKey)? = MLXArray?.none, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

The values are sampled uniformly in the range.  An optional shape can be used to broadcast into a larger array.  An optional `Key` can be specified to control the PRNG.

```swift
let key = MLXRandom.key(0)

// create an array of shape [50] type Float values in the range 0 ..< 10
let array = MLXRandom.uniform(0 ..< 10, [50], key: key)

// same, but in range 0.5 ..< 1
let array = MLXRandom.uniform(0.5 ..< 1, [50], key: key)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/uniform(_:_:type:key:stream:)-57r7y)*