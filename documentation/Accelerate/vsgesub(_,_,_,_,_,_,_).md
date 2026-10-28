# vSgesub(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Subtracts two general matrices or their transposes.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use appleblas_sgeadd instead

## Declaration

```swift
func vSgesub(_ height: Int32, _ width: Int32, _ a: UnsafePointer<vFloat>, _ forma: CChar, _ b: UnsafePointer<vFloat>, _ formb: CChar, _ c: UnsafeMutablePointer<vFloat>)
```

```c
extern void vSgesub(int32_t height, int32_t width, const vFloat *a, char forma, const vFloat *b, char formb, vFloat *c);
```

## Discussion

Matrix `b` (or its transpose) is subtracted from matrix `a` (or its transpose); the result is stored in mactrix `c`.

## Parameters

- `height`: Number of rows in the matrices to be subtracted; must be a multiple of 4.
- `width`: Number of columns in the matrices to be subtracted; must be a multiple of 4.
- `a`: A matrix with elements of type `float`.  If `forma` = ‘N’, the matrix itself is used in the calculation and it has `height` rows and `width` columns.  If `forma` = ‘T’, the transpose is used and `a` has `width` rows and `height` columns.
- `forma`: Selector with a value of ‘N’ or ‘T’.
- `b`: A matrix with elements of type `float`.  If `formb` = ‘N’, the matrix itself is used in the calculation and it has `height` rows and `width` columns.  If `formb` = ‘T’, the transpose is used and `b` has `width` rows and `height` columns.
- `formb`: Selector with a value of  ‘N’ or ‘T’.
- `c`: Destination matrix with `height` rows and `width` columns.

## See Also

### Matrix Operations (from vectorOps.h)
- [func vSgeadd(Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>)](./vsgeadd%28_,_,_,_,_,_,_%29.md)
  Adds two general matrices or their transposes.
- [func vSgemul(Int32, Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>)](./vsgemul%28_,_,_,_,_,_,_,_%29.md)
  Multiplies two general matrices or their transposes.
- [func vSgemm(Int32, Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>, Float, Float, UnsafeMutablePointer<vFloat>)](./vsgemm%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Multiples two general matrices or their transposes, then scales and adds a third.
- [func vSgetmi(Int32, UnsafeMutablePointer<vFloat>)](./vsgetmi%28_,_%29.md)
  Transposes a matrix in place.
- [func vSgetmo(Int32, Int32, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](./vsgetmo%28_,_,_,_%29.md)
  Transposes a matrix out of place.
- [func vSgevv(Int32, Int32, UnsafePointer<vFloat>, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](./vsgevv%28_,_,_,_,_%29.md)
  Produces the outer product of two vectors and places the results into a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vsgesub(_:_:_:_:_:_:_:))*