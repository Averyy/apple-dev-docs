---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/categorical(_:axis:shape:key:stream:)"
framework: "mlx-swift/MLXRandom"
---

# categorical(_:axis:shape:key:stream:)

**Framework**: mlx-swift/MLXRandom  
**Kind**: func  
**Role**: Function

Sample from a categorical distribution.

> **Deprecated**: categorical is now available in the main MLX module

## Declaration

```swift
func categorical(_ logits: MLXArray, axis: Int = -1, shape: [Int]? = nil, key: MLXArray? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

The values are sampled from the categorical distribution specified by the unnormalized values in `logits`.   If the `shape` is not specified the result shape will be the same shape as `logits` with the `axis` dimension removed.

```swift
let key = MLXRandom.key(0)

let logits = MLXArray.zeros([5, 20])

// produces MLXArray of UInt32 shape [5]
let result = MLXRandom.categorical(logits, key: key)
```

## Parameters

- `logits`: The *unnormalized* categorical distribution(s).
- `axis`: The axis which specifies the distribution
- `shape`: The shape of the output
- `key`: PRNG key
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxrandom/categorical(_:axis:shape:key:stream:))*