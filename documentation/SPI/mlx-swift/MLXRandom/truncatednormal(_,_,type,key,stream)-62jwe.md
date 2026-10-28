---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/truncatednormal(_:_:type:key:stream:)-62jwe"
framework: "mlx-swift/MLXRandom"
---

# truncatedNormal(_:_:type:key:stream:)

**Framework**: mlx-swift/MLXRandom  
**Kind**: func  
**Role**: Function

Generate values from a truncated normal distribution in a given `RangeExpression<Float>`.

> **Deprecated**: truncatedNormal is now available in the main MLX module

## Declaration

```swift
func truncatedNormal<T>(_ range: Range<Float>, _ shape: [Int] = [], type: T.Type = Float.self, key: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray where T : HasDType, T : BinaryFloatingPoint
```

## Discussion

Specialization to make it easy to call with `Float`:

```swift
let key = MLXRandom.key(0)
let array = MLXRandom.truncatedNormal(0.5 ..< 1, [50], key: key)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/truncatednormal(_:_:type:key:stream:)-62jwe)*