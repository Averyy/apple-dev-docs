---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/instancenorm"
framework: "mlx-swift/MLXNN"
---

# InstanceNorm

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Applies instance normalization [1] on the inputs.

## Declaration

```swift
class InstanceNorm
```

### References

1. [https://arxiv.org/abs/1607.08022](https://arxiv.org/abs/1607.08022)

### See also

- [Normalization](./normalization.md)

## Topics

### Initializers
- [init(dimensions: Int, eps: Float, affine: Bool)](./instancenorm/init%28dimensions,eps,affine%29.md)
  Applies instance normalization [1] on the inputs.
### Instance Properties
- [let bias: MLXArray?](./instancenorm/bias.md)
- [let dimensions: Int](./instancenorm/dimensions.md)
- [let eps: Float](./instancenorm/eps.md)
- [let weight: MLXArray?](./instancenorm/weight.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./instancenorm/callasfunction%28_%29.md)

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
- [class LayerNorm](./layernorm.md)
  Applies layer normalization [1] on the inputs.
- [class RMSNorm](./rmsnorm.md)
  Applies Root Mean Square normalization [1] to the inputs.
- [class GroupNorm](./groupnorm.md)
  Applies Group Normalization [1] on the inputs.
- [class BatchNorm](./batchnorm.md)
  Applies batch normalization [1] on the inputs.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/instancenorm)*