---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(_:dtype:)"
framework: "mlx-swift/MLX"
---

# init(_:dtype:)

**Framework**: mlx-swift/MLX  
**Kind**: init  
**Role**: Initializer

Initializer allowing creation of scalar (0-dimension) `MLXArray` from a `HasDType` value with a conversion to a given [`DType`](../dtype.md).

## Declaration

```swift
convenience init<T>(_ value: T, dtype: DType) where T : HasDType
```

## Discussion

```swift
let a = MLXArray(7.5, dtype: .float16)
```

### See Also

- [Initialization](../initialization.md)
- [`ScalarOrArray`](../scalarorarray.md)

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
- [convenience init<T>(T)](./init%28_%29-10m.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from a `HasDType` value.
- [convenience init(bfloat16: Float32)](./init%28bfloat16%29.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` with a [`DType.bfloat16`](../dtype/bfloat16.md) from a `Float32`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(_:dtype:))*