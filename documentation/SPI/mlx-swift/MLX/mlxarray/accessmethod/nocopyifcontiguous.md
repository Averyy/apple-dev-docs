---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/accessmethod/nocopyifcontiguous"
framework: "mlx-swift/MLX"
---

# MLXArray.AccessMethod.noCopyIfContiguous

**Framework**: mlx-swift/MLX  
**Kind**: case  
**Role**: Case

Return contiguous data from the backing of the [`MLXArray`](../../mlxarray.md), avoiding a copy if possible. The lifetime of the result is valid only while keeping the [`MLXArray`](../../mlxarray.md) alive.  This is best for temporary copies, e.g. creating and writing an image to disk.

## Declaration

```swift
case noCopyIfContiguous
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/accessmethod/nocopyifcontiguous)*