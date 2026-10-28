---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/fftnorm"
framework: "mlx-swift/MLX"
---

# FFTNorm

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

Normalization mode for discrete Fourier Transforms.

## Declaration

```swift
enum FFTNorm
```

### See Also

- [`MLXFFT`](./mlxfft.md)

## Topics

### Enumeration Cases
- [FFTNorm.backward](./fftnorm/backward.md)
  No normalization on the forward transform; the inverse transform is scaled by `1/n`.
- [FFTNorm.forward](./fftnorm/forward.md)
  The forward transform is scaled by `1/n`; no normalization on the inverse transform.
- [FFTNorm.ortho](./fftnorm/ortho.md)
  Both the forward and inverse transforms are scaled by `1/sqrt(n)`, making the transform unitary.
### Default Implementations
- [Equatable Implementations](./fftnorm/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/fftnorm)*