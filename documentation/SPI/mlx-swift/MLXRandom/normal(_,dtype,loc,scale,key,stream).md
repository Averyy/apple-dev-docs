---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/normal(_:dtype:loc:scale:key:stream:)"
framework: "mlx-swift/MLXRandom"
---

# normal(_:dtype:loc:scale:key:stream:)

**Framework**: mlx-swift/MLXRandom  
**Kind**: func  
**Role**: Function

Generate normally distributed random numbers.

> **Deprecated**: normal is now available in the main MLX module

## Declaration

```swift
func normal(_ shape: [Int] = [], dtype: DType = .float32, loc: Float = 0, scale: Float = 1, key: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

Generate an array of random numbers using the optional shape.  The result will be of the given `type`.

```swift
let key = MLXRandom.key(0)

// generate a single Float with normal distribution
let value = MLXRandom.normal(key: key).item(Float.self)

// generate an array of Float with normal distribution in shape [10, 5]
let array = MLXRandom.normal([10, 5], key: key)
```

## Parameters

- `shape`: Shape of the output
- `dtype`: Type of the output
- `loc`: Mean of the distribution
- `scale`: Standard deviation of the distribution
- `key`: PRNG key
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/normal(_:dtype:loc:scale:key:stream:))*