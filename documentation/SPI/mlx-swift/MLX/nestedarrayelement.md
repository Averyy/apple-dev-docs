---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nestedarrayelement"
framework: "mlx-swift/MLX"
---

# NestedArrayElement

**Framework**: mlx-swift/MLX  
**Kind**: protocol  
**Role**: Protocol

A value that can appear in a nested array used to create an [`MLXArray`](./mlxarray.md).

## Declaration

```swift
protocol NestedArrayElement
```

#### Overview

Conformance is recursive: the built-in [`HasDType`](./hasdtype.md) scalars conform and so does an `Array` of conforming values, adding one dimension.  A nested array therefore describes both the shape and the contents of an [`MLXArray`](./mlxarray.md):

```swift
// shape [2, 3]
let a = MLXArray([[1, 2, 3], [4, 5, 6]])
```

This exists to express the nested array initializers, e.g. [`init(_:)`](./mlxarray/init%28_%29-1ocp6.md) – there should be no need to conform your own types to it.

##### See Also

- [Initialization](./initialization.md)

## Topics

### Associated Types
- [associatedtype Scalar : HasDType](./nestedarrayelement/scalar.md)
  The scalar type at the leaves of the nesting, e.g. `Int` for `[[Int]]`.
### Instance Properties
- [var nestedShape: [Int]](./nestedarrayelement/nestedshape.md)
  The shape of the receiver.
### Instance Methods
- [func appendNestedScalars(to: inout [Self.Scalar])](./nestedarrayelement/appendnestedscalars%28to%29.md)
  Append the receiver’s scalars to `values` in row major order.
### Type Properties
- [static var nestedRank: Int](./nestedarrayelement/nestedrank.md)
  The number of dimensions this type contributes – `0` for a scalar, `1` for `[Scalar]`.

## Relationships

### Conforming Types
- [Array](./swift/array.md)
- [Bool](./swift/bool.md)
- [Complex](./complexmodule/complex.md)
- [Double](./swift/double.md)
- [Float](./swift/float.md)
- [Float16](./swift/float16.md)
- [Int](./swift/int.md)
- [Int16](./swift/int16.md)
- [Int32](./swift/int32.md)
- [Int64](./swift/int64.md)
- [Int8](./swift/int8.md)
- [UInt](./swift/uint.md)
- [UInt16](./swift/uint16.md)
- [UInt32](./swift/uint32.md)
- [UInt64](./swift/uint64.md)
- [UInt8](./swift/uint8.md)

## See Also

### Data Types
- [enum DType](./dtype.md)
  Enum wrapping `Cmlx.mlx_array_dtype`.
- [protocol HasDType](./hasdtype.md)
  Protocol for types that can provide a [`DType`](./dtype.md)
- [protocol ScalarOrArray](./scalarorarray.md)
  Protocol for promoting a value (e.g. a scalar) to an MLXArray.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nestedarrayelement)*