# vSgemv(_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Multiplies a vector by a scalar. Multiplies a matrix by another scalar, then by a second vector, and adds the resulting vector to the first vector. This function can also perform the calculation with the transpose of the original matrix instead of the matrix itself. A selector parameter determines whether the transpose is used.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vSgemv(_ forma: CChar, _ m: Int32, _ n: Int32, _ alpha: Float, _ a: UnsafePointer<vFloat>, _ x: UnsafePointer<vFloat>, _ beta: Float, _ y: UnsafeMutablePointer<vFloat>)
```

#### Discussion

Vector `y` is multiplied by `beta`. Matrix `a` is multiplied by `alpha`. Then if `forma` = ‘N’, `a` is multiplied by vector `x`; if `forma` = ‘T’, the transpose of `a` is multiplied by `x`. The resulting vector is added to vector `y`, and the results are stored in `y`.

## Parameters

- `forma`: Selects the variant computation to be performed: ‘T’ causes the transpose  of matrix   to be used, ‘N’ causes   itself to be used.
- `m`: Number of rows in  . If   = ‘N’,   is the length of vector  ; if   = ‘T’,   is the length of vector  ; must be a multiple of 4.
- `n`: Number of columns in  . If   = ‘N’,   is the length of vector  ; if   = ‘T’,   is the length of vector  ; must be a multiple of 4.
- `alpha`: Scalar multiplier for matrix  .
- `a`:   by   matrix with elements of type  .
- `x`: Vector with elements of type  .
- `beta`: Scalar multiplier for vector  .
- `y`: Destination vector with   elements of type  .

## See Also

- [func vSgemx(Int32, Int32, Float, UnsafePointer<vFloat>, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vsgemx(_:_:_:_:_:_:).md)
  Multiplies a matrix by a scalar and then by a vector, and adds the resulting vector to a second vector.
- [func vSgemtx(Int32, Int32, Float, UnsafePointer<vFloat>, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vsgemtx(_:_:_:_:_:_:).md)
  Forms the transpose of a matrix, multiplies it by a scalar and then by a vector, and adds the resulting vector to a second vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vsgemv(_:_:_:_:_:_:_:_:))*