---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/hasdtype"
framework: "mlx-swift/MLX"
---

# HasDType

**Framework**: mlx-swift/MLX  
**Kind**: protocol  
**Role**: Protocol

Protocol for types that can provide a [`DType`](./dtype.md)

## Declaration

```swift
protocol HasDType : ScalarOrArray
```

## Overview

This is used to extract the [`DType`](./dtype.md) for values pass in to [`MLXArray`](./mlxarray.md) implicitly where possible.

See also [`ScalarOrArray`](./scalarorarray.md).

## Topics

### Type Properties
- [static var dtype: DType](./hasdtype/dtype.md)
  Return the type’s [`DType`](./dtype.md)

## Relationships

### Inherits From
- [ScalarOrArray](./scalarorarray.md)
### Conforming Types
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
- [protocol ScalarOrArray](./scalarorarray.md)
  Protocol for promoting a value (e.g. a scalar) to an MLXArray.
- [protocol NestedArrayElement](./nestedarrayelement.md)
  A value that can appear in a nested array used to create an [`MLXArray`](./mlxarray.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/hasdtype)*