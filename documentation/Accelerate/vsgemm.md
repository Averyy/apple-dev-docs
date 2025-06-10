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

- `l`: Number of rows in matrix  ; must be a multiple of 4.
- `m`: If   = ‘N’,   is the number of columns in matrix   ; if   = ‘T’,   is the number of rows in matrix  . Also, if   = ‘N’,   is the number of rows in matrix  ; if   = ‘T’,   is the number of columns in matrix  .   must be a multiple of 4.
- `n`: Number of columns in matrix  ; must be a multiple of 4.
- `a`: A matrix with elements of type  .  If   = ‘N’, the matrix itself is used in the calculation and it has   rows and   columns.  If   = ‘T’, the transpose is used and   has   rows and   columns. Thus the matrix used in the calculation is   by  .
- `forma`: Selector with a value of ‘N’ or ‘T’.
- `b`: A matrix with elements of type  .  If   = ‘N’, the matrix itself is used in the calculation and it has   rows and   columns.  If   = ‘T’, the transpose is used and   has   rows and   columns. Thus the matrix used in the calculation is   by  .
- `formb`: Selector with a value of ‘N’ or ‘T’.
- `c`: An   by   matrix with elements of type  .
- `alpha`: Multiplier for matrix  .
- `beta`: Multiplier for matrix  .
- `matrix`: Destination matrix with   rows and   columns.

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