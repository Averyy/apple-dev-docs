# vBasicOps

**Framework**: Accelerate

Perform basic arithmetic and logical functions on 128-bit vectors.

#### Overview

vBasicOps.h declares a set of basic arithmetic and logical functions on 128-bit vectors, using the integer types from vecLibTypes.h.

The function names begin with “v,” followed by a mnemonic for the type of operation, e.g. “S” or “U” for signed or unsigned, then the width of the operation, then the name of the operation. For example, `vS8Divide` performs division of signed 8-bit values packed into 128-bit vectors.

## Topics

### Shift and Rotate Functions (from vBasicOps.h)
- [func vLL128Shift(vUInt32, vUInt8) -> vUInt32](vll128shift(_:_:).md)
  128-bit logical left shift.
- [func vLR128Shift(vUInt32, vUInt8) -> vUInt32](vlr128shift(_:_:).md)
  128-bit logical right shift.
- [func vLL64Shift(vUInt32, vUInt8) -> vUInt32](vll64shift(_:_:).md)
  64-bit logical left shift.
- [func vLL64Shift2(vUInt32, vUInt8) -> vUInt32](vll64shift2(_:_:).md)
  64-bit logical left shift with two shift factors.
- [func vLR64Shift(vUInt32, vUInt8) -> vUInt32](vlr64shift(_:_:).md)
  64-bit logical right shift.
- [func vLR64Shift2(vUInt32, vUInt8) -> vUInt32](vlr64shift2(_:_:).md)
  64-bit logical right shift with two shift factors.
- [func vA64Shift(vUInt32, vUInt8) -> vUInt32](va64shift(_:_:).md)
  64-bit arithmetic (signed) shift.
- [func vA64Shift2(vUInt32, vUInt8) -> vUInt32](va64shift2(_:_:).md)
  64-bit arithmetic (signed) shift with two shift factors.
- [func vA128Shift(vUInt32, vUInt8) -> vUInt32](va128shift(_:_:).md)
  128-bit arithmetic (signed) shift.
- [func vL64Rotate(vUInt32, vUInt8) -> vUInt32](vl64rotate(_:_:).md)
  64-bit left rotate.
- [func vR64Rotate(vUInt32, vUInt8) -> vUInt32](vr64rotate(_:_:).md)
  64-bit right rotate.
- [func vL64Rotate2(vUInt32, vUInt8) -> vUInt32](vl64rotate2(_:_:).md)
  64-bit left rotate with two rotation factors.
- [func vR64Rotate2(vUInt32, vUInt8) -> vUInt32](vr64rotate2(_:_:).md)
  64-bit right rotate with two rotation factors.
- [func vL128Rotate(vUInt32, vUInt8) -> vUInt32](vl128rotate(_:_:).md)
  128-bit left rotate.
- [func vR128Rotate(vUInt32, vUInt8) -> vUInt32](vr128rotate(_:_:).md)
  128-bit right rotate.
### Integer Arithmetic Functions (from vBasicOps.h)
- [vU64Add](vu64add.md)
  Unsigned 64-bit addition (modular arithmetic).
- [func vU64AddS(vUInt32, vUInt32) -> vUInt32](vu64adds(_:_:).md)
  Unsigned 64-bit addition with saturation (clipping).
- [vS64Add](vs64add.md)
  Signed 64-bit addition (modular arithmetic).
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
- [vU64Sub](vu64sub.md)
  Unsigned 64-bit subtraction (modular arithmetic).
- [func vU64SubS(vUInt32, vUInt32) -> vUInt32](vu64subs(_:_:).md)
  Unsigned 64-bit subtraction with saturation (clipping).
- [vS64Sub](vs64sub.md)
  Signed 64-bit subtraction (modular arithmetic).
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
- [vU16HalfMultiply](vu16halfmultiply.md)
  Unsigned 16-bit multiplication; results are same width as multiplicands.
- [vS16HalfMultiply](vs16halfmultiply.md)
  Signed 16-bit multiplication; results are same width as multiplicands.
- [func vU32HalfMultiply(vUInt32, vUInt32) -> vUInt32](vu32halfmultiply(_:_:).md)
  Unsigned 32-bit multiplication; results are same width as multiplicands.
- [func vS32HalfMultiply(vSInt32, vSInt32) -> vSInt32](vs32halfmultiply(_:_:).md)
  Signed 32-bit multiplication; results are same width as multiplicands.
- [func vU64HalfMultiply(vUInt32, vUInt32) -> vUInt32](vu64halfmultiply(_:_:).md)
  Unsigned 64-bit multiplication; results are same width as multiplicands.
- [func vS64HalfMultiply(vSInt32, vSInt32) -> vSInt32](vs64halfmultiply(_:_:).md)
  Signed 64-bit multiplication; results are same width as multiplicands.
- [func vU128HalfMultiply(vUInt32, vUInt32) -> vUInt32](vu128halfmultiply(_:_:).md)
  Unsigned 128-bit multiplication; results are same width as multiplicands.
- [func vS128HalfMultiply(vSInt32, vSInt32) -> vSInt32](vs128halfmultiply(_:_:).md)
  Signed 128-bit multiplication; results are same width as multiplicands.
- [func vU32FullMulEven(vUInt32, vUInt32) -> vUInt32](vu32fullmuleven(_:_:).md)
  Unsigned 32-bit multiplication; results are twice as wide as multiplicands, even-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.
- [func vU32FullMulOdd(vUInt32, vUInt32) -> vUInt32](vu32fullmulodd(_:_:).md)
  Unsigned 32-bit multiplication; results are twice as wide as multiplicands, odd-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.
- [func vS32FullMulEven(vSInt32, vSInt32) -> vSInt32](vs32fullmuleven(_:_:).md)
  Signed 32-bit multiplication; results are twice as wide as multiplicands, even-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.
- [func vS32FullMulOdd(vSInt32, vSInt32) -> vSInt32](vs32fullmulodd(_:_:).md)
  Signed 32-bit multiplication; results are twice as wide as multiplicands, odd-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.
- [func vU64FullMulEven(vUInt32, vUInt32) -> vUInt32](vu64fullmuleven(_:_:).md)
  Unsigned 64-bit multiplication; results are twice as wide as multiplicands, even-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.
- [func vU64FullMulOdd(vUInt32, vUInt32) -> vUInt32](vu64fullmulodd(_:_:).md)
  Unsigned 64-bit multiplication; results are twice as wide as multiplicands, odd-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.
- [func vS64FullMulEven(vSInt32, vSInt32) -> vSInt32](vs64fullmuleven(_:_:).md)
  Signed 64-bit multiplication; results are twice as wide as multiplicands, even-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.
- [func vS64FullMulOdd(vSInt32, vSInt32) -> vSInt32](vs64fullmulodd(_:_:).md)
  Signed 64-bit multiplication; results are twice as wide as multiplicands, odd-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.
- [func vU8Divide(vUInt8, vUInt8, UnsafeMutablePointer<vUInt8>?) -> vUInt8](vu8divide(_:_:_:).md)
  Unsigned 8-bit division.
- [func vS8Divide(vSInt8, vSInt8, UnsafeMutablePointer<vSInt8>?) -> vSInt8](vs8divide(_:_:_:).md)
  Signed 8-bit division.
- [func vU16Divide(vUInt16, vUInt16, UnsafeMutablePointer<vUInt16>?) -> vUInt16](vu16divide(_:_:_:).md)
  Unsigned 16-bit division.
- [func vS16Divide(vSInt16, vSInt16, UnsafeMutablePointer<vSInt16>?) -> vSInt16](vs16divide(_:_:_:).md)
  Signed 16-bit division.
- [func vU32Divide(vUInt32, vUInt32, UnsafeMutablePointer<vUInt32>?) -> vUInt32](vu32divide(_:_:_:).md)
  Unsigned 32-bit division.
- [func vS32Divide(vSInt32, vSInt32, UnsafeMutablePointer<vSInt32>?) -> vSInt32](vs32divide(_:_:_:).md)
  Signed 32-bit division.
- [func vU64Divide(vUInt32, vUInt32, UnsafeMutablePointer<vUInt32>?) -> vUInt32](vu64divide(_:_:_:).md)
  Unsigned 64-bit division.
- [func vS64Divide(vSInt32, vSInt32, UnsafeMutablePointer<vSInt32>?) -> vSInt32](vs64divide(_:_:_:).md)
  Signed 64-bit division.
- [func vU128Divide(vUInt32, vUInt32, UnsafeMutablePointer<vUInt32>?) -> vUInt32](vu128divide(_:_:_:).md)
  Unsigned 128-bit division.
- [func vS128Divide(vSInt32, vSInt32, UnsafeMutablePointer<vSInt32>?) -> vSInt32](vs128divide(_:_:_:).md)
  Signed 128-bit division.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vbasicops)*