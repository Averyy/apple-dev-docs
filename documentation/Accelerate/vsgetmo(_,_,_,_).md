# vSgetmo(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Transposes a matrix out of place.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use appleblas_sgeadd instead

## Declaration

```swift
func vSgetmo(_ height: Int32, _ width: Int32, _ x: UnsafePointer<vFloat>, _ y: UnsafeMutablePointer<vFloat>)
```

```c
extern void vSgetmo(int32_t height, int32_t width, const vFloat *x, vFloat *y);
```

#### Discussion

The matrix `x` is transposed into matrix `y`.

## Parameters

- `height`: Number of rows in matrix `x` and number of columns in matrix y; must be a multiple of 4.
- `width`: Number of columns in matrix `x` and number of rows in matrix y; must be a multiple of 4.
- `x`: Matrix with `height` rows and `width` columns.
- `y`: Matrix with `width` rows and `height` columns.

## See Also

### Matrix Operations (from vectorOps.h)
- [func vSgeadd(Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>)](./vsgeadd%28_,_,_,_,_,_,_%29.md)
  Adds two general matrices or their transposes.
- [func vSgesub(Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>)](./vsgesub%28_,_,_,_,_,_,_%29.md)
  Subtracts two general matrices or their transposes.
- [func vSgemul(Int32, Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>)](./vsgemul%28_,_,_,_,_,_,_,_%29.md)
  Multiplies two general matrices or their transposes.
- [func vSgemm(Int32, Int32, Int32, UnsafePointer<vFloat>, CChar, UnsafePointer<vFloat>, CChar, UnsafeMutablePointer<vFloat>, Float, Float, UnsafeMutablePointer<vFloat>)](./vsgemm%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Multiples two general matrices or their transposes, then scales and adds a third.
- [func vSgetmi(Int32, UnsafeMutablePointer<vFloat>)](./vsgetmi%28_,_%29.md)
  Transposes a matrix in place.
- [func vSgevv(Int32, Int32, UnsafePointer<vFloat>, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](./vsgevv%28_,_,_,_,_%29.md)
  Produces the outer product of two vectors and places the results into a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vsgetmo(_:_:_:_:))*