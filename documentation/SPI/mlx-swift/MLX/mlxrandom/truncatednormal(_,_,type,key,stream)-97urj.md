---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/truncatednormal(_:_:type:key:stream:)-97urj"
framework: "mlx-swift/MLX"
---

# truncatedNormal(_:_:type:key:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Generate values from a truncated normal distribution.

## Declaration

```swift
static func truncatedNormal(_ range: Range<some HasDType & Comparable>, _ shape: some Collection<Int> = [], type: (some HasDType & BinaryFloatingPoint).Type = Float.self, key: (some RandomStateOrKey)? = MLXArray?.none, stream: StreamOrDevice = .default) -> MLXArray
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/truncatednormal(_:_:type:key:stream:)-97urj)*