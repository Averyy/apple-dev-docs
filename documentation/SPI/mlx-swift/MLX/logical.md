---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/logical"
framework: "mlx-swift/MLX"
---

# Logical Operators

**Framework**: mlx-swift/MLX  
**Role**: API Collection

Evaluating logical operations on MLXArray.

#### Overview

[`MLXArray`](./mlxarray.md) has a number of logical operators, instance methods and free functions.  Single or multiple arrayscan be combined using these operators:

```swift
let r = a > b || !(b < c)
```

These can be used for control flow, though consider [Lazy Evaluation](./lazy-evaluation.md) when doing this:

```swift
if (a < b).all().item() {
    ...
}
```

## Topics

### MLXArray Operators
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
### MLXArray Logical Functions
- [func all(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/all%28axes,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func any(axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/any%28axes,keepdims,stream%29.md)
  An `or` reduction over the given axes.
- [func allClose(some ScalarOrArray, rtol: Double, atol: Double, equalNaN: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/allclose%28_,rtol,atol,equalnan,stream%29.md)
  Approximate comparison of two arrays.
- [func arrayEqual(some ScalarOrArray, equalNAN: Bool, stream: StreamOrDevice) -> MLXArray](./mlxarray/arrayequal%28_,equalnan,stream%29.md)
  Array equality check.
### Logical Free Functions
- [func all(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28_,axes,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func allClose(MLXArray, some ScalarOrArray, rtol: Double, atol: Double, equalNaN: Bool, stream: StreamOrDevice) -> MLXArray](./allclose%28_,_,rtol,atol,equalnan,stream%29.md)
  Approximate comparison of two arrays.
- [func any(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./any%28_,axes,keepdims,stream%29.md)
  An `or` reduction over the given axes.
- [func arrayEqual(MLXArray, some ScalarOrArray, equalNAN: Bool, stream: StreamOrDevice) -> MLXArray](./arrayequal%28_,_,equalnan,stream%29.md)
  Array equality check.
- [func equal(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./equal%28_,_,stream%29.md)
  Element-wise equality.
- [func greater(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./greater%28_,_,stream%29.md)
  Element-wise greater than.
- [func greaterEqual(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./greaterequal%28_,_,stream%29.md)
  Element-wise less greater than or equal.
- [func isClose(MLXArray, MLXArray, rtol: Double, atol: Double, equalNaN: Bool, stream: StreamOrDevice) -> MLXArray](./isclose%28_,_,rtol,atol,equalnan,stream%29.md)
  Returns a boolean array where two arrays are element-wise equal within a tolerance.
- [func less(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./less%28_,_,stream%29.md)
  Element-wise less than.
- [func lessEqual(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./lessequal%28_,_,stream%29.md)
  Element-wise less than or equal.
- [func logicalAnd(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./logicaland%28_,_,stream%29.md)
  Element-wise logical and.
- [func logicalNot(MLXArray, stream: StreamOrDevice) -> MLXArray](./logicalnot%28_,stream%29.md)
  Element-wise logical not.
- [func logicalOr(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./logicalor%28_,_,stream%29.md)
  Element-wise logical or.
- [func logicalXor(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./logicalxor%28_,_,stream%29.md)
  Element-wise logical exclusive or.
- [func notEqual(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./notequal%28_,_,stream%29.md)
  Element-wise not equal.
- [func `where`(MLXArray, some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./where%28_,_,_,stream%29.md)
  Select from `x` or `y` according to `condition`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/logical)*