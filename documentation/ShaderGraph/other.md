# Other

**Framework**: ShaderGraph  
**Kind**: dictionary

Perform a wide variety of miscellaneous operations.

## Topics

### Nodes
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
- [All (RealityKit)](other/all-(realitykit).md)
  Returns true only if all components of x are true.
- [Any (RealityKit)](other/any-(realitykit).md)
  Returns true only if any component of x is true.
- [Is Finite (RealityKit)](other/is-finite-(realitykit).md)
  Returns true if the incoming value is finite.
- [Is Infinite (RealityKit)](other/is-infinite-(realitykit).md)
  Returns true if the incoming value is infinite.
- [Is Not a Number (RealityKit)](other/is-not-a-number-(realitykit).md)
  Returns true if the incoming value is a not a number (NaN).
- [Is Normal (RealityKit)](other/is-normal-(realitykit).md)
  Test if the incoming value is a normalized floating-point value.
- [Is Ordered (RealityKit)](other/is-ordered-(realitykit).md)
  Test if arguments are ordered. Returns the result (X == X) && (Y == Y).
- [Is Unordered (RealityKit)](other/is-unordered-(realitykit).md)
  Test if arguments are unordered. Returns true if X or Y is NaN, otherwise returns false.
- [Sign Bit (RealityKit)](other/sign-bit-(realitykit).md)
  Tests for sign bit. Returns true if the sign bit is set for the value in X, otherwise returns false.
- [Select (RealityKit)](other/select-(realitykit).md)
  Selects B if conditional is true, A if false.
- [Inverse Hyperbolic Cos](other/inverse-hyperbolic-cos.md)
  The inverse hyperbolic cosine of the incoming value in radians.
- [Inverse Hyperbolic Sin](other/inverse-hyperbolic-sin.md)
  The inverse hyperbolic sine of the incoming value in radians.
- [Atan](other/atan.md)
  The arctangent of the incoming value in radians.
- [Inverse Hyperbolic Tan](other/inverse-hyperbolic-tan.md)
  The hyperbolic arc tangent of the incoming value in radians.
- [Copy Sign (RealityKit)](other/copy-sign-(realitykit).md)
  Return x with its sign changed to match the sign of y.
- [Hyperbolic Cos](other/hyperbolic-cos.md)
  The hyperbolic cosine of the incoming value in radians.
- [Cos Pi (RealityKit)](other/cos-pi-(realitykit).md)
  Compute cos(πX).
- [Exponential 2 (RealityKit)](other/exponential-2-(realitykit).md)
  Exponential Base 2 of X.
- [Exponential 10 (RealityKit)](other/exponential-10-(realitykit).md)
  Exponential Base 10 of X.
- [Fortran Difference and Minimum (RealityKit)](other/fortran-difference-and-minimum-(realitykit).md)
  Returns X – Y if X > Y, or +0 if X <= Y.
- [Fused Multiply-Add (RealityKit)](other/fused-multiply-add-(realitykit).md)
  Returns (A * B) + C.
- [Max (RealityKit)](other/max-(realitykit).md)
  Outputs the maximum of two incoming values.
- [Min (RealityKit)](other/min-(realitykit).md)
  Outputs the minimum of two incoming values.
- [Modulo (RealityKit)](other/modulo-(realitykit).md)
  Outputs the remaining fraction after dividing the input by a value and subtracting the integer portion.
- [Fractional-(RealityKit)](other/fractional-(realitykit).md)
  Returns the fractional part of a floating point number.
- [Power Positive (RealityKit)](other/power-positive-(realitykit).md)
  Computes X to the power of Y, where X is >= 0
- [Round Integral (RealityKit)](other/round-integral-(realitykit).md)
  Rounds X to integral value using round ties to even rounding mode in floating-point format.
- [Reciprocal Square Root (RealityKit)](other/reciprocal-square-root-(realitykit).md)
  Computes inverse square root of X.
- [Hyperbolic Sin](other/hyperbolic-sin.md)
  The hyperbolic sine of the incoming value in radians.
- [Sin Pi (RealityKit)](other/sin-pi-(realitykit).md)
  Compute sin(πX).
- [Hyperbolic Tan](other/hyperbolic-tan.md)
  The hyperbolic tangent of the incoming value in radians.
- [Tan Pi (RealityKit)](other/tan-pi-(realitykit).md)
  Compute tan(πX).
- [Truncate (RealityKit)](other/truncate-(realitykit).md)
  Rounds X to integral value using the round-toward-zero rounding mode.
- [Distance (RealityKit)](other/distance-(realitykit).md)
  Returns the distance between X and Y.
- [Distance Square (RealityKit)](other/distance-square-(realitykit).md)
  Returns the square of the distance between X and Y.
- [Magnitude Square (RealityKit)](other/magnitude-square-(realitykit).md)
  Outputs the float magnitude of a vector, squared.
- [Screen-Space X Partial Derivative (RealityKit)](other/screen-space-x-partial-derivative-(realitykit).md)
  Returns a high-precision partial derivative of the specified value with respect to the screen space X coordinate.
- [Screen-Space Y Partial Derivative (RealityKit)](other/screen-space-y-partial-derivative-(realitykit).md)
  Returns a high-precision partial derivative of the specified value with respect to the screen space Y coordinate.
- [Absolute Derivatives Sum (RealityKit)](other/absolute-derivatives-sum-(realitykit).md)
  Returns the sum of the absolute derivatives in X and Y using local differencing for p; that is, fabs(dfdx(p)) + fabs(dfdy(p)).
- [Log 2](other/log-2.md)
  The log base 2 of the input.
- [Log 10](other/log-10.md)
  The log base 10 of the input.
- [Reflection Diffuse (RealityKit)](other/reflection-diffuse-(realitykit).md)
  Diffuse component of reflection.
- [Reflection Specular (RealityKit)](other/reflection-specular-(realitykit).md)
  Specular component of reflection.
### Subscripts
- [Absolute-(RealityKit)](other/absolute-(realitykit)-146ys.md)
  Outputs the per-channel absolute value of the input.
- [Absolute-(RealityKit)](other/absolute-(realitykit)-5niip.md)
  Compute absolute value of a floating-point number.
- [Max3-(RealityKit)](other/max3-(realitykit)-6nj67.md)
  Outputs the maximum of three incoming values.
- [Max3-(RealityKit)](other/max3-(realitykit)-8ww2g.md)
  Outputs the maximum of three incoming values.
- [Median3-(RealityKit)](other/median3-(realitykit)-2iusb.md)
  Returns the middle value of three incoming values.
- [Median3-(RealityKit)](other/median3-(realitykit)-t96k.md)
  Returns the middle value of three incoming values.
- [Min3-(RealityKit)](other/min3-(realitykit)-1c3iu.md)
  Outputs the minimum of three incoming values.
- [Min3-(RealityKit)](other/min3-(realitykit)-6x2f6.md)
  Outputs the minimum of three incoming values.
- [Multiply-High-(RealityKit)](other/multiply-high-(realitykit)-20zzc.md)
  Computes X * Y and returns the high half.
- [Multiply-High-(RealityKit)](other/multiply-high-(realitykit)-jif4.md)
  Computes X * Y and returns the high half with Z added to the product.

## See Also

- [2D-Procedural](2d-procedural.md)
  Generate 2D gradients, noise, and other patterns programmatically for your material.
- [2D-Texture](2d-texture.md)
  Load and configure 2D texture files.
- [3D-Procedural](3d-procedural.md)
  Generate 3D noise patterns programmatically for your material.
- [3D-Texture](3d-texture.md)
  Project multiple 2D images onto a surface to create a 3D texture.
- [Adjustment](adjustment.md)
  Modify or convert values, or ranges of values, from one form to another.
- [Application](application.md)
  Get system values such as the current time or the direction of the up vector.
- [Compositing](compositing.md)
  Generate a single output from the combination of multiple data values.
- [Data](data.md)
  Convert data values to different formats, or manipulate individual elements within a data structure.
- [Geometric](geometric.md)
  Access scene geometry while your graph runs.
- [Logic](logic.md)
  Perform Boolean operations and other logical comparisons on data values.
- [Material](material.md)
  Encapsulate a set of shader graph nodes into a single module.
- [Math](math.md)
  Perform a wide variety of mathematical and transformative operations on data values.
- [Organization](organization.md)
  Modify the visual flow of data within your graph without changing any values.
- [Procedural](procedural.md)
  Add a constant number, vector, matrix, color, string, or other value to your graph.
- [RealityKit](realitykit.md)
  Add RealityKit surfaces or textures to your material and access and manipulate scene geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/other)*