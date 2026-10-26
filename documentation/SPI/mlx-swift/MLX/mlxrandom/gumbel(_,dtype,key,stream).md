---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/gumbel(_:dtype:key:stream:)"
framework: "mlx-swift/MLX"
---

# gumbel(_:dtype:key:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Sample from the standard Gumbel distribution with a given `DType`.

## Declaration

```swift
static func gumbel(_ shape: some Collection<Int> = [], dtype: DType, key: (some RandomStateOrKey)? = MLXArray?.none, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

The values are sampled from a standard Gumbel distribution which CDF `exp(-exp(-x))`.

```swift
let key = MLXRandom.key(0)

// generate a single Float with Gumbel distribution
let value = MLXRandom.gumbel(key: key).item(Float.self)

// generate an array of Float with Gumbel distribution in shape [10, 5]
let array = MLXRandom.gumbel([10, 5], key: key)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/gumbel(_:dtype:key:stream:))*