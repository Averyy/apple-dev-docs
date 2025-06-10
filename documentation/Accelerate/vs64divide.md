# vS64Divide(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Signed 64-bit division.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func vS64Divide(_ vN: vSInt32, _ vD: vSInt32, _ vRemainder: UnsafeMutablePointer<vSInt32>?) -> vSInt32
```

## See Also

- [func vU64AddS(vUInt32, vUInt32) -> vUInt32](vu64adds(_:_:).md)
  Unsigned 64-bit addition with saturation (clipping).
- [func vS64AddS(vSInt32, vSInt32) -> vSInt32](vs64adds(_:_:).md)
  Signed 64-bit addition with saturation (clipping).
- [func vU128Add(vUInt32, vUInt32) -> vUInt32](vu128add(_:_:).md)
  Unsigned 128-bit addition (modular arithmetic).
- [func vU128AddS(vUInt32, vUInt32) -> vUInt32](vu128adds(_:_:).md)
  Unsigned 128-bit addition with saturation (clipping).
- [func vS128Add(vSInt32, vSInt32) -> vSInt32](vs128add(_:_:).md)
  Signed 128-bit addition (modular arithmetic).
- [func vS128AddS(vSInt32, vSInt32) -> vSInt32](vs128adds(_:_:).md)
  Signed 128-bit addition with saturation (clipping).
- [func vU64SubS(vUInt32, vUInt32) -> vUInt32](vu64subs(_:_:).md)
  Unsigned 64-bit subtraction with saturation (clipping).
- [func vS64SubS(vSInt32, vSInt32) -> vSInt32](vs64subs(_:_:).md)
  Signed 64-bit subtraction with saturation (clipping).
- [func vU128Sub(vUInt32, vUInt32) -> vUInt32](vu128sub(_:_:).md)
  Unsigned 128-bit subtraction (modular arithmetic).
- [func vU128SubS(vUInt32, vUInt32) -> vUInt32](vu128subs(_:_:).md)
  Unsigned 128-bit subtraction with saturation (clipping).
- [func vS128Sub(vSInt32, vSInt32) -> vSInt32](vs128sub(_:_:).md)
  Signed 128-bit subtraction (modular arithmetic).
- [func vS128SubS(vSInt32, vSInt32) -> vSInt32](vs128subs(_:_:).md)
  Signed 128-bit subtraction with saturation (clipping).
- [func vU8HalfMultiply(vUInt8, vUInt8) -> vUInt8](vu8halfmultiply(_:_:).md)
  Unsigned 8-bit multiplication; results are same width as multiplicands.
- [func vS8HalfMultiply(vSInt8, vSInt8) -> vSInt8](vs8halfmultiply(_:_:).md)
  Signed 8-bit multiplication; results are same width as multiplicands.
- [func vU32HalfMultiply(vUInt32, vUInt32) -> vUInt32](vu32halfmultiply(_:_:).md)
  Unsigned 32-bit multiplication; results are same width as multiplicands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vs64divide(_:_:_:))*