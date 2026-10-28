---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/categorical(_:axis:shape:key:stream:)"
framework: "mlx-swift/MLX"
---

# categorical(_:axis:shape:key:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Sample from a categorical distribution.

## Declaration

```swift
func categorical(_ logits: MLXArray, axis: Int = -1, shape: (some Collection<Int>)? = [Int]?.none, key: (some RandomStateOrKey)? = MLXArray?.none, stream: StreamOrDevice = .default) -> MLXArray
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
- `axis`: Axis that specifies the distribution
- `shape`: Optional shape of the output – this must be broadcast compatible with the shape of logits
- `key`: Optional PRNG key
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/categorical(_:axis:shape:key:stream:))*