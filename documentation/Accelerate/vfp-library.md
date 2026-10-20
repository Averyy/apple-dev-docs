# vfp

**Framework**: Accelerate  
**Role**: API Collection

Perform floating-point arithmetic, transcendental, and trigonometric functions on 128-bit vectors.

#### Overview

vfp.h declares a set of floating-point arithmetic, transcendental and trigonometric functions, on 128-bit vectors, using the floating-point types from vecLibTypes.h.

These functions are named with their customary mathematical names, prefixed with the letter “v”, and all except `vtablelookup()` have the suffix “f” to indicate that they work with single-precision floating-point data. For example, `vcosf` is the single-precision cosine function.

## Topics

### Floating-Point Arithmetic and Auxiliary Functions (from vfp.h)
- [func vceilf(vFloat) -> vFloat](./vceilf%28_%29.md)
  Computes the ceiling of values in a vector of floating-point values.
- [func vcopysignf(vFloat, vFloat) -> vFloat](./vcopysignf%28_,_%29.md)
  For each vector element, produces a value with the magnitude of `arg2` and sign `arg1`.  Note that the order of the arguments matches the recommendation of the IEEE 754 floating-point standard, which is opposite from the SANE copysign function.
- [func vdivf(vFloat, vFloat) -> vFloat](./vdivf%28_,_%29.md)
  For each vector element, calculates `A`/`B`.
- [func vfabf(vFloat) -> vFloat](./vfabf%28_%29.md)
  For each vector element, calculates the absolute value of `v`.
- [func vfabsf(vFloat) -> vFloat](./vfabsf%28_%29.md)
- [func vfloorf(vFloat) -> vFloat](./vfloorf%28_%29.md)
  Computes the floor of values in a vector of floating-point values.
- [func vintf(vFloat) -> vFloat](./vintf%28_%29.md)
  Truncates the decimal portion of a vector of floating-point values.
- [func vnintf(vFloat) -> vFloat](./vnintf%28_%29.md)
  Rounds to the nearest integer (nearest even for ties).
- [func vnextafterf(vFloat, vFloat) -> vFloat](./vnextafterf%28_,_%29.md)
  For each vector element, calculates the next representable value after `x` in the direction of `y`.  If `x` is equal to `y`, then `y` is returned.
- [func vrecf(vFloat) -> vFloat](./vrecf%28_%29.md)
  Computes the reciprocal of values in a vector.
- [func vrsqrtf(vFloat) -> vFloat](./vrsqrtf%28_%29.md)
  For each vector element, calculates the inverse of the square root of `X`.
- [func vsqrtf(vFloat) -> vFloat](./vsqrtf%28_%29.md)
  For each vector element, calculates the square root of `X`.
- [func vtablelookup(vSInt32, UnsafeMutablePointer<UInt32>) -> vUInt32](./vtablelookup%28_,_%29.md)
  For each vector element of `Index_Vect`, returns the corresponding value from `Table`.
- [func vtruncf(vFloat) -> vFloat](./vtruncf%28_%29.md)
### Exponential and Logarithmic Functions (from vfp.h)
- [func vexpf(vFloat) -> vFloat](./vexpf%28_%29.md)
  For each vector element, calculates the exponential of X.
- [func vexp2f(vFloat) -> vFloat](./vexp2f%28_%29.md)
- [func vexpm1f(vFloat) -> vFloat](./vexpm1f%28_%29.md)
  For each vector element, calculates ExpM1(x) = Exp(x) - 1.  But, for small enough arguments, ExpM1(x) is expected to be more accurate than Exp(x) - 1.
- [func vlogf(vFloat) -> vFloat](./vlogf%28_%29.md)
  For each vector element, calculates the natural logarithm of `X`.
- [func vlog1pf(vFloat) -> vFloat](./vlog1pf%28_%29.md)
  For each vector element, calculates Log1P = Log(1 + x). But, for small enough arguments, Log1P is expected to be more accurate than Log(1 + x).
- [func vlog10f(vFloat) -> vFloat](./vlog10f%28_%29.md)
  Computes the base-10 logarithm of values in a vector.
- [func vlogbf(vFloat) -> vFloat](./vlogbf%28_%29.md)
  For each vector element, extracts the exponent of `X`, as a signed integral value. A subnormal argument is treated as though it were first normalized. Thus:   1  <=  x * 2^(-logb(x))  <  2.
- [func vlog2f(vFloat) -> vFloat](./vlog2f%28_%29.md)
- [func vvpows(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](./vvpows%28_,_,_,_%29.md)
  Calculates the cube root for each element of a vector.
- [func vvpowsf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](./vvpowsf%28_,_,_,_%29.md)
  Calculates, element-wise, x**y for a vector x and a scalar y.
- [func vscalbf(vFloat, vSInt32) -> vFloat](./vscalbf%28_,_%29.md)
  For each vector element, calculates x * 2^n efficiently.  This is not normally done by computing 2^n explicitly.
### Trigonometric Functions (from vfp.h)
- [func vsinf(vFloat) -> vFloat](./vsinf%28_%29.md)
  For each vector element, calculates the sine.
- [func vcosf(vFloat) -> vFloat](./vcosf%28_%29.md)
  For each vector element, calculates the cosine.
- [func vsincosf(vFloat, UnsafeMutablePointer<vFloat>) -> vFloat](./vsincosf%28_,_%29.md)
  Simultaneously computes sine and cosine of values in a vector.
- [func vtanf(vFloat) -> vFloat](./vtanf%28_%29.md)
  For each vector element, calculates the tangent.
- [func vasinf(vFloat) -> vFloat](./vasinf%28_%29.md)
  For each vector element, calculates the arcsine.  Results are in the interval [-pi/2, pi/2].
- [func vacosf(vFloat) -> vFloat](./vacosf%28_%29.md)
  For each vector element, calculates the arccosine.  Results are in the interval [0, pi].
- [func vatanf(vFloat) -> vFloat](./vatanf%28_%29.md)
  For each vector element, calculates the arctangent.  Results are in the interval [-pi/2, pi/2].
- [func vatan2f(vFloat, vFloat) -> vFloat](./vatan2f%28_,_%29.md)
  For each vector element, calculates the arctangent of `arg2`/`arg1` in the interval [-pi,pi] using the sign of both arguments to determine the quadrant of the computed value.
- [func vvcbrt(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](./vvcbrt%28_,_,_%29.md)
  Calculates the cube root for each element of a vector.
- [func vvcbrtf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](./vvcbrtf%28_,_,_%29.md)
  Calculates the cube root for each element of a vector.
### Hyperbolic Functions (from vfp.h)
- [func vsinhf(vFloat) -> vFloat](./vsinhf%28_%29.md)
  For each vector element, calculates the hyperbolic sine of `X`.
- [func vcoshf(vFloat) -> vFloat](./vcoshf%28_%29.md)
  For each vector element, calculates the hyperbolic cosine of `X`.
- [func vtanhf(vFloat) -> vFloat](./vtanhf%28_%29.md)
  For each vector element, calculates the hyperbolic tangent of `X`.
- [func vasinhf(vFloat) -> vFloat](./vasinhf%28_%29.md)
  For each vector element, calculates the inverse hyperbolic sine of `X`.
- [func vacoshf(vFloat) -> vFloat](./vacoshf%28_%29.md)
  For each vector element, calculates the inverse hyperbolic cosine of `X`.
- [func vatanhf(vFloat) -> vFloat](./vatanhf%28_%29.md)
  For each vector element, calculates the inverse hyperbolic tangent of `X`.
### Power Functions (from vfp.h)
- [func vipowf(vFloat, vSInt32) -> vFloat](./vipowf%28_,_%29.md)
  For each vector element, calculates `X` to the integer power of `Y`.
- [func vpowf(vFloat, vFloat) -> vFloat](./vpowf%28_,_%29.md)
  For each vector element, calculates `X` to the floating-point power of `Y`. The result is more accurate than using exp(log(`X`)*`Y`).
### Remainder Functions (from vfp.h)
- [func vfmodf(vFloat, vFloat) -> vFloat](./vfmodf%28_,_%29.md)
  For each vector element, calculates `X` modulo `Y`.
- [func vremainderf(vFloat, vFloat) -> vFloat](./vremainderf%28_,_%29.md)
  For each vector element, calculates the remainder of `X`/`Y`, according to the IEEE 754 floating-point standard.
- [func vremquof(vFloat, vFloat, UnsafeMutablePointer<vUInt32>) -> vFloat](./vremquof%28_,_,_%29.md)
  For each vector element, calculates the remainder of `X`/`Y`, according to the SANE standard. It stores into `QUO` the 7 low-order bits of the integer quotient, such that -127 <= `QUO` <= 127.
### Inquiry Functions (from vfp.h)
- [func vclassifyf(vFloat) -> vUInt32](./vclassifyf%28_%29.md)
  For each vector element, returns the class of the argument (one of the FP_ … constants defined in math.h).
- [func vsignbitf(vFloat) -> vUInt32](./vsignbitf%28_%29.md)
  For each vector element, returns a non-zero value if and only if the sign of `arg` is negative. This includes NaNs, infinities and zeros.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vfp-library)*