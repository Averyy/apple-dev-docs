---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/gumbel(_:type:key:stream:)"
framework: "mlx-swift/MLXRandom"
---

# gumbel(_:type:key:stream:)

**Framework**: mlx-swift/MLXRandom  
**Kind**: func  
**Role**: Function

Sample from the standard Gumbel distribution.

> **Deprecated**: gumbel is now available in the main MLX module

## Declaration

```swift
func gumbel<T>(_ shape: [Int] = [], type: T.Type = Float.self, key: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray where T : HasDType, T : BinaryFloatingPoint
```

## Discussion

The values are sampled from a standard Gumbel distribution which CDF `exp(-exp(-x))`.

```swift
let key = MLXRandom.key(0)

// generate a single Float with Gumbel distribution
let value = MLXRandom.gumbel(key: key).item(Float.self)

// generate an array of Float with Gumbel distribution in shape [10, 5]
let array = MLXRandom.gumbel([10, 5], key: key)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/gumbel(_:type:key:stream:))*