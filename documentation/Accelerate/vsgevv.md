# vSgevv(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Produces the outer product of two vectors and places the results into a matrix.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vSgevv(_ l: Int32, _ n: Int32, _ A: UnsafePointer<vFloat>, _ B: UnsafePointer<vFloat>, _ M: UnsafeMutablePointer<vFloat>)
```

#### Discussion

The vectors `A` and `B` are multiplied and the result is stored in matrix `M`, that is, for `0 <= i < l` and `0 <= j < n`, `C[i*n + j] = A[i] * B[j]`..

## Parameters

- `l`: Number of elements in vector   and the number of rows in matrix  ; must be a multiple of 4.
- `n`: Number of elements in vector   and the number of columns in matrix  ; must be a multiple of 4.
- `A`: Vector with   elements.
- `B`: Vector with   elements.
- `M`: Matrix with   rows and   columns.

## See Also

- [func vSgeadd(Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>)](vsgeadd(_:_:_:_:_:_:_:).md)
  Adds two general matrices or their transposes.
- [func vSgesub(Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>)](vsgesub(_:_:_:_:_:_:_:).md)
  Subtracts two general matrices or their transposes.
- [func vSgemul(Int32, Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>)](vsgemul(_:_:_:_:_:_:_:_:).md)
  Multiplies two general matrices or their transposes.
- [func vSgemm(Int32, Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>, Float, Float, UnsafeMutablePointer<vFloat>)](vsgemm(_:_:_:_:_:_:_:_:_:_:_:).md)
  Multiples two general matrices or their transposes, then scales and adds a third.
- [func vSgetmi(Int32, UnsafeMutablePointer<vFloat>)](vsgetmi(_:_:).md)
  Transposes a matrix in place.
- [func vSgetmo(Int32, Int32, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](vsgetmo(_:_:_:_:).md)
  Transposes a matrix out of place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vsgevv(_:_:_:_:_:))*