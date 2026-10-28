---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray"
framework: "mlx-swift/MLX"
---

# MLXArray

**Framework**: mlx-swift/MLX  
**Kind**: class  
**Role**: Class

An N dimensional array.  The main type in `mlx`.

## Declaration

```swift
final class MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)
- [Numpy Style Broadcasting](./broadcasting.md)
- [Running on iOS](./running-on-ios.md)

## Introduction

`MLXArray` is an N dimension array that can contain a variety of data types ([`DType`](./dtype.md)). `MLXArray` supports a wide range of functions and operations to manipulate it and is used as the basis for the `MLXNN` module which implements many layers that are the basis for building machine learning models.

```swift
// create an array from a swift array
let a1 = MLXArray([1, 2, 3])

// this holds Int32
print(a1.dtype)

// and has a shape of [3]
print(a1.shape)

// there are a variety of operators and functions that can be used
let a2 = sqrt(a1 * 3)
```

## Thread Safety

> **Note**: `MLXArray` is not thread safe.

Although `MLXArray` looks like a normal multidimensional array, it is actually far more sophisticated.  It actually holds a promise for future computations, see [Lazy Evaluation](./lazy-evaluation.md) and is thus not thread safe.  For example:

```swift
let a: MLXArray
let b: MLXArray

let c = a + b
```

`c` is not the result of `a + b` but rather a graph representing `a` and `b` (which in turn may be large unresolved graphs) and the `addition` operator that combines them.  It is not safe to create `c` in one thread and consume/evaluate it in another.

## Memory Safety

> **Note**: `MLXArray` is not memory safe.

Unlike swift `Array`, `MLXArray` is not memory safe – use caution when using indexing operators.

For example:

```swift
let a = MLXArray([0])
print(a[10000])
```

Will print a random value from outside `a`.

## Topics

### Creation
- [Initialization](./initialization.md)
  Creating MLXArrays.
### Arithmetic Operators and Functions
- [Arithmetic](./arithmetic.md)
  MLX supports a wide range of binary arithmetic operators.
- [Convolution](./convolution.md)
  Convolution operations.
- [Cumulative Operations](./cumulative.md)
  Operations that produce a cumulative result.
### Indexing
- [Indexes](./indexes.md)
  Functions to produce and consume array indexes.
- [Indexing](./indexing.md)
  Array subscripts.
- [Sorting](./sorting.md)
  Sorting and partitioning values and indices.
### Logical Operations
- [Logical Operators](./logical.md)
  Evaluating logical operations on MLXArray.
### Shapes
- [Shapes](./shapes.md)
  Shape is a term to describe the number and size of the dimensions of an N dimension (ND) array.
- [Reduction Functions](./reduction.md)
  Reduction or aggregation functions.
### Conversion and Data Types
- [Conversion](./conversion.md)
  Conversion functions.
### Structures
- [MLXArray.MLXArrayData](./mlxarray/mlxarraydata.md)
  Container for `Data` backing of [`MLXArray`](./mlxarray.md).
### Operators
- [static func *= (inout MLXArray, some ScalarOrArray)](./mlxarray/stareq%28_,_%29-56esu.md)
  Element-wise multiplication with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument and store the result in the left-hand side array.
- [static func *= (inout MLXArray, MLXArray)](./mlxarray/stareq%28_,_%29-p75g.md)
  Element-wise multiplication.
- [static func += (inout MLXArray, some ScalarOrArray)](./mlxarray/pluseq%28_,_%29-25gsg.md)
  Element-wise addition with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument and store the result in the left-hand side array.
- [static func += (inout MLXArray, MLXArray)](./mlxarray/pluseq%28_,_%29-6c7kn.md)
  Element-wise addition.
- [static func - (MLXArray, MLXArray) -> MLXArray](./mlxarray/minus%28_,_%29-7frdo.md)
  Element-wise subtraction.
- [static func - (some ScalarOrArray, MLXArray) -> MLXArray](./mlxarray/minus%28_,_%29-971j0.md)
  Element-wise subtraction with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [static func - (MLXArray, some ScalarOrArray) -> MLXArray](./mlxarray/minus%28_,_%29-9mf3.md)
  Element-wise subtraction with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [static func -= (inout MLXArray, MLXArray)](./mlxarray/minuseq%28_,_%29-6t2l4.md)
  Element-wise subtraction.
- [static func -= (inout MLXArray, some ScalarOrArray)](./mlxarray/minuseq%28_,_%29-7kpim.md)
  Element-wise subtraction with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument and store the result in the left-hand side array.
- [static func / (MLXArray, some ScalarOrArray) -> MLXArray](./mlxarray/op%28_,_%29-24oh0.md)
  Element-wise division with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [static func / (MLXArray, MLXArray) -> MLXArray](./mlxarray/op%28_,_%29-6ijef.md)
  Element-wise division.
- [static func / (some ScalarOrArray, MLXArray) -> MLXArray](./mlxarray/op%28_,_%29-7cmtz.md)
  Element-wise division with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [static func /= (inout MLXArray, MLXArray)](./mlxarray/opeq%28_,_%29-si8w.md)
  Element-wise division.
- [static func /= (inout MLXArray, some ScalarOrArray)](./mlxarray/opeq%28_,_%29-u6xd.md)
  Element-wise division with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument and store the result in the left-hand side array.
### Initializers
- [init(consuming mlx_array)](./mlxarray/init%28_%29-8z7u6.md)
  Initialize with the given +1 context (transfer ownership).
- [convenience init<S>(S, (some Collection<Int>)?)](./mlxarray/init%28_,_%29-4l41j.md)
  Initializer allowing creation of `MLXArray` from a sequence of `HasDType` values with an optional shape.
- [convenience init<T>(UnsafeBufferPointer<T>, (some Collection<Int>)?)](./mlxarray/init%28_,_%29-798zt.md)
  Initializer allowing creation of `MLXArray` from a buffer of `HasDType` values with an optional shape.
- [convenience init(Data, (some Collection<Int>)?, dtype: DType)](./mlxarray/init%28_,_,dtype%29.md)
  Initializer allowing creation of `MLXArray` from a `Data`  buffer values with an optional shape and an explicit DType.
- [convenience init(data: MLXArray.MLXArrayData)](./mlxarray/init%28data%29.md)
- [convenience init(float64: Double)](./mlxarray/init%28float64%29.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from a `Double` as a `Dtype.float64`.
- [convenience init(rawPointer: UnsafeMutableRawPointer, (some Collection<Int>)?, dtype: DType, finalizer: () -> Void)](./mlxarray/init%28rawpointer,_,dtype,finalizer%29.md)
  Initialize an MLXArray by transferring ownership of a raw pointer.
### Instance Properties
- [var at: ArrayAt](./mlxarray/at.md)
  Used to apply update at given indices.
- [var count: Int](./mlxarray/count.md)
  Number of elements in the 0th dimension.
- [var ctx: mlx_array](./mlxarray/ctx.md)
  Internal pointer to the mlx-c wrapper on `mlx::core::array`, used with `Cmlx` interop.
- [var dtype: DType](./mlxarray/dtype.md)
  Data type of the elements in the array.
- [var itemSize: Int](./mlxarray/itemsize.md)
  Number of bytes per element
- [var nbytes: Int](./mlxarray/nbytes.md)
  Number of bytes in the array.
- [var ndim: Int](./mlxarray/ndim.md)
  Number of dimensions in the array.
- [var size: Int](./mlxarray/size.md)
  Total number of elements in the array
- [var strides: [Int]](./mlxarray/strides.md)
  Strides of the array.  Note: do not use this as it changes before and after evaluation.  See also [`asData(access:)`](./mlxarray/asdata%28access%29.md) and [`strides`](./mlxarray/mlxarraydata/strides.md).
### Instance Methods
- [func asData(access: MLXArray.AccessMethod) -> MLXArray.MLXArrayData](./mlxarray/asdata%28access%29.md)
  Return the contents as `Data` bytes in the native [`dtype`](./mlxarray/dtype.md).
- [func asData(noCopy: Bool, disambiguate: Bool) -> Data](./mlxarray/asdata%28nocopy,disambiguate%29.md)
  Return the contents as contiguous bytes in the native [`dtype`](./mlxarray/dtype.md).
- [func asType((some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./mlxarray/astype%28_,stream%29-4eqoc.md)
  Create a new `MLXArray` with the contents converted to the given type, e.g. `Float.self`.
- [func contiguous(allowColMajor: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/contiguous%28allowcolmajor,stream%29.md)
  Force an array to be row contiguous. Copy if necessary.
- [func cumprod(reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./mlxarray/cumprod%28reverse,inclusive,dtype,stream%29.md)
  Return the cumulative product of the elements over the flattened array.
- [func cumsum(reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./mlxarray/cumsum%28reverse,inclusive,dtype,stream%29.md)
  Return the cumulative sum of the elements over the flattened array.
- [func diag(k: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/diag%28k,stream%29.md)
  Extract a diagonal or construct a diagonal matrix.
- [func diagonal(offset: Int, axis1: Int, axis2: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/diagonal%28offset,axis1,axis2,stream%29.md)
  Return specified diagonals.
- [func eval()](./mlxarray/eval%28%29.md)
  Evaluate the array.
- [func item<T>() -> T](./mlxarray/item%28%29.md)
  Return the scalar value of the array.
- [func item<T>(T.Type) -> T](./mlxarray/item%28_%29.md)
  Return the scalar value of the array.
- [func l2Normalized(axis: Int, eps: Float) -> MLXArray](./mlxarray/l2normalized%28axis,eps%29.md)
  Returns a new array normalized by its L2 norm along the specified axis.
- [func take(MLXArray, stream: StreamOrDevice) -> MLXArray](./mlxarray/take%28_,stream%29.md)
  Take elements from flattened 1-D array.
- [func view(dtype: DType, stream: StreamOrDevice) -> MLXArray](./mlxarray/view%28dtype,stream%29.md)
  View the array as a different type.
### Type Properties
- [static var mlxNone: MLXArray](./mlxarray/mlxnone.md)
  return the equivalent of a `.none` MLXArray (for the C API).
### Type Methods
- [static func arange(Double, Double, step: Double, dtype: DType, stream: StreamOrDevice) -> MLXArray](./mlxarray/arange%28_,_,step,dtype,stream%29-493i3.md)
  Generate values in the half-open interval `[start, stop)` spaced by `step` (floating point version).
- [static func arange(Int, Int, step: Int, dtype: DType, stream: StreamOrDevice) -> MLXArray](./mlxarray/arange%28_,_,step,dtype,stream%29-5h4mf.md)
  Generate values in the half-open interval `[start, stop)` spaced by `step` with a given [`DType`](./dtype.md).
- [static func arange(Int, Int, step: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/arange%28_,_,step,stream%29.md)
  Generate values in the half-open interval `[start, stop)` spaced by `step`.
- [static func arange(Double, dtype: DType, stream: StreamOrDevice) -> MLXArray](./mlxarray/arange%28_,dtype,stream%29-4b7j6.md)
  Generate values in the half-open interval `[0, stop)` (floating point version).
- [static func arange(Int, dtype: DType, stream: StreamOrDevice) -> MLXArray](./mlxarray/arange%28_,dtype,stream%29-85kbk.md)
  Generate values in the half-open interval `[0, stop)` with a given [`DType`](./dtype.md).
- [static func arange(Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/arange%28_,stream%29.md)
  Generate values in the half-open interval `[0, stop)`.
- [static func eye(Int, m: Int?, k: Int, dtype: DType, stream: StreamOrDevice) -> MLXArray](./mlxarray/eye%28_,m,k,dtype,stream%29.md)
  Create an identity matrix or a general diagonal matrix given a [`DType`](./dtype.md).
- [static func full(some Collection<Int>, values: MLXArray, dtype: DType, stream: StreamOrDevice) -> MLXArray](./mlxarray/full%28_,values,dtype,stream%29.md)
  Construct an array with the given value and a given [`DType`](./dtype.md).
- [static func identity(Int, dtype: DType, stream: StreamOrDevice) -> MLXArray](./mlxarray/identity%28_,dtype,stream%29.md)
  Create a square identity matrix with a given [`DType`](./dtype.md).
- [static func linspace<T>(T, T, count: Int, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./mlxarray/linspace%28_,_,count,dtype,stream%29-3fx01.md)
  Generate `count` evenly spaced numbers over interval `[start, stop]` for `BinaryInteger`.
- [static func linspace<T>(T, T, count: Int, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./mlxarray/linspace%28_,_,count,dtype,stream%29-9yqai.md)
  Generate `count` evenly spaced numbers over interval `[start, stop]` for `BinaryFloatingPoint`.
- [static func maskFill(for: DType) -> MLXArray](./mlxarray/maskfill%28for%29.md)
  Scalar masked-score fill (`-finfo(dtype).max`) constructed directly in `dtype`, so masked positions vanish under softmax — no `asType` to forget.
- [static func ones(like: MLXArray, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./mlxarray/ones%28like,dtype,stream%29.md)
  Construct an array of ones.
- [static func tri(Int, m: Int?, k: Int, dtype: DType, stream: StreamOrDevice) -> MLXArray](./mlxarray/tri%28_,m,k,dtype,stream%29.md)
  An array with ones at and below the given diagonal and zeros elsewhere and a given [`DType`](./dtype.md).
- [static func zeros(like: MLXArray, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./mlxarray/zeros%28like,dtype,stream%29.md)
  Construct an array of zeros.
### Enumerations
- [MLXArray.AccessMethod](./mlxarray/accessmethod.md)
  How to access backing data with [`asData(access:)`](./mlxarray/asdata%28access%29.md) – this controls how [`MLXArray.MLXArrayData`](./mlxarray/mlxarraydata.md) is produced.
### Default Implementations
- [CustomStringConvertible Implementations](./mlxarray/customstringconvertible-implementations.md)
- [ExpressibleByArrayLiteral Implementations](./mlxarray/expressiblebyarrayliteral-implementations.md)
- [MLXArrayIndex Implementations](./mlxarray/mlxarrayindex-implementations.md)
- [RandomStateOrKey Implementations](./mlxarray/randomstateorkey-implementations.md)
- [ScalarOrArray Implementations](./mlxarray/scalarorarray-implementations.md)
- [Sequence Implementations](./mlxarray/sequence-implementations.md)
- [Updatable Implementations](./mlxarray/updatable-implementations.md)

## Relationships

### Conforms To
- [Evaluatable](./evaluatable.md)
- [MLXArrayIndex](./mlxarrayindex.md)
- [RandomStateOrKey](./randomstateorkey.md)
- [ScalarOrArray](./scalarorarray.md)
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Escapable
- Swift.ExpressibleByArrayLiteral
- Swift.Sequence
- [Updatable](./updatable.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray)*