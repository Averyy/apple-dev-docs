---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/layernorm"
framework: "mlx-swift/MLXNN"
---

# LayerNorm

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Applies layer normalization [1] on the inputs.

## Declaration

```swift
class LayerNorm
```

##### References

1. [https://arxiv.org/abs/1607.06450](https://arxiv.org/abs/1607.06450)

##### See also

- [Normalization](./normalization.md)

## Topics

### Initializers
- [init(dimensions: Int, eps: Float, affine: Bool, bias: Bool)](./layernorm/init%28dimensions,eps,affine,bias%29.md)
  Applies layer normalization [1] on the inputs.
### Instance Properties
- [let bias: MLXArray?](./layernorm/bias.md)
- [let dimensions: Int](./layernorm/dimensions.md)
- [let eps: Float](./layernorm/eps.md)
- [let weight: MLXArray?](./layernorm/weight.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./layernorm/callasfunction%28_%29.md)

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
- [class RMSNorm](./rmsnorm.md)
  Applies Root Mean Square normalization [1] to the inputs.
- [class GroupNorm](./groupnorm.md)
  Applies Group Normalization [1] on the inputs.
- [class BatchNorm](./batchnorm.md)
  Applies batch normalization [1] on the inputs.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/layernorm)*