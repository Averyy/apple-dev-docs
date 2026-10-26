---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/shardingerror"
framework: "mlx-swift/MLXNN"
---

# ShardingError

**Framework**: mlx-swift/MLXNN  
**Kind**: enum  
**Role**: Enumeration

A layer cannot be sharded across a group.

## Declaration

```swift
enum ShardingError
```

## Topics

### Enumeration Cases
- [case indivisible(dimension: String, of: Int, across: Int)](./shardingerror/indivisible%28dimension,of,across%29.md)
  A dimension is not divisible by the size of the group.
- [case invalidSegments(Segments, dimension: Int)](./shardingerror/invalidsegments%28_,dimension%29.md)
  The segments cannot split a dimension, e.g. `.count(3)` of 8.
- [ShardingError.missingParameter(_:)](./shardingerror/missingparameter%28_%29.md)
  The layer being sharded is missing a parameter.
- [case quantizationGroup(inputDimensions: Int, groupSize: Int, across: Int)](./shardingerror/quantizationgroup%28inputdimensions,groupsize,across%29.md)
  A shard would not hold whole quantization groups.
- [ShardingError.quantizedLayer](./shardingerror/quantizedlayer.md)
  A [`QuantizedLinear`](./quantizedlinear.md) was given to a float sharded layer.
### Instance Properties
- [var description: String](./shardingerror/description.md)
### Default Implementations
- [Equatable Implementations](./shardingerror/equatable-implementations.md)
- [Error Implementations](./shardingerror/error-implementations.md)

## Relationships

### Conforms To
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Error
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/shardingerror)*