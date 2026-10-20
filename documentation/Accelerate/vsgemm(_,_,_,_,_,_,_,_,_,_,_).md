# vSgemm(_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Multiples two general matrices or their transposes, then scales and adds a third.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vSgemm(_ l: Int32, _ m: Int32, _ n: Int32, _ a: UnsafePointer<vFloat>, _ forma: CChar, _ b: UnsafePointer<vFloat>, _ formb: CChar, _ c: UnsafeMutablePointer<vFloat>, _ alpha: Float, _ beta: Float, _ matrix: UnsafeMutablePointer<vFloat>)
```

#### Discussion

Matrix `a` (or its transpose) is multiplied by matrix `b` (or its transpose); matrix `c` is multiplied by `beta`, and the result is added to the result of the matrix multiplication; the result is stored in matrix `matrix`

## Parameters

- `l`: Number of rows in matrix `c`; must be a multiple of 4.
- `m`: If `forma` = ‘N’, `m` is the number of columns in matrix `a` ; if `forma` = ‘T’, `m` is the number of rows in matrix `a`. Also, if `formb` = ‘N’, `m` is the number of rows in matrix `b`; if `formb` = ‘T’, `m` is the number of columns in matrix `b`. `m` must be a multiple of 4.
- `n`: Number of columns in matrix `c`; must be a multiple of 4.
- `a`: A matrix with elements of type `float`.  If `forma` = ‘N’, the matrix itself is used in the calculation and it has `l` rows and `m` columns.  If `forma` = ‘T’, the transpose is used and `a` has `m` rows and `l` columns. Thus the matrix used in the calculation is `l` by `n`.
- `forma`: Selector with a value of ‘N’ or ‘T’.
- `b`: A matrix with elements of type `float`.  If `formb` = ‘N’, the matrix itself is used in the calculation and it has `m` rows and `n` columns.  If `formb` = ‘T’, the transpose is used and `b` has `n` rows and `m` columns. Thus the matrix used in the calculation is `m` by `n`.
- `formb`: Selector with a value of ‘N’ or ‘T’.
- `c`: An `l` by `n` matrix with elements of type `float`.
- `alpha`: Multiplier for matrix `a`.
- `beta`: Multiplier for matrix `c`.
- `matrix`: Destination matrix with `l` rows and `n` columns.

## See Also

- [func vSgeadd(Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>)](vsgeadd(_:_:_:_:_:_:_:).md)
  Adds two general matrices or their transposes.
- [func vSgesub(Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>)](vsgesub(_:_:_:_:_:_:_:).md)
  Subtracts two general matrices or their transposes.
- [func vSgemul(Int32, Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>)](vsgemul(_:_:_:_:_:_:_:_:).md)
  Multiplies two general matrices or their transposes.
- [func vSgetmi(Int32, UnsafeMutablePointer<vFloat>)](vsgetmi(_:_:).md)
  Transposes a matrix in place.
- [func vSgetmo(Int32, Int32, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vsgetmo(_:_:_:_:).md)
  Transposes a matrix out of place.
- [func vSgevv(Int32, Int32, UnsafePointer<vFloat>, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vsgevv(_:_:_:_:_:).md)
  Produces the outer product of two vectors and places the results into a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vsgemm(_:_:_:_:_:_:_:_:_:_:_:))*