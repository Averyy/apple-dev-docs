---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/uniform(_:_:type:key:stream:)-10gj2"
framework: "mlx-swift/MLXRandom"
---

# uniform(_:_:type:key:stream:)

**Framework**: mlx-swift/MLXRandom  
**Kind**: func  
**Role**: Function

Generate uniformly distributed random numbers with a `RangeExpression`.

> **Deprecated**: uniform is now available in the main MLX module

## Declaration

```swift
func uniform<R, T>(_ range: Range<R>, _ shape: [Int] = [], type: T.Type = Float.self, key: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray where R : HasDType, R : Comparable, T : HasDType, T : BinaryFloatingPoint
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/uniform(_:_:type:key:stream:)-10gj2)*