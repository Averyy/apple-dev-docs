---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/initialization"
framework: "mlx-swift/MLX"
---

# Initialization

**Framework**: mlx-swift/MLX  
**Role**: API Collection

Creating MLXArrays.

### Scalar Arrays

A scalar [`MLXArray`](./mlxarray.md) is created from a scalar and has zero dimensions:

```swift
let v1 = MLXArray(true)
let v2 = MLXArray(7)
let v3 = MLXArray(8.5)
```

If an `MLXArray` of a different type is needed there is an initializer:

```swift
// dtype is .float32
let v4 = MLXArray(8.5)

// dtype is .float16
let v5 = MLXArray(Float16(8.5))

// dtype is .float16
let v6 = MLXArray(8.5, dtype: .float16)
```

Sometimes scalars can be used in place of arrays (no need to explicitly create them). Some functions and operators that work on [`MLXArray`](./mlxarray.md) take a [`ScalarOrArray`](./scalarorarray.md) argument or have an overload that does.  A sampling:

- [`+(_:_:)`](./mlxarray/plus%28_,_%29-2vili.md)
- [`+(_:_:)`](./mlxarray/plus%28_,_%29-1jn5i.md)
- [`minimum(_:_:stream:)`](./minimum%28_,_,stream%29.md)
- [`pow(_:_:stream:)`](./pow%28_,_,stream%29-7pe7j.md)
- [`pow(_:_:stream:)`](./pow%28_,_,stream%29-49xi0.md)

[`ScalarOrArray`](./scalarorarray.md) is a protocol that various numeric types (`Int`, `Float`, etc.) implement and it provides a method to convert the scalar to an [`MLXArray`](./mlxarray.md) using a suggested [`DType`](./dtype.md).  This allows:

```swift
let values: [Float16] = [ 0.5, 1.0, 2.5 ]

// a has dtype .float16
let a = MLXArray(values)

// b also has dtype .float16 because this translates (roughly) to:
// t = Int(3).asMLXArray(dtype: .float16)
// let b = a + t
let b = a + 3
```

Scalars will not promote results to `float32` using these functions.

### Int vs Int32 vs Int64

In swift an Int is a 64 bit value (aka Int64).  You can get 32 bit values by using:

```swift
let i = Int32(10)
```

In MLX the preferred integer type is [`DType.int32`](./dtype/int32.md) or smaller.  You can create an [`MLXArray`](./mlxarray.md) with an Int32 like this:

```swift
let a = MLXArray(Int32(10))
```

but as a convenience you can also create them like this:

```swift
// also int32!
let a = MLXArray(10)
```

If the value is out of range you will get an error pointing you to the alternate initializer:

```swift
// array creation with Int -- we want it to produce .int32
let a1 = MLXArray(500)
XCTAssertEqual(a1.dtype, .int32)

// eplicit int64
let a2 = MLXArray(int64: 500)
XCTAssertEqual(a2.dtype, .int64)
```

All of the `Int` initializers (e.g. `[Int]`, `Sequence<Int>` and nested arrays) work the same way and all have the `int64:` variant.

### Double

If you have a `Double` array, you have to convert it as `MLXArray` does not support `Double`:

```swift
// this converts to a Float array behind the scenes
let v1 = MLXArray(converting: [0.1, 0.5])
```

### Multi Value Arrays

Typically MLXArrays are created with many values and potentially many dimensions.  You can create an MLXArray from another array (literal in this case, but swift `Array` variables work as well):

```swift
// create an array of Int64 with shape [3]
let v1 = MLXArray([1, 2, 3])
```

You can also create an array from a swift `Sequence`:

```swift
// create an array of shape [12] from a sequence
let v1 = MLXArray(0 ..< 12)

// this works with various types of sequences
let v2 = MLXArray(stride(from: Float(0.5), to: Float(1.5), by: Float(0.1)))
```

Multiple dimensions can be given directly as a nested array, in which case, the shape is inferred from the nesting.

```swift
// create an array of Int32 with shape [2, 3]
let v1 = MLXArray([[1, 2, 3],
                   [4, 5, 6]])

// any depth of nesting works -- shape [2, 2, 2]
let v2 = MLXArray([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
```

Nested arrays must be tensors: every element at a given level must have the same shape.

If you have `Data` or a `UnsafePointer` (of various kinds) you can also create an `MLXArray` from that:

```swift
let data = Data([1, 2, 3, 4])

// directly from Data
let v1 = MLXArray(data, type: UInt8.self)

// or via a pointer
let v2 = data.withUnsafeBytes { ptr in
    MLXArray(ptr, type: UInt8.self)
}
```

When creating using an array or sequence you can also control the shape:

```swift
let v1 = MLXArray(0 ..< 12, [3, 4])
```

### Random Value Arrays

See also `MLXRandom` for creating arrays with random data.

### Other Arrays

There are a number of factory methods to create common array patterns.  For example:

```swift
// an array full of zeros
let zeros = MLXArray.zeros([5, 5])

// 2-d identity array
let identity = MLXArray.identity(5)
```

### Complex Values

[`MLXArray`](./mlxarray.md) supports complex numbers, specifically a real and imaginary `Float32` as [`DType.complex64`](./dtype/complex64.md). MLX uses [swift-numerics](https://github.com/apple/swift-numerics/tree/main) to represent the `Complex` type, though there are a few functions for manipulating the individual pieces, see [Conversion](./conversion.md).

To create a complex scalar there are a few approaches:

```swift
let c1 = MLXArray(Complex(0, 1))
let c2 = MLXArray(real: 0, imaginary: 1)
```

You can use `Complex` to create an array of complex as well:

```swift
let c3 = MLXArray([Complex(2, 7), Complex(3, 8), Complex(4, 9)])
```

If you have two arrays that you want to combine you can use this pattern:

```swift
let r = MLXRandom.uniform(0.0 ..< 1.0, [100, 100])
let i = MLXRandom.uniform(0.0 ..< 1.0, [100, 100])

// dtype is .complex64
let c = r + i.asImaginary()
```

## Topics

### MLXArray Literal Initializers
- [convenience init(arrayLiteral: Int32...)](./mlxarray/init%28arrayliteral%29.md)
  Initializer allowing creation of 1d `MLXArray` from an array literal.
### MLXArray Scalar Initializers
- [convenience init(Int32)](./mlxarray/init%28_%29-86r8u.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `Int32`.
- [convenience init(Bool)](./mlxarray/init%28_%29-9iiz7.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from a `Bool`.
- [convenience init(Float)](./mlxarray/init%28_%29-6zp01.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from a `Float`.
- [convenience init(Int)](./mlxarray/init%28_%29-6nnka.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `Int` as a `Dtype.int32`.
- [convenience init<T>(T)](./mlxarray/init%28_%29-10m.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from a `HasDType` value.
- [convenience init<T>(T, dtype: DType)](./mlxarray/init%28_,dtype%29.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from a `HasDType` value with a conversion to a given [`DType`](./dtype.md).
- [convenience init(bfloat16: Float32)](./mlxarray/init%28bfloat16%29.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` with a [`DType.bfloat16`](./dtype/bfloat16.md) from a `Float32`.
### MLXArray Int Overrides
- [convenience init(Int)](./mlxarray/init%28_%29-6nnka.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `Int` as a `Dtype.int32`.
- [convenience init([Int], (some Collection<Int>)?)](./mlxarray/init%28_,_%29-97hqf.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `[Int]` as a `Dtype.int32`.
- [convenience init<N>([[N]])](./mlxarray/init%28_%29-1ocp6.md)
  Initializer allowing creation of a multi dimensional `MLXArray` from a nested array of `HasDType` values.
- [convenience init(int64: Int)](./mlxarray/init%28int64%29-750va.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `Int` as a `Dtype.int64`.
- [convenience init(int64: [Int], (some Collection<Int>)?)](./mlxarray/init%28int64,_%29-3hkzx.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `[Int]` as a `Dtype.int64`.
- [convenience init(int64: some Sequence<Int>, (some Collection<Int>)?)](./mlxarray/init%28int64,_%29-8xap9.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `[Int]` as a `Dtype.int64`.
- [convenience init<N>(int64: [[N]])](./mlxarray/init%28int64%29-4fpsp.md)
  Initializer allowing creation of a multi dimensional `MLXArray` from a nested array of `Int` as a `DType.int64`.
### MLXArray Array Initializers
- [convenience init<T>([T], (some Collection<Int>)?)](./mlxarray/init%28_,_%29-7autl.md)
  Initializer allowing creation of `MLXArray` from an array of `HasDType` values with an optional shape.
- [class MLXArray](./mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [convenience init([Int], (some Collection<Int>)?)](./mlxarray/init%28_,_%29-97hqf.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `[Int]` as a `Dtype.int32`.
- [convenience init(converting: [Double], (some Collection<Int>)?)](./mlxarray/init%28converting,_%29.md)
  Initializer allowing creation of `MLXArray` from an array of `Double` values with an optional shape.
- [convenience init(UnsafeRawBufferPointer, (some Collection<Int>)?, type: (some HasDType).Type)](./mlxarray/init%28_,_,type%29-7ktbj.md)
  Initializer allowing creation of `MLXArray` from a `UnsafeRawBufferPointer` filled with bytes of `HasDType` values with an optional shape.
- [convenience init(Data, (some Collection<Int>)?, type: (some HasDType).Type)](./mlxarray/init%28_,_,type%29-3fuk4.md)
  Initializer allowing creation of `MLXArray` from a `Data` filled with bytes of `HasDType` values with an optional shape.
### MLXArray Nested Array Initializers
- [convenience init<N>([[N]])](./mlxarray/init%28_%29-1ocp6.md)
  Initializer allowing creation of a multi dimensional `MLXArray` from a nested array of `HasDType` values.
- [convenience init<N>(int64: [[N]])](./mlxarray/init%28int64%29-4fpsp.md)
  Initializer allowing creation of a multi dimensional `MLXArray` from a nested array of `Int` as a `DType.int64`.
- [convenience init<N>(converting: [[N]])](./mlxarray/init%28converting%29.md)
  Initializer allowing creation of a multi dimensional `MLXArray` from a nested array of `Double` values.
### MLXArray Complex Initializers
- [convenience init(real: Float, imaginary: Float)](./mlxarray/init%28real,imaginary%29.md)
  Create a [`DType.complex64`](./dtype/complex64.md) scalar.
- [convenience init(Complex<Float>)](./mlxarray/init%28_%29-6iii5.md)
  Create a [`DType.complex64`](./dtype/complex64.md) scalar from `Complex<Float>`.
### MLXArray Factory Methods
- [static func zeros(some Collection<Int>, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./mlxarray/zeros%28_,type,stream%29.md)
  Construct an array of zeros.
- [class MLXArray](./mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [static func zeros(some Collection<Int>, dtype: DType, stream: StreamOrDevice) -> MLXArray](./mlxarray/zeros%28_,dtype,stream%29.md)
  Construct an array of zeros with a given [`DType`](./dtype.md)
- [static func ones(some Collection<Int>, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./mlxarray/ones%28_,type,stream%29.md)
  Construct an array of ones.
- [class MLXArray](./mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [static func ones(some Collection<Int>, dtype: DType, stream: StreamOrDevice) -> MLXArray](./mlxarray/ones%28_,dtype,stream%29.md)
  Construct an array of ones with a given [`DType`](./dtype.md)
- [static func eye(Int, m: Int?, k: Int, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./mlxarray/eye%28_,m,k,type,stream%29.md)
  Create an identity matrix or a general diagonal matrix.
- [static func full(some Collection<Int>, values: MLXArray, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./mlxarray/full%28_,values,type,stream%29.md)
  Construct an array with the given value.
- [static func full(some Collection<Int>, values: MLXArray, stream: StreamOrDevice) -> MLXArray](./mlxarray/full%28_,values,stream%29.md)
  Construct an array with the given value.
- [static func identity(Int, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./mlxarray/identity%28_,type,stream%29.md)
  Create a square identity matrix.
- [class MLXArray](./mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [class MLXArray](./mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [static func repeated(MLXArray, count: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/repeated%28_,count,axis,stream%29.md)
  Repeat an array along a specified axis.
- [static func repeated(MLXArray, count: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/repeated%28_,count,stream%29.md)
  Repeat a flattened array along axis 0.
- [static func `repeat`(MLXArray, count: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/repeat%28_,count,axis,stream%29.md)
  Repeat an array along a specified axis.
- [static func `repeat`(MLXArray, count: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/repeat%28_,count,stream%29.md)
  Repeat a flattened array along axis 0.
- [static func tri(Int, m: Int?, k: Int, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./mlxarray/tri%28_,m,k,type,stream%29.md)
  An array with ones at and below the given diagonal and zeros elsewhere.
### MLXArray Factory Free Methods
- [func zeros(some Collection<Int>, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./zeros%28_,type,stream%29.md)
  Construct an array of zeros.
- [func zeros(like: MLXArray, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./zeros%28like,dtype,stream%29.md)
  Construct an array of zeros.
- [func ones(some Collection<Int>, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./ones%28_,type,stream%29.md)
  Construct an array of ones.
- [func ones(like: MLXArray, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./ones%28like,dtype,stream%29.md)
  Construct an array of ones.
- [func eye(Int, m: Int?, k: Int, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./eye%28_,m,k,type,stream%29.md)
  Create an identity matrix or a general diagonal matrix.
- [func full(some Collection<Int>, values: some ScalarOrArray, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./full%28_,values,type,stream%29.md)
  Construct an array with the given value.
- [func full(some Collection<Int>, values: some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./full%28_,values,stream%29.md)
  Construct an array with the given value.
- [func identity(Int, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./identity%28_,type,stream%29.md)
  Create a square identity matrix.
- [func linspace<T>(T, T, count: Int, endpoint: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./linspace%28_,_,count,endpoint,dtype,stream%29-2b6eu.md)
  Generate `count` evenly spaced numbers over interval `[start, stop]`.
- [func linspace<T>(T, T, count: Int, endpoint: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./linspace%28_,_,count,endpoint,dtype,stream%29-8k1d2.md)
  Generate `count` evenly spaced numbers over interval `[start, stop]`.
- [static func repeated(MLXArray, count: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/repeated%28_,count,axis,stream%29.md)
  Repeat an array along a specified axis.
- [static func repeated(MLXArray, count: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/repeated%28_,count,stream%29.md)
  Repeat a flattened array along axis 0.
- [func `repeat`(MLXArray, count: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./repeat%28_,count,axis,stream%29.md)
  Repeat an array along a specified axis.
- [func `repeat`(MLXArray, count: Int, stream: StreamOrDevice) -> MLXArray](./repeat%28_,count,stream%29.md)
  Repeat a flattened array along axis 0.
- [func tri(Int, m: Int?, k: Int, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./tri%28_,m,k,type,stream%29.md)
  An array with ones at and below the given diagonal and zeros elsewhere.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/initialization)*