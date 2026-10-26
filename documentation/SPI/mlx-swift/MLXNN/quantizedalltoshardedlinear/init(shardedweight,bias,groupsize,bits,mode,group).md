---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedalltoshardedlinear/init(shardedweight:bias:groupsize:bits:mode:group:)"
framework: "mlx-swift/MLXNN"
---

# init(shardedWeight:bias:groupSize:bits:mode:group:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Quantize a weight that is already this process’ shard.

## Declaration

```swift
init(shardedWeight weight: MLXArray, bias: MLXArray?, groupSize: Int = 64, bits: Int = 4, mode: QuantizationMode = .affine, group: MLXDistributed.Group)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedalltoshardedlinear/init(shardedweight:bias:groupsize:bits:mode:group:))*