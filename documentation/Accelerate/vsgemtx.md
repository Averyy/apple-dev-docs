# vSgemtx(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Forms the transpose of a matrix, multiplies it by a scalar and then by a vector, and adds the resulting vector to a second vector.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vSgemtx(_ m: Int32, _ n: Int32, _ alpha: Float, _ a: UnsafePointer<vFloat>, _ x: UnsafePointer<vFloat>, _ y: UnsafeMutablePointer<vFloat>)
```

#### Discussion

The transpose of matrix `a` is multiplied by `alpha` and then by vector `x`; the resulting vector is added to vector `y`, and the results are stored in `y`.

## Parameters

- `m`: Number of rows in  , and the length of vector  ; must be a multiple of 4.
- `n`: Number of columns in  , and the length of vector  ; must be a multiple of 4.
- `alpha`: Scalar multiplier for matrix  .
- `a`:   by   matrix with elements of type  .
- `x`: Vector with elements of type  .
- `y`: Destination vector with   elements of type  .

## See Also

- [func vSgemv(CChar, Int32, Int32, Float, UnsafePointer<vFloat>, UnsafePointer<vFloat>, Float, UnsafeMutablePointer<vFloat>)](vsgemv(_:_:_:_:_:_:_:_:).md)
  Multiplies a vector by a scalar. Multiplies a matrix by another scalar, then by a second vector, and adds the resulting vector to the first vector. This function can also perform the calculation with the transpose of the original matrix instead of the matrix itself. A selector parameter determines whether the transpose is used.
- [func vSgemx(Int32, Int32, Float, UnsafePointer<vFloat>, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vsgemx(_:_:_:_:_:_:).md)
  Multiplies a matrix by a scalar and then by a vector, and adds the resulting vector to a second vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vsgemtx(_:_:_:_:_:_:))*