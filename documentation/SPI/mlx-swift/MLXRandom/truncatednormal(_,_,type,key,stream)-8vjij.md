---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/truncatednormal(_:_:type:key:stream:)-8vjij"
framework: "mlx-swift/MLXRandom"
---

# truncatedNormal(_:_:type:key:stream:)

**Framework**: mlx-swift/MLXRandom  
**Kind**: func  
**Role**: Function

Generate values from a truncated normal distribution.

> **Deprecated**: truncatedNormal is now available in the main MLX module

## Declaration

```swift
func truncatedNormal<R, T>(_ range: Range<R>, _ shape: [Int] = [], type: T.Type = Float.self, key: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray where R : HasDType, R : Comparable, T : HasDType, T : BinaryFloatingPoint
```

#### Discussion

The values are sampled from the truncated normal distribution in the range. An optional shape can be used to broadcast into a larger array.  An optional `Key` can be specified to control the PRNG.

```swift
let key = MLXRandom.key(0)

// create an array of shape [50] type Float values in the range 0 ..< 10
let array = MLXRandom.truncatedNormal(0 ..< 10, [50], key: key)

// same, but in range 0.5 ..< 1
let array = MLXRandom.truncatedNormal(0.5 ..< 1, [50], key: key)
```

##### See also

- [JAX Documentation](https://jax.readthedocs.io/en/latest/_modules/jax/_src/random.html#truncated_normal)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/truncatednormal(_:_:type:key:stream:)-8vjij)*