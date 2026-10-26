---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/batchnorm/init(featurecount:eps:momentum:affine:trackrunningstats:)"
framework: "mlx-swift/MLXNN"
---

# init(featureCount:eps:momentum:affine:trackRunningStats:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Applies batch normalization [1] on the inputs.

## Declaration

```swift
init(featureCount: Int, eps: Float = 1e-5, momentum: Float = 0.1, affine: Bool = true, trackRunningStats: Bool = true)
```

#### Discussion

See [BatchNorm python docs](https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.BatchNorm.html) for more information.

The input shape is specified as `NC` or `NLC`, where `N` is the batch, `C` is the number of features or channels, and `L` is the sequence length. The output has the same shape as the input. For four-dimensional arrays, the shape is `NHWC`, where `H` and `W` are the height and width respectively.

For more information on Batch Normalization, see the original paper “Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift” [https://arxiv.org/abs/1502.03167](https://arxiv.org/abs/1502.03167).

##### References

1. [https://arxiv.org/abs/1502.03167](https://arxiv.org/abs/1502.03167)

## Parameters

- `featureCount`: Number of features in the input
- `eps`: Value added to the denominator for numerical stability
- `momentum`: Momentum for updating the running mean and variance
- `affine`: If `true` adds a trainable `weight` and `bias`
- `trackRunningStats`: If `true` track the running mean and variance


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/batchnorm/init(featurecount:eps:momentum:affine:trackrunningstats:))*