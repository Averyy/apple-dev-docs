---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/accessmethod"
framework: "mlx-swift/MLX"
---

# MLXArray.AccessMethod

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

How to access backing data with [`asData(access:)`](./asdata%28access%29.md) – this controls how [`MLXArray.MLXArrayData`](./mlxarraydata.md) is produced.

## Declaration

```swift
enum AccessMethod
```

## Topics

### Enumeration Cases
- [MLXArray.AccessMethod.copy](./accessmethod/copy.md)
  Create a contiguous copy of the data backing the [`MLXArray`](../mlxarray.md).  The lifetime of this data independent of the lifetime of the [`MLXArray`](../mlxarray.md).
- [MLXArray.AccessMethod.noCopy](./accessmethod/nocopy.md)
  Return a wrapper around the backing of the [`MLXArray`](../mlxarray.md).  This might not be contiguous – the caller must examine [`strides`](./mlxarraydata/strides.md) The lifetime of the result is valid only while keeping the [`MLXArray`](../mlxarray.md) alive.  This is best for temporary copies, e.g. creating and writing an image to disk.
- [MLXArray.AccessMethod.noCopyIfContiguous](./accessmethod/nocopyifcontiguous.md)
  Return contiguous data from the backing of the [`MLXArray`](../mlxarray.md), avoiding a copy if possible. The lifetime of the result is valid only while keeping the [`MLXArray`](../mlxarray.md) alive.  This is best for temporary copies, e.g. creating and writing an image to disk.
### Default Implementations
- [Equatable Implementations](./accessmethod/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/accessmethod)*