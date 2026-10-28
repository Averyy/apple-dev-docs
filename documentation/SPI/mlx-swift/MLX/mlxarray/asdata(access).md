---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/asdata(access:)"
framework: "mlx-swift/MLX"
---

# asData(access:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Return the contents as `Data` bytes in the native [`dtype`](./dtype.md).

## Declaration

```swift
func asData(access: MLXArray.AccessMethod = .copy) -> MLXArray.MLXArrayData
```

## Discussion

> **Note**: If you use [`MLXArray.AccessMethod.noCopy`](./accessmethod/nocopy.md) or [`MLXArray.AccessMethod.noCopyIfContiguous`](./accessmethod/nocopyifcontiguous.md) you must guarantee that the lifetime of the [`MLXArray`](../mlxarray.md) exceeds the lifetime of the result.

Callers can specify an [`MLXArray.AccessMethod`](./accessmethod.md) to cause the data to be in *contiguous* memory vs. whatever layout the backing actually has.  Callers can use [`strides`](./mlxarraydata/strides.md) if the data is not contiguous.

By default it will use [`MLXArray.AccessMethod.copy`](./accessmethod/copy.md) and will return a copy of the data in contiguous memory.

### See Also

- [Conversion](../conversion.md)
- [`asArray(_:)`](./asarray%28_%29.md)
- [`asMTLBuffer(device:noCopy:)`](./asmtlbuffer%28device,nocopy%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/asdata(access:))*