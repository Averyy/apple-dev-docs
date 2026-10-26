---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/dtype"
framework: "mlx-swift/MLX"
---

# DType

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

Enum wrapping `Cmlx.mlx_array_dtype`.

## Declaration

```swift
enum DType
```

#### Overview

This is typically not used directly, rather it is inferred from parameters that are [`HasDType`](./hasdtype.md), for example:

```swift
let ones = MLXArray.ones([2, 2], type: Int32.self)
```

provides [`DType.int32`](./dtype/int32.md) via [`dtype`](./hasdtype/dtype.md).

Some methods take a `dtype` directly for cases where it may not be possible to use a Swift type:

```swift
let bf = MLXArray(10.5, dtype: .bfloat16)
```

##### See Also

- [`HasDType`](./hasdtype.md)
- [`asType(_:stream:)`](./mlxarray/astype%28_,stream%29-6d44y.md)
- [`MLXArray`](./mlxarray.md)
- [`init(_:dtype:)`](./mlxarray/init%28_,dtype%29.md)

## Topics

### Structures
- [struct FInfo](./dtype/finfo-swift.struct.md)
  Floating point info.
### Enumeration Cases
- [DType.bfloat16](./dtype/bfloat16.md)
- [DType.bool](./dtype/bool.md)
- [DType.complex64](./dtype/complex64.md)
- [DType.float16](./dtype/float16.md)
- [DType.float32](./dtype/float32.md)
- [DType.float64](./dtype/float64.md)
- [DType.int16](./dtype/int16.md)
- [DType.int32](./dtype/int32.md)
- [DType.int64](./dtype/int64.md)
- [DType.int8](./dtype/int8.md)
- [DType.uint16](./dtype/uint16.md)
- [DType.uint32](./dtype/uint32.md)
- [DType.uint64](./dtype/uint64.md)
- [DType.uint8](./dtype/uint8.md)
### Instance Properties
- [var cmlxDtype: mlx_dtype](./dtype/cmlxdtype.md)
- [var finfo: DType.FInfo?](./dtype/finfo-swift.property.md)
  For floating point values return the floating point info, similar to `numpy.finfo`.
- [var greatestFiniteMagnitudeArray: MLXArray](./dtype/greatestfinitemagnitudearray.md)
  A scalar `MLXArray` containing the largest finite value for this dtype’s real floating-point component.
- [var isComplex: Bool](./dtype/iscomplex.md)
- [var isFloatingPoint: Bool](./dtype/isfloatingpoint.md)
- [var isInteger: Bool](./dtype/isinteger.md)
- [var isSignedInteger: Bool](./dtype/issignedinteger.md)
- [var size: Int](./dtype/size.md)
### Default Implementations
- [Decodable Implementations](./dtype/decodable-implementations.md)
- [Encodable Implementations](./dtype/encodable-implementations.md)
- [Equatable Implementations](./dtype/equatable-implementations.md)

## Relationships

### Conforms To
- [KernelTemplateArg](./kerneltemplatearg.md)
- Swift.CaseIterable
- Swift.Copyable
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Escapable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Data Types
- [protocol HasDType](./hasdtype.md)
  Protocol for types that can provide a [`DType`](./dtype.md)
- [protocol ScalarOrArray](./scalarorarray.md)
  Protocol for promoting a value (e.g. a scalar) to an MLXArray.
- [protocol NestedArrayElement](./nestedarrayelement.md)
  A value that can appear in a nested array used to create an [`MLXArray`](./mlxarray.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/dtype)*