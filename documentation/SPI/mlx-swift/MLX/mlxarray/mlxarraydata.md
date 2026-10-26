---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/mlxarraydata"
framework: "mlx-swift/MLX"
---

# MLXArray.MLXArrayData

**Framework**: mlx-swift/MLX  
**Kind**: struct  
**Role**: Structure

Container for `Data` backing of [`MLXArray`](../mlxarray.md).

## Declaration

```swift
struct MLXArrayData
```

##### See Also

- [`asData(access:)`](./asdata%28access%29.md)

## Topics

### Instance Properties
- [let dType: DType](./mlxarraydata/dtype.md)
  The layout of a single items in the [`data`](./mlxarraydata/data.md)
- [let data: Data](./mlxarraydata/data.md)
  The bytes backing the [`MLXArray`](../mlxarray.md).
- [let shape: [Int]](./mlxarraydata/shape.md)
  Dimensions of the data when viewed as [`dType`](./mlxarraydata/dtype.md)
- [let strides: [Int]](./mlxarraydata/strides.md)
  Strides of the data in terms of the [`dType`](./mlxarraydata/dtype.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/mlxarraydata)*