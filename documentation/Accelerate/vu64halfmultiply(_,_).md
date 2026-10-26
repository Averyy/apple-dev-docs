# vU64HalfMultiply(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Unsigned 64-bit multiplication; results are same width as multiplicands.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vU64HalfMultiply(_ vA: vUInt32, _ vB: vUInt32) -> vUInt32
```

```c
extern vUInt32 vU64HalfMultiply(vUInt32 vA, vUInt32 vB);
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
- [vU64Add](./vu64add.md)
  Unsigned 64-bit addition (modular arithmetic).
- [vS64Add](./vs64add.md)
  Signed 64-bit addition (modular arithmetic).
- [vU64Sub](./vu64sub.md)
  Unsigned 64-bit subtraction (modular arithmetic).
- [vS64Sub](./vs64sub.md)
  Signed 64-bit subtraction (modular arithmetic).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vu64halfmultiply(_:_:))*