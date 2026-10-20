# vU32FullMulEven(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Unsigned 32-bit multiplication; results are twice as wide as multiplicands, even-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vU32FullMulEven(_ vA: vUInt32, _ vB: vUInt32) -> vUInt32
```

```c
extern vUInt32 vU32FullMulEven(vUInt32 vA, vUInt32 vB);
```

## See Also

### Integer Arithmetic Functions (from vBasicOps.h)
- [func vU64AddS(vUInt32, vUInt32) -> vUInt32](./vu64adds%28_,_%29.md)
  Unsigned 64-bit addition with saturation (clipping).
- [func vS64AddS(vSInt32, vSInt32) -> vSInt32](./vs64adds%28_,_%29.md)
  Signed 64-bit addition with saturation (clipping).
- [func vU128Add(vUInt32, vUInt32) -> vUInt32](./vu128add%28_,_%29.md)
  Unsigned 128-bit addition (modular arithmetic).
- [func vU128AddS(vUInt32, vUInt32) -> vUInt32](./vu128adds%28_,_%29.md)
  Unsigned 128-bit addition with saturation (clipping).
- [func vS128Add(vSInt32, vSInt32) -> vSInt32](./vs128add%28_,_%29.md)
  Signed 128-bit addition (modular arithmetic).
- [func vS128AddS(vSInt32, vSInt32) -> vSInt32](./vs128adds%28_,_%29.md)
  Signed 128-bit addition with saturation (clipping).
- [func vU64SubS(vUInt32, vUInt32) -> vUInt32](./vu64subs%28_,_%29.md)
  Unsigned 64-bit subtraction with saturation (clipping).
- [func vS64SubS(vSInt32, vSInt32) -> vSInt32](./vs64subs%28_,_%29.md)
  Signed 64-bit subtraction with saturation (clipping).
- [func vU128Sub(vUInt32, vUInt32) -> vUInt32](./vu128sub%28_,_%29.md)
  Unsigned 128-bit subtraction (modular arithmetic).
- [func vU128SubS(vUInt32, vUInt32) -> vUInt32](./vu128subs%28_,_%29.md)
  Unsigned 128-bit subtraction with saturation (clipping).
- [func vS128Sub(vSInt32, vSInt32) -> vSInt32](./vs128sub%28_,_%29.md)
  Signed 128-bit subtraction (modular arithmetic).
- [func vS128SubS(vSInt32, vSInt32) -> vSInt32](./vs128subs%28_,_%29.md)
  Signed 128-bit subtraction with saturation (clipping).
- [func vU8HalfMultiply(vUInt8, vUInt8) -> vUInt8](./vu8halfmultiply%28_,_%29.md)
  Unsigned 8-bit multiplication; results are same width as multiplicands.
- [func vS8HalfMultiply(vSInt8, vSInt8) -> vSInt8](./vs8halfmultiply%28_,_%29.md)
  Signed 8-bit multiplication; results are same width as multiplicands.
- [func vU32HalfMultiply(vUInt32, vUInt32) -> vUInt32](./vu32halfmultiply%28_,_%29.md)
  Unsigned 32-bit multiplication; results are same width as multiplicands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vu32fullmuleven(_:_:))*