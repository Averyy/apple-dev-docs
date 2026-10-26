# vBasicOps

**Framework**: Accelerate  
**Role**: API Collection

Perform basic arithmetic and logical functions on 128-bit vectors.

#### Overview

vBasicOps.h declares a set of basic arithmetic and logical functions on 128-bit vectors, using the integer types from vecLibTypes.h.

The function names begin with “v,” followed by a mnemonic for the type of operation, e.g. “S” or “U” for signed or unsigned, then the width of the operation, then the name of the operation. For example, `vS8Divide` performs division of signed 8-bit values packed into 128-bit vectors.

## Topics

### Shift and Rotate Functions (from vBasicOps.h)
- [func vLL128Shift(vUInt32, vUInt8) -> vUInt32](./vll128shift%28_,_%29.md)
  128-bit logical left shift.
- [func vLR128Shift(vUInt32, vUInt8) -> vUInt32](./vlr128shift%28_,_%29.md)
  128-bit logical right shift.
- [func vLL64Shift(vUInt32, vUInt8) -> vUInt32](./vll64shift%28_,_%29.md)
  64-bit logical left shift.
- [func vLL64Shift2(vUInt32, vUInt8) -> vUInt32](./vll64shift2%28_,_%29.md)
  64-bit logical left shift with two shift factors.
- [func vLR64Shift(vUInt32, vUInt8) -> vUInt32](./vlr64shift%28_,_%29.md)
  64-bit logical right shift.
- [func vLR64Shift2(vUInt32, vUInt8) -> vUInt32](./vlr64shift2%28_,_%29.md)
  64-bit logical right shift with two shift factors.
- [func vA64Shift(vUInt32, vUInt8) -> vUInt32](./va64shift%28_,_%29.md)
  64-bit arithmetic (signed) shift.
- [func vA64Shift2(vUInt32, vUInt8) -> vUInt32](./va64shift2%28_,_%29.md)
  64-bit arithmetic (signed) shift with two shift factors.
- [func vA128Shift(vUInt32, vUInt8) -> vUInt32](./va128shift%28_,_%29.md)
  128-bit arithmetic (signed) shift.
- [func vL64Rotate(vUInt32, vUInt8) -> vUInt32](./vl64rotate%28_,_%29.md)
  64-bit left rotate.
- [func vR64Rotate(vUInt32, vUInt8) -> vUInt32](./vr64rotate%28_,_%29.md)
  64-bit right rotate.
- [func vL64Rotate2(vUInt32, vUInt8) -> vUInt32](./vl64rotate2%28_,_%29.md)
  64-bit left rotate with two rotation factors.
- [func vR64Rotate2(vUInt32, vUInt8) -> vUInt32](./vr64rotate2%28_,_%29.md)
  64-bit right rotate with two rotation factors.
- [func vL128Rotate(vUInt32, vUInt8) -> vUInt32](./vl128rotate%28_,_%29.md)
  128-bit left rotate.
- [func vR128Rotate(vUInt32, vUInt8) -> vUInt32](./vr128rotate%28_,_%29.md)
  128-bit right rotate.
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
- [func vS32HalfMultiply(vSInt32, vSInt32) -> vSInt32](./vs32halfmultiply%28_,_%29.md)
  Signed 32-bit multiplication; results are same width as multiplicands.
- [func vU64HalfMultiply(vUInt32, vUInt32) -> vUInt32](./vu64halfmultiply%28_,_%29.md)
  Unsigned 64-bit multiplication; results are same width as multiplicands.
- [func vS64HalfMultiply(vSInt32, vSInt32) -> vSInt32](./vs64halfmultiply%28_,_%29.md)
  Signed 64-bit multiplication; results are same width as multiplicands.
- [func vU128HalfMultiply(vUInt32, vUInt32) -> vUInt32](./vu128halfmultiply%28_,_%29.md)
  Unsigned 128-bit multiplication; results are same width as multiplicands.
- [func vS128HalfMultiply(vSInt32, vSInt32) -> vSInt32](./vs128halfmultiply%28_,_%29.md)
  Signed 128-bit multiplication; results are same width as multiplicands.
- [func vU32FullMulEven(vUInt32, vUInt32) -> vUInt32](./vu32fullmuleven%28_,_%29.md)
  Unsigned 32-bit multiplication; results are twice as wide as multiplicands, even-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.
- [func vU32FullMulOdd(vUInt32, vUInt32) -> vUInt32](./vu32fullmulodd%28_,_%29.md)
  Unsigned 32-bit multiplication; results are twice as wide as multiplicands, odd-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.
- [func vS32FullMulEven(vSInt32, vSInt32) -> vSInt32](./vs32fullmuleven%28_,_%29.md)
  Signed 32-bit multiplication; results are twice as wide as multiplicands, even-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.
- [func vS32FullMulOdd(vSInt32, vSInt32) -> vSInt32](./vs32fullmulodd%28_,_%29.md)
  Signed 32-bit multiplication; results are twice as wide as multiplicands, odd-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.
- [func vU64FullMulEven(vUInt32, vUInt32) -> vUInt32](./vu64fullmuleven%28_,_%29.md)
  Unsigned 64-bit multiplication; results are twice as wide as multiplicands, even-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.
- [func vU64FullMulOdd(vUInt32, vUInt32) -> vUInt32](./vu64fullmulodd%28_,_%29.md)
  Unsigned 64-bit multiplication; results are twice as wide as multiplicands, odd-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.
- [func vS64FullMulEven(vSInt32, vSInt32) -> vSInt32](./vs64fullmuleven%28_,_%29.md)
  Signed 64-bit multiplication; results are twice as wide as multiplicands, even-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.
- [func vS64FullMulOdd(vSInt32, vSInt32) -> vSInt32](./vs64fullmulodd%28_,_%29.md)
  Signed 64-bit multiplication; results are twice as wide as multiplicands, odd-numbered elements of multiplicand vectors are used.  Note the big-endian convention: the leftmost element is element 0.
- [func vU8Divide(vUInt8, vUInt8, UnsafeMutablePointer<vUInt8>?) -> vUInt8](./vu8divide%28_,_,_%29.md)
  Unsigned 8-bit division.
- [func vS8Divide(vSInt8, vSInt8, UnsafeMutablePointer<vSInt8>?) -> vSInt8](./vs8divide%28_,_,_%29.md)
  Signed 8-bit division.
- [func vU16Divide(vUInt16, vUInt16, UnsafeMutablePointer<vUInt16>?) -> vUInt16](./vu16divide%28_,_,_%29.md)
  Unsigned 16-bit division.
- [func vS16Divide(vSInt16, vSInt16, UnsafeMutablePointer<vSInt16>?) -> vSInt16](./vs16divide%28_,_,_%29.md)
  Signed 16-bit division.
- [func vU32Divide(vUInt32, vUInt32, UnsafeMutablePointer<vUInt32>?) -> vUInt32](./vu32divide%28_,_,_%29.md)
  Unsigned 32-bit division.
- [func vS32Divide(vSInt32, vSInt32, UnsafeMutablePointer<vSInt32>?) -> vSInt32](./vs32divide%28_,_,_%29.md)
  Signed 32-bit division.
- [func vU64Divide(vUInt32, vUInt32, UnsafeMutablePointer<vUInt32>?) -> vUInt32](./vu64divide%28_,_,_%29.md)
  Unsigned 64-bit division.
- [func vS64Divide(vSInt32, vSInt32, UnsafeMutablePointer<vSInt32>?) -> vSInt32](./vs64divide%28_,_,_%29.md)
  Signed 64-bit division.
- [func vU128Divide(vUInt32, vUInt32, UnsafeMutablePointer<vUInt32>?) -> vUInt32](./vu128divide%28_,_,_%29.md)
  Unsigned 128-bit division.
- [func vS128Divide(vSInt32, vSInt32, UnsafeMutablePointer<vSInt32>?) -> vSInt32](./vs128divide%28_,_,_%29.md)
  Signed 128-bit division.
- [vU64Add](./vu64add.md)
  Unsigned 64-bit addition (modular arithmetic).
- [vS64Add](./vs64add.md)
  Signed 64-bit addition (modular arithmetic).
- [vU64Sub](./vu64sub.md)
  Unsigned 64-bit subtraction (modular arithmetic).
- [vS64Sub](./vs64sub.md)
  Signed 64-bit subtraction (modular arithmetic).
- [vU16HalfMultiply](./vu16halfmultiply.md)
  Unsigned 16-bit multiplication; results are same width as multiplicands.
- [vS16HalfMultiply](./vs16halfmultiply.md)
  Signed 16-bit multiplication; results are same width as multiplicands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vbasicops)*