# vS256Divide(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Computes the signed 256-bit division.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vS256Divide(_ numerator: UnsafePointer<vS256>, _ divisor: UnsafePointer<vS256>, _ result: UnsafeMutablePointer<vS256>, _ remainder: UnsafeMutablePointer<vS256>?)
```

#### Discussion

> ❗ **Important**:  Apple provides the BLAS and LAPACK libraries under the Accelerate framework to be in line with LAPACK 3.9.1. These new interfaces provide additional functionality, as well as a new ILP64 interface. To use the new interfaces, define `ACCELERATE_NEW_LAPACK` before including the Accelerate or vecLib headers. For ILP64 interfaces, also define `ACCELERATE_LAPACK_ILP64`. For Swift projects, specify `ACCELERATE_NEW_LAPACK=1` and `ACCELERATE_LAPACK_ILP64=1` as preprocessor macros in Xcode build settings.

## See Also

- [func vU256Add(UnsafePointer<vU256>, UnsafePointer<vU256>, UnsafeMutablePointer<vU256>)](vu256add(_:_:_:).md)
  Unsigned 256-bit addition (modular arithmetic).
- [func vU256AddS(UnsafePointer<vU256>, UnsafePointer<vU256>, UnsafeMutablePointer<vU256>)](vu256adds(_:_:_:).md)
  Unsigned 256-bit addition with saturation (clipping).
- [func vS256Add(UnsafePointer<vS256>, UnsafePointer<vS256>, UnsafeMutablePointer<vS256>)](vs256add(_:_:_:).md)
  Signed 256-bit addition (modular arithmetic).
- [func vS256AddS(UnsafePointer<vS256>, UnsafePointer<vS256>, UnsafeMutablePointer<vS256>)](vs256adds(_:_:_:).md)
  Signed 256-bit addition with saturation (clipping).
- [func vU512Add(UnsafePointer<vU512>, UnsafePointer<vU512>, UnsafeMutablePointer<vU512>)](vu512add(_:_:_:).md)
  Unsigned 512-bit addition (modular arithmetic).
- [func vU512AddS(UnsafePointer<vU512>, UnsafePointer<vU512>, UnsafeMutablePointer<vU512>)](vu512adds(_:_:_:).md)
  Unsigned 512-bit addition with saturation (clipping).
- [func vS512Add(UnsafePointer<vS512>, UnsafePointer<vS512>, UnsafeMutablePointer<vS512>)](vs512add(_:_:_:).md)
  Signed 512-bit addition (modular arithmetic).
- [func vS512AddS(UnsafePointer<vS512>, UnsafePointer<vS512>, UnsafeMutablePointer<vS512>)](vs512adds(_:_:_:).md)
  Signed 512-bit addition with saturation (clipping).
- [func vU1024Add(UnsafePointer<vU1024>, UnsafePointer<vU1024>, UnsafeMutablePointer<vU1024>)](vu1024add(_:_:_:).md)
  Unsigned 1024-bit addition (modular arithmetic).
- [func vU1024AddS(UnsafePointer<vU1024>, UnsafePointer<vU1024>, UnsafeMutablePointer<vU1024>)](vu1024adds(_:_:_:).md)
  Unsigned 1024-bit addition with saturation (clipping).
- [func vS1024Add(UnsafePointer<vS1024>, UnsafePointer<vS1024>, UnsafeMutablePointer<vS1024>)](vs1024add(_:_:_:).md)
  Signed 1024-bit addition (modular arithmetic).
- [func vS1024AddS(UnsafePointer<vS1024>, UnsafePointer<vS1024>, UnsafeMutablePointer<vS1024>)](vs1024adds(_:_:_:).md)
  Signed 1024-bit addition with saturation (clipping).
- [func vU256Sub(UnsafePointer<vU256>, UnsafePointer<vU256>, UnsafeMutablePointer<vU256>)](vu256sub(_:_:_:).md)
  Unsigned 256-bit subtraction (modular arithmetic).
- [func vU256SubS(UnsafePointer<vU256>, UnsafePointer<vU256>, UnsafeMutablePointer<vU256>)](vu256subs(_:_:_:).md)
  Unsigned 256-bit subtraction with saturation (clipping).
- [func vS256Sub(UnsafePointer<vS256>, UnsafePointer<vS256>, UnsafeMutablePointer<vS256>)](vs256sub(_:_:_:).md)
  Signed 256-bit subtraction (modular arithmetic).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vs256divide(_:_:_:_:))*