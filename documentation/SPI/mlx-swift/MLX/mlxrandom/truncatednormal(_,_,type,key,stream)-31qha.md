---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/truncatednormal(_:_:type:key:stream:)-31qha"
framework: "mlx-swift/MLX"
---

# truncatedNormal(_:_:type:key:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Generate values from a truncated normal distribution in a given `RangeExpression<Float>`.

## Declaration

```swift
static func truncatedNormal(_ range: Range<Float>, _ shape: some Collection<Int> = [], type: (some HasDType & BinaryFloatingPoint).Type = Float.self, key: (some RandomStateOrKey)? = MLXArray?.none, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

Specialization to make it easy to call with `Float`:

```swift
let key = MLXRandom.key(0)
let array = MLXRandom.truncatedNormal(0.5 ..< 1, [50], key: key)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/truncatednormal(_:_:type:key:stream:)-31qha)*