---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/gumbel(_:dtype:key:stream:)"
framework: "mlx-swift/MLXRandom"
---

# gumbel(_:dtype:key:stream:)

**Framework**: mlx-swift/MLXRandom  
**Kind**: func  
**Role**: Function

Sample from the standard Gumbel distribution with a given `DType`.

> **Deprecated**: gumbel is now available in the main MLX module

## Declaration

```swift
func gumbel(_ shape: [Int] = [], dtype: DType = .float32, key: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/gumbel(_:dtype:key:stream:))*