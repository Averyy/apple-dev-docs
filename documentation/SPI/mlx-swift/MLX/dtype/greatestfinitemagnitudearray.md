---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/dtype/greatestfinitemagnitudearray"
framework: "mlx-swift/MLX"
---

# greatestFiniteMagnitudeArray

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Instance Property

A scalar `MLXArray` containing the largest finite value for this dtype’s real floating-point component.

## Declaration

```swift
var greatestFiniteMagnitudeArray: MLXArray { get }
```

#### Discussion

Use this when the dtype is statically known to be floating point, e.g. `DType.float16.greatestFiniteMagnitudeArray`.

> **Precondition**: `self` is a floating-point dtype. Calling this on a non-floating-point dtype is a programming error and traps.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/dtype/greatestfinitemagnitudearray)*