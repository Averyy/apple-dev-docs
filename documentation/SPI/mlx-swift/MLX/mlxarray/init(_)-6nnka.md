---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(_:)-6nnka"
framework: "mlx-swift/MLX"
---

# init(_:)

**Framework**: mlx-swift/MLX  
**Kind**: init  
**Role**: Initializer

Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `Int` as a `Dtype.int32`.

## Declaration

```swift
convenience init(_ value: Int)
```

## Discussion

```swift
let a = MLXArray(7)
```

Note: if the value is out of bounds for an `Int32` the precondition will fail.  If you need an `Int` (`Int64`) scalar, please use [`init(int64:)`](./init%28int64%29-750va.md).

### See Also

- [Initialization](../initialization.md)
- [`init(int64:)`](./init%28int64%29-750va.md)

## See Also

### MLXArray Scalar Initializers
- [convenience init(Int32)](./init%28_%29-86r8u.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `Int32`.
- [convenience init(Bool)](./init%28_%29-9iiz7.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from a `Bool`.
- [convenience init(Float)](./init%28_%29-6zp01.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from a `Float`.
- [convenience init<T>(T)](./init%28_%29-10m.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from a `HasDType` value.
- [convenience init<T>(T, dtype: DType)](./init%28_,dtype%29.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from a `HasDType` value with a conversion to a given [`DType`](../dtype.md).
- [convenience init(bfloat16: Float32)](./init%28bfloat16%29.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` with a [`DType.bfloat16`](../dtype/bfloat16.md) from a `Float32`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(_:)-6nnka)*