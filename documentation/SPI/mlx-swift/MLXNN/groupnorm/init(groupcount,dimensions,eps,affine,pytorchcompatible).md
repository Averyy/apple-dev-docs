---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/groupnorm/init(groupcount:dimensions:eps:affine:pytorchcompatible:)"
framework: "mlx-swift/MLXNN"
---

# init(groupCount:dimensions:eps:affine:pytorchCompatible:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Applies Group Normalization [1] on the inputs.

## Declaration

```swift
init(groupCount: Int, dimensions: Int, eps: Float = 1e-5, affine: Bool = true, pytorchCompatible: Bool = false)
```

#### Discussion

See [GroupNorm python docs](https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.GroupNorm.html) for more information.

The feature dimension is assumed to be the last dimension and the dimensions that precede it (except the first) are considered the spatial dimensions.

##### References

1. [https://arxiv.org/abs/1803.08494](https://arxiv.org/abs/1803.08494)

## Parameters

- `groupCount`: Number of groups to separate the features into
- `dimensions`: Number of features in the input
- `eps`: Value added to the denominator for numerical stability
- `affine`: If `true` adds a trainable `weight` and `bias`
- `pytorchCompatible`: If `true` perform the group normalization in the same order/grouping as PyTorch


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/groupnorm/init(groupcount:dimensions:eps:affine:pytorchcompatible:))*