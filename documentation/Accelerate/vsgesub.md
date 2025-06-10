# vSgesub(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Subtracts two general matrices or their transposes.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vSgesub(_ height: Int32, _ width: Int32, _ a: UnsafePointer<vFloat>, _ forma: CChar, _ b: UnsafePointer<vFloat>, _ formb: CChar, _ c: UnsafeMutablePointer<vFloat>)
```

#### Discussion

Matrix `b` (or its transpose) is subtracted from matrix `a` (or its transpose); the result is stored in mactrix `c`.

## Parameters

- `height`: Number of rows in the matrices to be subtracted; must be a multiple of 4.
- `width`: Number of columns in the matrices to be subtracted; must be a multiple of 4.
- `a`: A matrix with elements of type  .  If   = ‘N’, the matrix itself is used in the calculation and it has   rows and   columns.  If   = ‘T’, the transpose is used and   has   rows and   columns.
- `forma`: Selector with a value of ‘N’ or ‘T’.
- `b`: A matrix with elements of type  .  If   = ‘N’, the matrix itself is used in the calculation and it has   rows and   columns.  If   = ‘T’, the transpose is used and   has   rows and   columns.
- `formb`: Selector with a value of  ‘N’ or ‘T’.
- `c`: Destination matrix with   rows and   columns.

## See Also

- [func vSgeadd(Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>)](vsgeadd(_:_:_:_:_:_:_:).md)
  Adds two general matrices or their transposes.
- [func vSgemul(Int32, Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>)](vsgemul(_:_:_:_:_:_:_:_:).md)
  Multiplies two general matrices or their transposes.
- [func vSgemm(Int32, Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>, Float, Float, UnsafeMutablePointer<vFloat>)](vsgemm(_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiples two general matrices or their transposes, then scales and adds a third.
- [func vSgetmi(Int32, UnsafeMutablePointer<vFloat>)](vsgetmi(_:_:).md)
  Transposes a matrix in place.
- [func vSgetmo(Int32, Int32, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vsgetmo(_:_:_:_:).md)
  Transposes a matrix out of place.
- [func vSgevv(Int32, Int32, UnsafePointer<vFloat>, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vsgevv(_:_:_:_:_:).md)
  Produces the outer product of two vectors and places the results into a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vsgesub(_:_:_:_:_:_:_:))*