---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/uniform(_:_:type:key:stream:)-8apf7"
framework: "mlx-swift/MLX"
---

# uniform(_:_:type:key:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Generate uniformly distributed random numbers with a `RangeExpression<Float>` (specialization).

## Declaration

```swift
func uniform(_ range: Range<Float> = 0 ..< 1, _ shape: some Collection<Int> = [], type: (some HasDType & BinaryFloatingPoint).Type = Float.self, key: (some RandomStateOrKey)? = MLXArray?.none, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

Specialization to make it easy to call with `Float`:

```swift
let key = MLXRandom.key(0)
let array = MLXRandom.uniform(0.5 ..< 1, [50], key: key)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/uniform(_:_:type:key:stream:)-8apf7)*