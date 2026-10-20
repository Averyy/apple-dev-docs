# vSgetmi(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Transposes a matrix in place.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use appleblas_sgeadd instead

## Declaration

```swift
func vSgetmi(_ size: Int32, _ x: UnsafeMutablePointer<vFloat>)
```

```c
extern void vSgetmi(int32_t size, vFloat *x);
```

#### Discussion

The matrix `x` is transposed in place.

## Parameters

- `size`: Number of rows and columns in matrix `x`; must be a multiple of 4.
- `x`: Square matrix with `size` rows and `size` columns.

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
- [func vSgetmo(Int32, Int32, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](./vsgetmo%28_,_,_,_%29.md)
  Transposes a matrix out of place.
- [func vSgevv(Int32, Int32, UnsafePointer<vFloat>, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](./vsgevv%28_,_,_,_,_%29.md)
  Produces the outer product of two vectors and places the results into a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vsgetmi(_:_:))*