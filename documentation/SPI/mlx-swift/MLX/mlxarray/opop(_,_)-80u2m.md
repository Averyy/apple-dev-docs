---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/__(_:_:)-80u2m"
framework: "mlx-swift/MLX"
---

# <<(_:_:)

**Framework**: mlx-swift/MLX  
**Kind**: op  
**Role**: Operator

Element-wise left shift.

## Declaration

```swift
static func << (lhs: MLXArray, rhs: some ScalarOrArray) -> MLXArray
```

## Discussion

Shift the bits of the first input to the left by the second using numpy-style broadcasting semantics. Either or both input arrays can also be scalars.

### See Also

- [Arithmetic](../arithmetic.md)
- [`leftShift(_:_:stream:)`](../leftshift%28_,_,stream%29.md)

## See Also

### MLXArray Operators
- [static func + (MLXArray, MLXArray) -> MLXArray](./plus%28_,_%29-1rv98.md)
  Element-wise addition.
- [static func + (MLXArray, some ScalarOrArray) -> MLXArray](./plus%28_,_%29-2vili.md)
  Element-wise addition with a [`ScalarOrArray`](../scalarorarray.md) (scalar) argument.
- [static func + (some ScalarOrArray, MLXArray) -> MLXArray](./plus%28_,_%29-1jn5i.md)
  Element-wise addition with a [`ScalarOrArray`](../scalarorarray.md) (scalar) argument.
- [class MLXArray](../mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [static func * (MLXArray, MLXArray) -> MLXArray](./star%28_,_%29-1z2ck.md)
  Element-wise multiplication.
- [static func * (MLXArray, some ScalarOrArray) -> MLXArray](./star%28_,_%29-sw3w.md)
  Element-wise multiplication with a [`ScalarOrArray`](../scalarorarray.md) (scalar) argument.
- [static func * (some ScalarOrArray, MLXArray) -> MLXArray](./star%28_,_%29-7441r.md)
  Element-wise multiplication with a [`ScalarOrArray`](../scalarorarray.md) (scalar) argument.
- [static func ** (MLXArray, MLXArray) -> MLXArray](./starstar%28_,_%29-8xxt3.md)
  Element-wise power operation.
- [static func ** (MLXArray, some ScalarOrArray) -> MLXArray](./starstar%28_,_%29-6ve5u.md)
  Element-wise power with a [`ScalarOrArray`](../scalarorarray.md) (scalar) argument.
- [static func ** (some ScalarOrArray, MLXArray) -> MLXArray](./starstar%28_,_%29-4lp4b.md)
  Element-wise power with a [`ScalarOrArray`](../scalarorarray.md) (scalar) argument.
- [static func % (MLXArray, MLXArray) -> MLXArray](./op%28_,_%29-3ubwd.md)
  Element-wise remainder of division.
- [static func % (some ScalarOrArray, MLXArray) -> MLXArray](./op%28_,_%29-8az7l.md)
  Element-wise remainder with a [`ScalarOrArray`](../scalarorarray.md) (scalar) argument.
- [static func % (MLXArray, some ScalarOrArray) -> MLXArray](./op%28_,_%29-516wd.md)
  Element-wise remainder with a [`ScalarOrArray`](../scalarorarray.md) (scalar) argument.
- [static func .! (MLXArray) -> MLXArray](./dotnot%28_%29.md)
  Unary element-wise logical not.
- [static func .== (MLXArray, MLXArray) -> MLXArray](./doteqeq%28_,_%29-56m0a.md)
  Element-wise equality.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/__(_:_:)-80u2m)*