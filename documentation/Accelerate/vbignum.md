# vBigNum

**Framework**: Accelerate

Perform arithmetic and logical functions on large integers.

#### Overview

The vBigNum module provides arithmetic and logical operations on large integers with lengths of 128, 256, 512, or 1024 bits.

vBigNum includes data types that represent large integer quantities, such as [`vS512`](vs512.md), which defines a 512-bit signed integer. The function names begin with the data type, followed by the name of the operation. For example, [`vS512Add(_:_:_:)`](vs512add(_:_:_:).md) performs the addition of two 512-bit signed integers.

## Topics

### Shifting and rotating large integers
- [func vLL256Shift(UnsafePointer<vU256>, UInt32, UnsafeMutablePointer<vU256>)](vll256shift(_:_:_:).md)
  256-bit logical left shift.
- [func vLR256Shift(UnsafePointer<vU256>, UInt32, UnsafeMutablePointer<vU256>)](vlr256shift(_:_:_:).md)
  256-bit logical right shift.
- [func vA256Shift(UnsafePointer<vS256>, UInt32, UnsafeMutablePointer<vS256>)](va256shift(_:_:_:).md)
  256-bit arithmetic shift.
- [func vLL512Shift(UnsafePointer<vU512>, UInt32, UnsafeMutablePointer<vU512>)](vll512shift(_:_:_:).md)
  512-bit logical left shift.
- [func vLR512Shift(UnsafePointer<vU512>, UInt32, UnsafeMutablePointer<vU512>)](vlr512shift(_:_:_:).md)
  512-bit logical right shift .
- [func vA512Shift(UnsafePointer<vS512>, UInt32, UnsafeMutablePointer<vS512>)](va512shift(_:_:_:).md)
  512-bit arithmetic shift.
- [func vLL1024Shift(UnsafePointer<vU1024>, UInt32, UnsafeMutablePointer<vU1024>)](vll1024shift(_:_:_:).md)
  1024-bit logical left shift.
- [func vLR1024Shift(UnsafePointer<vU1024>, UInt32, UnsafeMutablePointer<vU1024>)](vlr1024shift(_:_:_:).md)
  1024-bit logical right shift .
- [func vA1024Shift(UnsafePointer<vS1024>, UInt32, UnsafeMutablePointer<vS1024>)](va1024shift(_:_:_:).md)
  1024-bit arithmetic shift.
- [func vL256Rotate(UnsafePointer<vU256>, UInt32, UnsafeMutablePointer<vU256>)](vl256rotate(_:_:_:).md)
  256-bit left rotate.
- [func vR256Rotate(UnsafePointer<vU256>, UInt32, UnsafeMutablePointer<vU256>)](vr256rotate(_:_:_:).md)
  256-bit right rotate.
- [func vL512Rotate(UnsafePointer<vU512>, UInt32, UnsafeMutablePointer<vU512>)](vl512rotate(_:_:_:).md)
  512-bit left rotate.
- [func vR512Rotate(UnsafePointer<vU512>, UInt32, UnsafeMutablePointer<vU512>)](vr512rotate(_:_:_:).md)
  512-bit right rotate.
- [func vL1024Rotate(UnsafePointer<vU1024>, UInt32, UnsafeMutablePointer<vU1024>)](vl1024rotate(_:_:_:).md)
  1024-bit left rotate.
- [func vR1024Rotate(UnsafePointer<vU1024>, UInt32, UnsafeMutablePointer<vU1024>)](vr1024rotate(_:_:_:).md)
  1024-bit right rotate.
### Performing arithmetic operations on large integers
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
- [func vS256SubS(UnsafePointer<vS256>, UnsafePointer<vS256>, UnsafeMutablePointer<vS256>)](vs256subs(_:_:_:).md)
  Signed 256-bit subtraction with saturation (clipping).
- [func vU512Sub(UnsafePointer<vU512>, UnsafePointer<vU512>, UnsafeMutablePointer<vU512>)](vu512sub(_:_:_:).md)
  Unsigned 512-bit subtraction (modular arithmetic).
- [func vU512SubS(UnsafePointer<vU512>, UnsafePointer<vU512>, UnsafeMutablePointer<vU512>)](vu512subs(_:_:_:).md)
  Unsigned 512-bit subtraction with saturation (clipping).
- [func vS512Sub(UnsafePointer<vS512>, UnsafePointer<vS512>, UnsafeMutablePointer<vS512>)](vs512sub(_:_:_:).md)
  Signed 512-bit subtraction (modular arithmetic).
- [func vS512SubS(UnsafePointer<vS512>, UnsafePointer<vS512>, UnsafeMutablePointer<vS512>)](vs512subs(_:_:_:).md)
  Signed 512-bit subtraction with saturation (clipping).
- [func vU1024Sub(UnsafePointer<vU1024>, UnsafePointer<vU1024>, UnsafeMutablePointer<vU1024>)](vu1024sub(_:_:_:).md)
  Unsigned 1024-bit subtraction (modular arithmetic).
- [func vU1024SubS(UnsafePointer<vU1024>, UnsafePointer<vU1024>, UnsafeMutablePointer<vU1024>)](vu1024subs(_:_:_:).md)
  Unsigned 1024-bit subtraction with saturation (clipping).
- [func vS1024Sub(UnsafePointer<vS1024>, UnsafePointer<vS1024>, UnsafeMutablePointer<vS1024>)](vs1024sub(_:_:_:).md)
  Signed 1024-bit subtraction (modular arithmetic).
- [func vS1024SubS(UnsafePointer<vS1024>, UnsafePointer<vS1024>, UnsafeMutablePointer<vS1024>)](vs1024subs(_:_:_:).md)
  Signed 1024-bit subtraction with saturation (clipping).
- [func vU64Neg(vUInt32) -> vUInt32](vu64neg(_:).md)
  Unsigned 64-bit negation.
- [func vU128Neg(vUInt32) -> vUInt32](vu128neg(_:).md)
  Unsigned 128-bit negation.
- [func vU256Neg(UnsafePointer<vU256>, UnsafeMutablePointer<vU256>)](vu256neg(_:_:).md)
  Unsigned 256-bit negation.
- [func vS64Neg(vSInt32) -> vSInt32](vs64neg(_:).md)
  Signed 64-bit negation.
- [func vS128Neg(vSInt32) -> vSInt32](vs128neg(_:).md)
  Signed 128-bit negation.
- [func vS256Neg(UnsafePointer<vS256>, UnsafeMutablePointer<vS256>)](vs256neg(_:_:).md)
  Signed 256-bit negation.
- [func vU512Neg(UnsafePointer<vU512>, UnsafeMutablePointer<vU512>)](vu512neg(_:_:).md)
  Unsigned 512-bit negation.
- [func vS512Neg(UnsafePointer<vS512>, UnsafeMutablePointer<vS512>)](vs512neg(_:_:).md)
  Signed 512-bit negation.
- [func vU1024Neg(UnsafePointer<vU1024>, UnsafeMutablePointer<vU1024>)](vu1024neg(_:_:).md)
  Unsigned 1024-bit negation.
- [func vS1024Neg(UnsafePointer<vS1024>, UnsafeMutablePointer<vS1024>)](vs1024neg(_:_:).md)
  Signed 1024-bit negation.
- [func vU256Mod(UnsafePointer<vU256>, UnsafePointer<vU256>, UnsafeMutablePointer<vU256>)](vu256mod(_:_:_:).md)
  Unsigned 256-bit mod.
- [func vS256Mod(UnsafePointer<vS256>, UnsafePointer<vS256>, UnsafeMutablePointer<vS256>)](vs256mod(_:_:_:).md)
  Signed 256-bit mod.
- [func vU512Mod(UnsafePointer<vU512>, UnsafePointer<vU512>, UnsafeMutablePointer<vU512>)](vu512mod(_:_:_:).md)
  Unsigned 512-bit mod.
- [func vS512Mod(UnsafePointer<vS512>, UnsafePointer<vS512>, UnsafeMutablePointer<vS512>)](vs512mod(_:_:_:).md)
  Signed 512-bit mod.
- [func vU1024Mod(UnsafePointer<vU1024>, UnsafePointer<vU1024>, UnsafeMutablePointer<vU1024>)](vu1024mod(_:_:_:).md)
  Unsigned 1024-bit mod.
- [func vS1024Mod(UnsafePointer<vS1024>, UnsafePointer<vS1024>, UnsafeMutablePointer<vS1024>)](vs1024mod(_:_:_:).md)
  Signed 256-bit Mod.
- [func vU256HalfMultiply(UnsafePointer<vU256>, UnsafePointer<vU256>, UnsafeMutablePointer<vU256>)](vu256halfmultiply(_:_:_:).md)
  Unsigned 256-bit multiplication; result is the same width as multiplicands.
- [func vS256HalfMultiply(UnsafePointer<vS256>, UnsafePointer<vS256>, UnsafeMutablePointer<vS256>)](vs256halfmultiply(_:_:_:).md)
  Signed 256-bit multiplication; result is the same width as multiplicands.
- [func vU512HalfMultiply(UnsafePointer<vU512>, UnsafePointer<vU512>, UnsafeMutablePointer<vU512>)](vu512halfmultiply(_:_:_:).md)
  Unsigned 512-bit multiplication; result is the same width as multiplicands.
- [func vS512HalfMultiply(UnsafePointer<vS512>, UnsafePointer<vS512>, UnsafeMutablePointer<vS512>)](vs512halfmultiply(_:_:_:).md)
  Signed 512-bit multiplication; result is the same width as multiplicands.
- [func vU1024HalfMultiply(UnsafePointer<vU1024>, UnsafePointer<vU1024>, UnsafeMutablePointer<vU1024>)](vu1024halfmultiply(_:_:_:).md)
  Unsigned 1024-bit multiplication; result is the same width as multiplicands.
- [func vS1024HalfMultiply(UnsafePointer<vS1024>, UnsafePointer<vS1024>, UnsafeMutablePointer<vS1024>)](vs1024halfmultiply(_:_:_:).md)
  Signed 1024-bit multiplication; result is the same width as multiplicands.
- [func vU128FullMultiply(UnsafePointer<vU128>, UnsafePointer<vU128>, UnsafeMutablePointer<vU256>)](vu128fullmultiply(_:_:_:).md)
  Unsigned 128-bit multiplication; result is twice as wide as multiplicands.
- [func vS128FullMultiply(UnsafePointer<vS128>, UnsafePointer<vS128>, UnsafeMutablePointer<vS256>)](vs128fullmultiply(_:_:_:).md)
  Signed 128-bit multiplication; result is twice as wide as multiplicands.
- [func vU256FullMultiply(UnsafePointer<vU256>, UnsafePointer<vU256>, UnsafeMutablePointer<vU512>)](vu256fullmultiply(_:_:_:).md)
  Unsigned 256-bit multiplication; result is twice as wide as multiplicands.
- [func vS256FullMultiply(UnsafePointer<vS256>, UnsafePointer<vS256>, UnsafeMutablePointer<vS512>)](vs256fullmultiply(_:_:_:).md)
  Signed 256-bit multiplication; result is twice as wide as multiplicands.
- [func vU512FullMultiply(UnsafePointer<vU512>, UnsafePointer<vU512>, UnsafeMutablePointer<vU1024>)](vu512fullmultiply(_:_:_:).md)
  Unsigned 512-bit multiplication; result is twice as wide as multiplicands.
- [func vS512FullMultiply(UnsafePointer<vS512>, UnsafePointer<vS512>, UnsafeMutablePointer<vS1024>)](vs512fullmultiply(_:_:_:).md)
  Signed 512-bit multiplication; result is twice as wide as multiplicands.
- [func vU256Divide(UnsafePointer<vU256>, UnsafePointer<vU256>, UnsafeMutablePointer<vU256>, UnsafeMutablePointer<vU256>?)](vu256divide(_:_:_:_:).md)
  Unsigned 256-bit division.
- [func vS256Divide(UnsafePointer<vS256>, UnsafePointer<vS256>, UnsafeMutablePointer<vS256>, UnsafeMutablePointer<vS256>?)](vs256divide(_:_:_:_:).md)
  Computes the signed 256-bit division.
- [func vU512Divide(UnsafePointer<vU512>, UnsafePointer<vU512>, UnsafeMutablePointer<vU512>, UnsafeMutablePointer<vU512>?)](vu512divide(_:_:_:_:).md)
  Computes the unsigned 512-bit division.
- [func vS512Divide(UnsafePointer<vS512>, UnsafePointer<vS512>, UnsafeMutablePointer<vS512>, UnsafeMutablePointer<vS512>?)](vs512divide(_:_:_:_:).md)
  Signed 512-bit division.
- [func vU1024Divide(UnsafePointer<vU1024>, UnsafePointer<vU1024>, UnsafeMutablePointer<vU1024>, UnsafeMutablePointer<vU1024>?)](vu1024divide(_:_:_:_:).md)
  Unsigned 1024-bit division.
- [func vS1024Divide(UnsafePointer<vS1024>, UnsafePointer<vS1024>, UnsafeMutablePointer<vS1024>, UnsafeMutablePointer<vS1024>?)](vs1024divide(_:_:_:_:).md)
  Signed 1024-bit division.
### Data types
- [struct vU128](vu128.md)
  A union containing one `vUInt32` vector or four 32-bit integers, representing a 128-bit unsigned integer.
- [struct vS128](vs128.md)
  A union containing one `vSInt32` vector or four 32-bit integers, representing a 128-bit signed integer.
- [struct vU256](vu256.md)
  A union containing an array or structure of two `vUInt32` vectors or eight 32-bit integers, representing a 256-bit unsigned integer.
- [struct vS256](vs256.md)
  A union containing an array or structure of two `vUInt32` vectors or eight 32-bit integers, representing a 256-bit signed integer.
- [struct vU512](vu512.md)
  A union containing an array or structure of four `vUInt32` vectors or sixteen 32-bit integers, representing a 256-bit unsigned integer.
- [struct vS512](vs512.md)
  A union containing an array or structure of four `vUInt32` vectors or sixteen 32-bit integers, representing a 256-bit signed integer.
- [struct vU1024](vu1024.md)
  A union containing an array or structure of eight `vUInt32` vectors or thirty-two 32-bit integers, representing a 1024-bit unsigned integer.
- [struct vS1024](vs1024.md)
  A union containing an array or structure of eight `vUInt32` vectors or thirty-two 32-bit integers, representing a 1024-bit signed integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vbignum)*