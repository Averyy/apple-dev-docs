---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/groupnorm"
framework: "mlx-swift/MLXNN"
---

# GroupNorm

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Applies Group Normalization [1] on the inputs.

## Declaration

```swift
class GroupNorm
```

### References

1. [https://arxiv.org/abs/1803.08494](https://arxiv.org/abs/1803.08494)

### See also

- [Normalization](./normalization.md)

## Topics

### Initializers
- [init(groupCount: Int, dimensions: Int, eps: Float, affine: Bool, pytorchCompatible: Bool)](./groupnorm/init%28groupcount,dimensions,eps,affine,pytorchcompatible%29.md)
  Applies Group Normalization [1] on the inputs.
### Instance Properties
- [let bias: MLXArray?](./groupnorm/bias.md)
- [let dimensions: Int](./groupnorm/dimensions.md)
- [let eps: Float](./groupnorm/eps.md)
- [let groupCount: Int](./groupnorm/groupcount.md)
- [let pytorchCompatible: Bool](./groupnorm/pytorchcompatible.md)
- [let weight: MLXArray?](./groupnorm/weight.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./groupnorm/callasfunction%28_%29.md)

## Relationships

### Inherits From
- [Module](./module.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- Swift.CustomStringConvertible
- [UnaryLayer](./unarylayer.md)

## See Also

### Normalization Layers
- [class InstanceNorm](./instancenorm.md)
  Applies instance normalization [1] on the inputs.
- [class LayerNorm](./layernorm.md)
  Applies layer normalization [1] on the inputs.
- [class RMSNorm](./rmsnorm.md)
  Applies Root Mean Square normalization [1] to the inputs.
- [class BatchNorm](./batchnorm.md)
  Applies batch normalization [1] on the inputs.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/groupnorm)*