---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(_:)-10m"
framework: "mlx-swift/MLX"
---

# init(_:)

**Framework**: mlx-swift/MLX  
**Kind**: init  
**Role**: Initializer

Initializer allowing creation of scalar (0-dimension) `MLXArray` from a `HasDType` value.

## Declaration

```swift
convenience init<T>(_ value: T) where T : HasDType
```

#### Discussion

```swift
let a = MLXArray(UInt64(7))
```

##### See Also

- [Initialization](../initialization.md)

## See Also

### MLXArray Scalar Initializers
- [convenience init(Int32)](./init%28_%29-86r8u.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `Int32`.
- [convenience init(Bool)](./init%28_%29-9iiz7.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from a `Bool`.
- [convenience init(Float)](./init%28_%29-6zp01.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from a `Float`.
- [convenience init(Int)](./init%28_%29-6nnka.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `Int` as a `Dtype.int32`.
- [convenience init<T>(T, dtype: DType)](./init%28_,dtype%29.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from a `HasDType` value with a conversion to a given [`DType`](../dtype.md).
- [convenience init(bfloat16: Float32)](./init%28bfloat16%29.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` with a [`DType.bfloat16`](../dtype/bfloat16.md) from a `Float32`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(_:)-10m)*