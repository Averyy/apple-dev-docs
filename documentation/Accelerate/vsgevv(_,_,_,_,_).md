# vSgevv(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Produces the outer product of two vectors and places the results into a matrix.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use cblas_sger on a zero matrix instead

## Declaration

```swift
func vSgevv(_ l: Int32, _ n: Int32, _ A: UnsafePointer<vFloat>, _ B: UnsafePointer<vFloat>, _ M: UnsafeMutablePointer<vFloat>)
```

```c
extern void vSgevv(int32_t l, int32_t n, const vFloat *A, const vFloat *B, vFloat *M);
```

#### Discussion

The vectors `A` and `B` are multiplied and the result is stored in matrix `M`, that is, for `0 <= i < l` and `0 <= j < n`, `C[i*n + j] = A[i] * B[j]`..

## Parameters

- `l`: Number of elements in vector `A` and the number of rows in matrix `M`; must be a multiple of 4.
- `n`: Number of elements in vector `B` and the number of columns in matrix `M`; must be a multiple of 4.
- `A`: Vector with `l` elements.
- `B`: Vector with `n` elements.
- `M`: Matrix with `l` rows and `n` columns.

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
- [func vSgetmo(Int32, Int32, UnsafePointer<vFloat>, UnsafeMutablePointer<vFloat>)](./vsgetmo%28_,_,_,_%29.md)
  Transposes a matrix out of place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vsgevv(_:_:_:_:_:))*