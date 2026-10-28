---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/normal(_:dtype:loc:scale:key:stream:)"
framework: "mlx-swift/MLX"
---

# normal(_:dtype:loc:scale:key:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Generate normally distributed random numbers.

## Declaration

```swift
func normal(_ shape: some Collection<Int> = [], dtype: DType, loc: Float = 0, scale: Float = 1, key: (some RandomStateOrKey)? = MLXArray?.none, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/normal(_:dtype:loc:scale:key:stream:))*