---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/bernoulli(_:_:key:stream:)"
framework: "mlx-swift/MLXRandom"
---

# bernoulli(_:_:key:stream:)

**Framework**: mlx-swift/MLXRandom  
**Kind**: func  
**Role**: Function

Generate Bernoulli random values with a given `p` value.

> **Deprecated**: bernoulli is now available in the main MLX module

## Declaration

```swift
func bernoulli(_ p: any ScalarOrArray, _ shape: [Int]? = nil, key: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

The values are sampled from the bernoulli distribution with parameter `p`. The parameter `p` must have a floating point type and must be broadcastable to `shape`.

```swift
let key = MLXRandom.key(0)

// generate a single random Bool with p = 0.8
let value = MLXRandom.bernoulli(0.8, key: key).item(Bool.self)

// generate an array of shape [50, 2] of random Bool with p = 0.8
let array = MLXRandom.bernoulli(0.8, [50, 2], key: key)

// generate an array of [3] Bool with the given p values
let array = MLXRandom.bernoulli(MLXArray(convert: [0.1, 0.5, 0.8]), key: key)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/bernoulli(_:_:key:stream:))*