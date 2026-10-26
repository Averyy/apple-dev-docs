---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arithmetic"
framework: "mlx-swift/MLX"
---

# Arithmetic

**Framework**: mlx-swift/MLX  
**Role**: API Collection

MLX supports a wide range of binary arithmetic operators.

#### Overview

Many of the operations are avilable as infix operators (e.g. ‘+’) or as functions, either on MLXArray itself or as free functions.

```swift
let a = MLXArray(0 ..< 12, [4, 3])
let b = MLXArray([4, 5, 6])

// these are equivalent
let r1 = a + b + 7
let r2 = add(add(a, b), 7)
```

There are also a wide variety of element-wise math functions:

```swift
let a = MLXArray(0 ..< 12, [4, 3])

let r = log(a)
```

> **Note**: There are two operators from python that are not supported (as operators) in swift: `@` ([`matmul(_:_:stream:)`](./matmul%28_,_,stream%29.md)) and `//` ([`floorDivide(_:_:stream:)`](./floordivide%28_,_,stream%29.md)).  Please use the methods on `MLXArray` or the free functions.

#### Swift Naming

Note that the element-wise logical operations such as:

- [`.==(_:_:)`](./mlxarray/doteqeq%28_,_%29-56m0a.md)
- [`.==(_:_:)`](./mlxarray/doteqeq%28_,_%29-79hbc.md)

are named using the Swift convention for SIMD operations, e.g. `.==`, `.<`, etc.  These operators produce a new [`MLXArray`](./mlxarray.md) with `true`/`false` values for the elementwise comparison.

#### Operations With Scalars

Many functions and operators that work on [`MLXArray`](./mlxarray.md) take a [`ScalarOrArray`](./scalarorarray.md) argument or have an overload that does.  A sampling:

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

## Topics

### MLXArray Operators
- [static func + (MLXArray, MLXArray) -> MLXArray](./mlxarray/plus%28_,_%29-1rv98.md)
  Element-wise addition.
- [static func + (MLXArray, some ScalarOrArray) -> MLXArray](./mlxarray/plus%28_,_%29-2vili.md)
  Element-wise addition with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [static func + (some ScalarOrArray, MLXArray) -> MLXArray](./mlxarray/plus%28_,_%29-1jn5i.md)
  Element-wise addition with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [class MLXArray](./mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [static func * (MLXArray, MLXArray) -> MLXArray](./mlxarray/star%28_,_%29-1z2ck.md)
  Element-wise multiplication.
- [static func * (MLXArray, some ScalarOrArray) -> MLXArray](./mlxarray/star%28_,_%29-sw3w.md)
  Element-wise multiplication with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [static func * (some ScalarOrArray, MLXArray) -> MLXArray](./mlxarray/star%28_,_%29-7441r.md)
  Element-wise multiplication with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [static func ** (MLXArray, MLXArray) -> MLXArray](./mlxarray/starstar%28_,_%29-8xxt3.md)
  Element-wise power operation.
- [static func ** (MLXArray, some ScalarOrArray) -> MLXArray](./mlxarray/starstar%28_,_%29-6ve5u.md)
  Element-wise power with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [static func ** (some ScalarOrArray, MLXArray) -> MLXArray](./mlxarray/starstar%28_,_%29-4lp4b.md)
  Element-wise power with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [static func % (MLXArray, MLXArray) -> MLXArray](./mlxarray/op%28_,_%29-3ubwd.md)
  Element-wise remainder of division.
- [static func % (some ScalarOrArray, MLXArray) -> MLXArray](./mlxarray/op%28_,_%29-8az7l.md)
  Element-wise remainder with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [static func % (MLXArray, some ScalarOrArray) -> MLXArray](./mlxarray/op%28_,_%29-516wd.md)
  Element-wise remainder with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [static func .! (MLXArray) -> MLXArray](./mlxarray/dotnot%28_%29.md)
  Unary element-wise logical not.
- [static func .== (MLXArray, MLXArray) -> MLXArray](./mlxarray/doteqeq%28_,_%29-56m0a.md)
  Element-wise equality.
- [static func .== (MLXArray, some ScalarOrArray) -> MLXArray](./mlxarray/doteqeq%28_,_%29-79hbc.md)
  Element-wise equality with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [static func .!= (MLXArray, MLXArray) -> MLXArray](./mlxarray/dotnoteq%28_,_%29-mbw0.md)
  Element-wise not equal.
- [static func .!= (MLXArray, some ScalarOrArray) -> MLXArray](./mlxarray/dotnoteq%28_,_%29-gkdj.md)
  Element-wise not equal with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [static func .< (MLXArray, MLXArray) -> MLXArray](./mlxarray/dotop%28_,_%29-9rzup.md)
  Element-wise less than.
- [static func .< (MLXArray, some ScalarOrArray) -> MLXArray](./mlxarray/dotop%28_,_%29-54ivt.md)
  Element-wise less than with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [static func .<= (MLXArray, MLXArray) -> MLXArray](./mlxarray/dotopeq%28_,_%29-2a0s9.md)
  Element-wise less than or equal.
- [static func .<= (MLXArray, some ScalarOrArray) -> MLXArray](./mlxarray/dotopeq%28_,_%29-6vb92.md)
  Element-wise less than or equal with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [static func .> (MLXArray, MLXArray) -> MLXArray](./mlxarray/dotop%28_,_%29-fwi1.md)
  Element-wise greater than.
- [static func .> (MLXArray, some ScalarOrArray) -> MLXArray](./mlxarray/dotop%28_,_%29-2v86b.md)
  Element-wise greater than with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [static func .>= (MLXArray, MLXArray) -> MLXArray](./mlxarray/dotopeq%28_,_%29-2gqml.md)
  Element-wise less greater than or equal.
- [static func .>= (MLXArray, some ScalarOrArray) -> MLXArray](./mlxarray/dotopeq%28_,_%29-6zxj9.md)
  Element-wise greater than or equal with a [`ScalarOrArray`](./scalarorarray.md) (scalar) argument.
- [static func .&& (MLXArray, MLXArray) -> MLXArray](./mlxarray/dotampamp%28_,_%29.md)
  Element-wise logical and.
- [static func .|| (MLXArray, MLXArray) -> MLXArray](./mlxarray/dotopop%28_,_%29.md)
  Element-wise logical or.
- [static func ~ (MLXArray) -> MLXArray](./mlxarray/tilde%28_%29.md)
  Unary element-wise bitwise invert.
- [static func & (MLXArray, MLXArray) -> MLXArray](./mlxarray/amp%28_,_%29-9in7a.md)
  Element-wise bitwise and.
- [static func & (MLXArray, some ScalarOrArray) -> MLXArray](./mlxarray/amp%28_,_%29-8js41.md)
  Element-wise bitwise and.
- [static func & (some ScalarOrArray, MLXArray) -> MLXArray](./mlxarray/amp%28_,_%29-7iu4h.md)
  Element-wise bitwise and.
- [static func | (MLXArray, MLXArray) -> MLXArray](./mlxarray/op%28_,_%29-2upd6.md)
  Element-wise bitwise or.
- [static func | (MLXArray, some ScalarOrArray) -> MLXArray](./mlxarray/op%28_,_%29-35lfz.md)
  Element-wise bitwise or.
- [static func | (some ScalarOrArray, MLXArray) -> MLXArray](./mlxarray/op%28_,_%29-7c6lr.md)
  Element-wise bitwise or.
- [static func ^ (MLXArray, MLXArray) -> MLXArray](./mlxarray/op%28_,_%29-8hj69.md)
  Element-wise bitwise xor.
- [static func ^ (MLXArray, some ScalarOrArray) -> MLXArray](./mlxarray/op%28_,_%29-2oktd.md)
  Element-wise bitwise xor.
- [static func ^ (some ScalarOrArray, MLXArray) -> MLXArray](./mlxarray/op%28_,_%29-dik7.md)
  Element-wise bitwise xor.
- [static func << (MLXArray, MLXArray) -> MLXArray](./mlxarray/opop%28_,_%29-1dfss.md)
  Element-wise left shift.
- [static func << (MLXArray, some ScalarOrArray) -> MLXArray](./mlxarray/opop%28_,_%29-80u2m.md)
  Element-wise left shift.
- [static func << (some ScalarOrArray, MLXArray) -> MLXArray](./mlxarray/opop%28_,_%29-7hmgt.md)
  Element-wise left shift.
- [static func >> (MLXArray, MLXArray) -> MLXArray](./mlxarray/opop%28_,_%29-zpp3.md)
  Element-wise right shift.
- [static func >> (MLXArray, some ScalarOrArray) -> MLXArray](./mlxarray/opop%28_,_%29-4z891.md)
  Element-wise right shift.
- [static func >> (some ScalarOrArray, MLXArray) -> MLXArray](./mlxarray/opop%28_,_%29-89b4j.md)
  Element-wise right shift.
### MLXArray Element-wise Arithmetic Functions
- [func abs(stream: StreamOrDevice) -> MLXArray](./mlxarray/abs%28stream%29.md)
  Element-wise absolute value.
- [func conjugate(stream: StreamOrDevice) -> MLXArray](./mlxarray/conjugate%28stream%29.md)
  Element-wise complex conjugate of the input.
- [func cos(stream: StreamOrDevice) -> MLXArray](./mlxarray/cos%28stream%29.md)
  Element-wise cosine.
- [func exp(stream: StreamOrDevice) -> MLXArray](./mlxarray/exp%28stream%29.md)
  Element-wise exponential.
- [func floor(stream: StreamOrDevice) -> MLXArray](./mlxarray/floor%28stream%29.md)
  Element-wise floor.
- [func floorDivide(some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./mlxarray/floordivide%28_,stream%29.md)
  Element-wise integer division..
- [func log(stream: StreamOrDevice) -> MLXArray](./mlxarray/log%28stream%29.md)
  Element-wise natural logarithm.
- [func log2(stream: StreamOrDevice) -> MLXArray](./mlxarray/log2%28stream%29.md)
  Element-wise base-2 logarithm.
- [func log10(stream: StreamOrDevice) -> MLXArray](./mlxarray/log10%28stream%29.md)
  Element-wise base-10 logarithm.
- [func log1p(stream: StreamOrDevice) -> MLXArray](./mlxarray/log1p%28stream%29.md)
  Element-wise natural log of one plus the array.
- [func pow(some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./mlxarray/pow%28_,stream%29.md)
  Element-wise power operation.
- [func reciprocal(stream: StreamOrDevice) -> MLXArray](./mlxarray/reciprocal%28stream%29.md)
  Element-wise reciprocal.
- [func rsqrt(stream: StreamOrDevice) -> MLXArray](./mlxarray/rsqrt%28stream%29.md)
  Element-wise reciprocal and square root.
- [func round(decimals: Int, stream: StreamOrDevice) -> MLXArray](./mlxarray/round%28decimals,stream%29.md)
  Round to the given number of decimals.
- [func sin(stream: StreamOrDevice) -> MLXArray](./mlxarray/sin%28stream%29.md)
  Element-wise sine.
- [func sqrt(stream: StreamOrDevice) -> MLXArray](./mlxarray/sqrt%28stream%29.md)
  Element-wise square root
- [func square(stream: StreamOrDevice) -> MLXArray](./mlxarray/square%28stream%29.md)
  Element-wise square.
### Element-wise Arithmetic Free Functions
- [func abs(MLXArray, stream: StreamOrDevice) -> MLXArray](./abs%28_,stream%29.md)
  Element-wise absolute value.
- [func acos(MLXArray, stream: StreamOrDevice) -> MLXArray](./acos%28_,stream%29.md)
  Element-wise inverse cosine.
- [func acosh(MLXArray, stream: StreamOrDevice) -> MLXArray](./acosh%28_,stream%29.md)
  Element-wise inverse hyperbolic cosine.
- [func add(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./add%28_,_,stream%29.md)
  Element-wise addition.
- [func asin(MLXArray, stream: StreamOrDevice) -> MLXArray](./asin%28_,stream%29.md)
  Element-wise inverse sine.
- [func asinh(MLXArray, stream: StreamOrDevice) -> MLXArray](./asinh%28_,stream%29.md)
  Element-wise inverse hyperbolic sine.
- [func atan(MLXArray, stream: StreamOrDevice) -> MLXArray](./atan%28_,stream%29.md)
  Element-wise inverse tangent.
- [func atan2(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./atan2%28_,_,stream%29.md)
  Element-wise inverse tangent of the ratio of two arrays.
- [func atanh(MLXArray, stream: StreamOrDevice) -> MLXArray](./atanh%28_,stream%29.md)
  Element-wise inverse hyperbolic tangent.
- [func bitwiseAnd(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./bitwiseand%28_,_,stream%29.md)
  Element-wise bitwise and.
- [func bitwiseInvert(MLXArray, stream: StreamOrDevice) -> MLXArray](./bitwiseinvert%28_,stream%29.md)
  Unary element-wise bitwise invert.
- [func bitwiseOr(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./bitwiseor%28_,_,stream%29.md)
  Element-wise bitwise or.
- [func bitwiseXOr(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./bitwisexor%28_,_,stream%29.md)
  Element-wise bitwise xor.
- [func ceil(MLXArray, stream: StreamOrDevice) -> MLXArray](./ceil%28_,stream%29.md)
  Element-wise ceil.
- [func clip(MLXArray, min: some ScalarOrArray, max: some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./clip%28_,min,max,stream%29.md)
  Clip the values of the array between the given minimum and maximum.
- [func conjugate(MLXArray, stream: StreamOrDevice) -> MLXArray](./conjugate%28_,stream%29.md)
  Element-wise complex conjugate of the input.
- [func cos(MLXArray, stream: StreamOrDevice) -> MLXArray](./cos%28_,stream%29.md)
  Element-wise cosine.
- [func cosh(MLXArray, stream: StreamOrDevice) -> MLXArray](./cosh%28_,stream%29.md)
  Element-wise hyperbolic cosine.
- [func degrees(MLXArray, stream: StreamOrDevice) -> MLXArray](./degrees%28_,stream%29.md)
  Convert angles from radians to degrees.
- [func divide(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./divide%28_,_,stream%29.md)
  Element-wise division.
- [func divmod(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./divmod%28_,_,stream%29.md)
  Element-wise quotient and remainder.
- [func erf(MLXArray, stream: StreamOrDevice) -> MLXArray](./erf%28_,stream%29.md)
  Element-wise error function.
- [func erfInverse(MLXArray, stream: StreamOrDevice) -> MLXArray](./erfinverse%28_,stream%29.md)
  Element-wise inverse of [`erf(_:stream:)`](./erf%28_,stream%29.md).
- [func exp(MLXArray, stream: StreamOrDevice) -> MLXArray](./exp%28_,stream%29.md)
  Element-wise exponential.
- [func expm1(MLXArray, stream: StreamOrDevice) -> MLXArray](./expm1%28_,stream%29.md)
  Element-wise exponential minus 1.
- [func floor(MLXArray, stream: StreamOrDevice) -> MLXArray](./floor%28_,stream%29.md)
  Element-wise floor.
- [func floorDivide(MLXArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./floordivide%28_,_,stream%29.md)
  Element-wise integer division..
- [func isNaN(MLXArray, stream: StreamOrDevice) -> MLXArray](./isnan%28_,stream%29.md)
  Return a boolean array indicating which elements are NaN.
- [func isInf(MLXArray, stream: StreamOrDevice) -> MLXArray](./isinf%28_,stream%29.md)
  Return a boolean array indicating which elements are infinity.
- [func isFinite(MLXArray, stream: StreamOrDevice) -> MLXArray](./isfinite%28_,stream%29.md)
  Return a boolean array indicating which elements are finite.
- [func isPosInf(MLXArray, stream: StreamOrDevice) -> MLXArray](./isposinf%28_,stream%29.md)
  Return a boolean array indicating which elements are positive infinity.
- [func isNegInf(MLXArray, stream: StreamOrDevice) -> MLXArray](./isneginf%28_,stream%29.md)
  Return a boolean array indicating which elements are negative infinity.
- [func leftShift(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./leftshift%28_,_,stream%29.md)
  Element-wise left shift.
- [func log(MLXArray, stream: StreamOrDevice) -> MLXArray](./log%28_,stream%29.md)
  Element-wise natural logarithm.
- [func log10(MLXArray, stream: StreamOrDevice) -> MLXArray](./log10%28_,stream%29.md)
  Element-wise base-10 logarithm.
- [func log1p(MLXArray, stream: StreamOrDevice) -> MLXArray](./log1p%28_,stream%29.md)
  Element-wise natural log of one plus the array.
- [func log2(MLXArray, stream: StreamOrDevice) -> MLXArray](./log2%28_,stream%29.md)
  Element-wise base-2 logarithm.
- [func logAddExp(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./logaddexp%28_,_,stream%29.md)
  Element-wise log-add-exp.
- [func logicalAnd(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./logicaland%28_,_,stream%29.md)
  Element-wise logical and.
- [func logicalNot(MLXArray, stream: StreamOrDevice) -> MLXArray](./logicalnot%28_,stream%29.md)
  Element-wise logical not.
- [func logicalOr(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./logicalor%28_,_,stream%29.md)
  Element-wise logical or.
- [func logicalXor(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./logicalxor%28_,_,stream%29.md)
  Element-wise logical exclusive or.
- [func maximum(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./maximum%28_,_,stream%29.md)
  Element-wise maximum.
- [func minimum(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./minimum%28_,_,stream%29.md)
  Element-wise minimum.
- [func multiply(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./multiply%28_,_,stream%29.md)
  Element-wise multiplication.
- [func nanToNum(MLXArray, nan: Float, posInf: Float?, negInf: Float?, stream: StreamOrDevice) -> MLXArray](./nantonum%28_,nan,posinf,neginf,stream%29.md)
  Replace NaN and Inf values with finite numbers.
- [func negative(MLXArray, stream: StreamOrDevice) -> MLXArray](./negative%28_,stream%29.md)
  Element-wise negation.
- [func notEqual(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./notequal%28_,_,stream%29.md)
  Element-wise not equal.
- [func pow(MLXArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./pow%28_,_,stream%29-7pe7j.md)
  Element-wise power operation.
- [func pow(some ScalarOrArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./pow%28_,_,stream%29-49xi0.md)
  Element-wise power operation.
- [func pow(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./pow%28_,_,stream%29-8ie9c.md)
  Element-wise power operation.
- [func radians(MLXArray, stream: StreamOrDevice) -> MLXArray](./radians%28_,stream%29.md)
  Convert angles from degrees to radians.
- [func reciprocal(MLXArray, stream: StreamOrDevice) -> MLXArray](./reciprocal%28_,stream%29.md)
  Element-wise reciprocal.
- [func remainder(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./remainder%28_,_,stream%29.md)
  Element-wise remainder of division.
- [func rightShift(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./rightshift%28_,_,stream%29.md)
  Element-wise right shift.
- [func round(MLXArray, decimals: Int, stream: StreamOrDevice) -> MLXArray](./round%28_,decimals,stream%29.md)
  Round to the given number of decimals.
- [func rsqrt(MLXArray, stream: StreamOrDevice) -> MLXArray](./rsqrt%28_,stream%29.md)
  Element-wise reciprocal and square root.
- [func sigmoid(MLXArray, stream: StreamOrDevice) -> MLXArray](./sigmoid%28_,stream%29.md)
  Element-wise logistic sigmoid.
- [func sign(MLXArray, stream: StreamOrDevice) -> MLXArray](./sign%28_,stream%29.md)
  Element-wise sign.
- [func sin(MLXArray, stream: StreamOrDevice) -> MLXArray](./sin%28_,stream%29.md)
  Element-wise sine.
- [func sinh(MLXArray, stream: StreamOrDevice) -> MLXArray](./sinh%28_,stream%29.md)
  Element-wise hyperbolic sine.
- [func softmax(MLXArray, axes: some Collection<Int>, precise: Bool, stream: StreamOrDevice) -> MLXArray](./softmax%28_,axes,precise,stream%29.md)
  Perform the softmax along the given axis.
- [func sqrt(MLXArray, stream: StreamOrDevice) -> MLXArray](./sqrt%28_,stream%29.md)
  Element-wise square root
- [func square(MLXArray, stream: StreamOrDevice) -> MLXArray](./square%28_,stream%29.md)
  Element-wise square.
- [func subtract(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./subtract%28_,_,stream%29.md)
  Element-wise subtraction.
- [func tan(MLXArray, stream: StreamOrDevice) -> MLXArray](./tan%28_,stream%29.md)
  Element-wise tangent.
- [func tanh(MLXArray, stream: StreamOrDevice) -> MLXArray](./tanh%28_,stream%29.md)
  Element-wise hyperbolic tangent.
- [func trace(MLXArray, offset: Int, axis1: Int, axis2: Int, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./trace%28_,offset,axis1,axis2,dtype,stream%29.md)
  Return the sum along a specified diagonal in the given array.
- [func which(MLXArray, some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./which%28_,_,_,stream%29.md)
  Alias for [`where(_:_:_:stream:)`](./where%28_,_,_,stream%29.md) – select from `x` or `y` according to `condition`.
### Vector, Matrix, and Tensor Products
- [func matmul(MLXArray, stream: StreamOrDevice) -> MLXArray](./mlxarray/matmul%28_,stream%29.md)
  Matrix multiplication.
- [func matmul(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./matmul%28_,_,stream%29.md)
  Matrix multiplication.
- [func gatherMM(MLXArray, MLXArray, lhsIndices: MLXArray?, rhsIndices: MLXArray?, sortedIndices: Bool, stream: StreamOrDevice) -> MLXArray](./gathermm%28_,_,lhsindices,rhsindices,sortedindices,stream%29.md)
  Matrix multiplication with matrix-level gather.
- [func blockMaskedMM(MLXArray, MLXArray, blockSize: Int, maskOut: MLXArray?, maskLHS: MLXArray?, maskRHS: MLXArray?, stream: StreamOrDevice) -> MLXArray](./blockmaskedmm%28_,_,blocksize,maskout,masklhs,maskrhs,stream%29.md)
  Matrix multiplication with block masking.
- [func addMM(some ScalarOrArray, some ScalarOrArray, some ScalarOrArray, alpha: Float, beta: Float, stream: StreamOrDevice) -> MLXArray](./addmm%28_,_,_,alpha,beta,stream%29.md)
  Matrix multiplication with addition and optional scaling.
- [func quantizedMM(MLXArray, MLXArray, scales: MLXArray, biases: MLXArray?, transpose: Bool, groupSize: Int?, bits: Int?, mode: QuantizationMode, stream: StreamOrDevice) -> MLXArray](./quantizedmm%28_,_,scales,biases,transpose,groupsize,bits,mode,stream%29.md)
  Perform the matrix multiplication with the quantized matrix `w`. The quantization uses one floating point scale and bias per `group_size` of elements. Each element in `w` takes `bits` bits and is packed in an unsigned 32 bit integer.
- [func gatherQuantizedMM(MLXArray, MLXArray, scales: MLXArray, biases: MLXArray?, lhsIndices: MLXArray?, rhsIndices: MLXArray?, transpose: Bool, groupSize: Int?, bits: Int?, mode: QuantizationMode, sortedIndices: Bool, stream: StreamOrDevice) -> MLXArray](./gatherquantizedmm%28_,_,scales,biases,lhsindices,rhsindices,transpose,groupsize,bits,mode,sortedindices,stream%29.md)
  Perform quantized matrix multiplication with matrix-level gather.
- [func quantizedQuantizedMM(MLXArray, MLXArray, scales: MLXArray?, groupSize: Int?, bits: Int?, mode: QuantizationMode, globalScaleX: MLXArray?, globalScaleW: MLXArray?, stream: StreamOrDevice) -> MLXArray](./quantizedquantizedmm%28_,_,scales,groupsize,bits,mode,globalscalex,globalscalew,stream%29.md)
  Perform a matrix multiplication using a possibly quantized weight matrix `w` and a non-quantized input `x`. The input `x` is quantized on the fly. The weight matrix `w` is used as-is if it is already quantized; otherwise, it is quantized on the fly.
- [func segmentedMM(MLXArray, MLXArray, segments: MLXArray, stream: StreamOrDevice) -> MLXArray](./segmentedmm%28_,_,segments,stream%29.md)
  Perform a matrix multiplication but segment the inner dimension and save the result for each segment separately.
- [func inner(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./inner%28_,_,stream%29.md)
  Ordinary inner product of vectors for 1-D arrays, in higher dimensions a sum product over the last axes.
- [func outer(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./outer%28_,_,stream%29.md)
  Compute the outer product of two 1-D arrays, if the array’s passed are not 1-D a flatten op will be run beforehand.
- [func tensordot(MLXArray, MLXArray, axes: Int, stream: StreamOrDevice) -> MLXArray](./tensordot%28_,_,axes,stream%29-3qkgq.md)
  Compute tensor dot product.
- [func tensordot(MLXArray, MLXArray, axes: ((Int, Int), (Int, Int)), stream: StreamOrDevice) -> MLXArray](./tensordot%28_,_,axes,stream%29-8yqyi.md)
  Compute tensor dot product.

## See Also

### Arithmetic Operators and Functions
- [Convolution](./convolution.md)
  Convolution operations.
- [Cumulative Operations](./cumulative.md)
  Operations that produce a cumulative result.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/arithmetic)*