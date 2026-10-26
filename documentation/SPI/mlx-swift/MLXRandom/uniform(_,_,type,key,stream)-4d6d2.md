---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/uniform(_:_:type:key:stream:)-4d6d2"
framework: "mlx-swift/MLXRandom"
---

# uniform(_:_:type:key:stream:)

**Framework**: mlx-swift/MLXRandom  
**Kind**: func  
**Role**: Function

Generate uniformly distributed random numbers with a `RangeExpression<Float>` (specialization).

> **Deprecated**: uniform is now available in the main MLX module

## Declaration

```swift
func uniform<T>(_ range: Range<Float> = 0 ..< 1, _ shape: [Int] = [], type: T.Type = Float.self, key: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray where T : HasDType, T : BinaryFloatingPoint
```

#### Discussion

Specialization to make it easy to call with `Float`:

```swift
let key = MLXRandom.key(0)
let array = MLXRandom.uniform(0.5 ..< 1, [50], key: key)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/uniform(_:_:type:key:stream:)-4d6d2)*