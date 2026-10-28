---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/bernoulli(_:key:stream:)"
framework: "mlx-swift/MLXRandom"
---

# bernoulli(_:key:stream:)

**Framework**: mlx-swift/MLXRandom  
**Kind**: func  
**Role**: Function

Generate Bernoulli random values with a `p` value of 0.5.

> **Deprecated**: bernoulli is now available in the main MLX module

## Declaration

```swift
func bernoulli(_ shape: [Int] = [], key: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

The values are sampled from the bernoulli distribution with parameter `p` using the default value of 0.5. The result will be of size `shape`.

```swift
let key = MLXRandom.key(0)

// generate a single random Bool with p = 0.5
let value = MLXRandom.bernoulli(key: key).item(Bool.self)

// generate an array of shape [50, 2] of random Bool
let array = MLXRandom.bernoulli([50, 2], key: key)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/bernoulli(_:key:stream:))*