---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/batchnorm"
framework: "mlx-swift/MLXNN"
---

# BatchNorm

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Applies batch normalization [1] on the inputs.

## Declaration

```swift
class BatchNorm
```

### References

1. [https://arxiv.org/abs/1502.03167](https://arxiv.org/abs/1502.03167)

### See also

- [Normalization](./normalization.md)

## Topics

### Initializers
- [init(featureCount: Int, eps: Float, momentum: Float, affine: Bool, trackRunningStats: Bool)](./batchnorm/init%28featurecount,eps,momentum,affine,trackrunningstats%29.md)
  Applies batch normalization [1] on the inputs.
### Instance Properties
- [let bias: MLXArray?](./batchnorm/bias.md)
- [let eps: Float](./batchnorm/eps.md)
- [let featureCount: Int](./batchnorm/featurecount.md)
- [let momentum: Float](./batchnorm/momentum.md)
- [let weight: MLXArray?](./batchnorm/weight.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./batchnorm/callasfunction%28_%29.md)
- [func unfreeze(recursive: Bool, keys: [String]?, strict: Bool) throws](./batchnorm/unfreeze%28recursive,keys,strict%29.md)
  Unfreeze the `Module`’s parameters or subset.

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
- [class GroupNorm](./groupnorm.md)
  Applies Group Normalization [1] on the inputs.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/batchnorm)*