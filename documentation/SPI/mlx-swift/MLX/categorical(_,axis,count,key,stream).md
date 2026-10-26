---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/categorical(_:axis:count:key:stream:)"
framework: "mlx-swift/MLX"
---

# categorical(_:axis:count:key:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Sample `count` values from a categorical distribution.

## Declaration

```swift
func categorical(_ logits: MLXArray, axis: Int = -1, count: Int, key: (some RandomStateOrKey)? = MLXArray?.none, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

The values are sampled from the categorical distribution specified by the unnormalized values in `logits`.

```swift
let key = MLXRandom.key(0)

let logits = MLXArray.zeros([5, 20])

// produces MLXArray of UInt32 shape [5, 2]
let result = MLXRandom.categorical(logits, count: 2, key: key)
```

## Parameters

- `logits`: The *unnormalized* categorical distribution(s).
- `axis`: Axis that specifies the distribution
- `count`: Number of samples to draw from logits
- `key`: Optional PRNG key
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/categorical(_:axis:count:key:stream:))*