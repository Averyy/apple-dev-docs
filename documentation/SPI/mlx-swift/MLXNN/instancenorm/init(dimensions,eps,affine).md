---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/instancenorm/init(dimensions:eps:affine:)"
framework: "mlx-swift/MLXNN"
---

# init(dimensions:eps:affine:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Applies instance normalization [1] on the inputs.

## Declaration

```swift
init(dimensions: Int, eps: Float = 1e-5, affine: Bool = false)
```

## Discussion

See [InstanceNorm python docs](https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.InstanceNorm.html) for more information.

### References

1. [https://arxiv.org/abs/1607.08022](https://arxiv.org/abs/1607.08022)

## Parameters

- `dimensions`: Number of features in the input
- `eps`: Value added to the denominator for numerical stability
- `affine`: If `true` adds a trainable `weight` and `bias`


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/instancenorm/init(dimensions:eps:affine:))*