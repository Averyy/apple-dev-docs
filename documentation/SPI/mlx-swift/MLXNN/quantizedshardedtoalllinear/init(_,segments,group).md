---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedshardedtoalllinear/init(_:segments:group:)"
framework: "mlx-swift/MLXNN"
---

# init(_:segments:group:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Create a sharded layer from an existing [`QuantizedLinear`](../quantizedlinear.md).

## Declaration

```swift
convenience init(_ other: QuantizedLinear, segments: Segments = .count(1), group: MLXDistributed.Group? = nil) throws
```

#### Discussion

This shards the input dimension, which is the packed one, so every segment has to hold whole quantization groups on every process.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedshardedtoalllinear/init(_:segments:group:))*