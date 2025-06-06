# Truncate (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript

Rounds X to integral value using the round-toward-zero rounding mode.

#### Parameter Types

## See Also

- [Add Saturate (RealityKit)](other/add-saturate-(realitykit).md)
  Returns X + Y and saturates the result.
- [Count Leading Zeros (RealityKit)](other/count-leading-zeros-(realitykit).md)
  Returns the number of leading 0-bits in X, starting at the most significant bit position.
- [Count Trailing Zeros (RealityKit)](other/count-trailing-zeros-(realitykit).md)
  Returns the count of trailing 0-bits in X, starting at the least significant bit position.
- [Extract Bits (RealityKit)](other/extract-bits-(realitykit).md)
  Extract bits [Offset, Offset + Bits - 1] from X, returning them in the least significant bits of the result.
- [Integer Average, Rounded Down (RealityKit)](other/integer-average,-rounded-down-(realitykit).md)
  Uses the `hadd` metal instruction to return (x + y) >> 1. The intermediate sum does not modulo overflow.
- [Insert Bits (RealityKit)](other/insert-bits-(realitykit).md)
  Returns the insertion of the Bits least-significant bits of Insert into Base.  The result has bits [Offset, Offset + Bits - 1] taken from bits [0, Bits - 1] of Insert, and all other bits are taken directly from the corresponding bits of Base.
- [Multiply Add Saturate (RealityKit)](other/multiply-add-saturate-(realitykit).md)
  Returns A * B + C and saturates the result.
- [Count Non Zeros (RealityKit)](other/count-non-zeros-(realitykit).md)
  Returns the number of non-zero bits in X.
- [Reverse Bits (RealityKit)](other/reverse-bits-(realitykit).md)
  Returns the reversal of the bits of X. The bit numbered N of the result is taken from bit (Bits – 1) – n of X, where Bits is the total number of bits used to represent X.
- [Integer Average, Rounded Up (RealityKit)](other/integer-average,-rounded-up-(realitykit).md)
  Uses the `rhadd` metal instruction to return (x + y + 1) >> 1. The intermediate sum does not modulo overflow.
- [Rotate Bits (RealityKit)](other/rotate-bits-(realitykit).md)
  For each element in V,the bits are shifted left by the corresponding element in I. Bits shifted off the left side of the element are shifted back in from the right.
- [Subtract Saturate (RealityKit)](other/subtract-saturate-(realitykit).md)
  Returns X – Y and saturates the result.
- [Absolute Diff (RealityKit)](other/absolute-diff-(realitykit).md)
  Return |X - Y| without modulo overflow.
- [Multiply Add 24 (RealityKit)](other/multiply-add-24-(realitykit).md)
  Multiplies two 24-bit integer values X and Y and returns the 32-bit integer result with 32-bit Z value added. X and Y are 32-bit integers but only the low 24 bits perform the multiplication.
- [Multiply 24 (RealityKit)](other/multiply-24-(realitykit).md)
  Multiplies two 24-bit integer values X and Y and returns the 32-bit integer result. X and Y are 32-bit integers but only the low 24 bits perform the multiplication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/other/truncate-(realitykit))*