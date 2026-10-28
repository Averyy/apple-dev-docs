---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/bernoulli(_:_:key:stream:)"
framework: "mlx-swift/MLX"
---

# bernoulli(_:_:key:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Generate Bernoulli random values with a given `p` value.

## Declaration

```swift
static func bernoulli(_ p: some ScalarOrArray, _ shape: (some Collection<Int>)? = [Int]?.none, key: (some RandomStateOrKey)? = MLXArray?.none, stream: StreamOrDevice = .default) -> MLXArray
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxrandom/bernoulli(_:_:key:stream:))*