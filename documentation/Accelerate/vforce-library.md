# vForce

**Framework**: Accelerate

Perform transcendental and trigonometric functions on vectors of any length.

#### Overview

The vForce library provides a range of trigonometric and transcendental functions that work over large collections of single- and double-precision values. The collections can be of any length, and vForce supplies vectorized functions for the current architecture.

The functions declared in the vForce library have the customary mathematical names, but with the prefix `vv`, for example, [`vvsqrtf(_:_:_:)`](vvsqrtf(_:_:_:).md). Each mathematical function is available in two variants: one for single-precision data and one for double-precision data. The single-precision forms have the suffix `f`, whereas the double-precision forms have no suffix. For example, [`vvcosf(_:_:_:)`](vvcosf(_:_:_:).md) is the single-precision cosine function, and [`vvcos(_:_:_:)`](vvcos(_:_:_:).md) is the double-precision variant.

All of the vForce library functions follow a common format:

- The return type is `void`.
- The first parameter points to an array to hold the results. The only exceptions are [`vvsincosf(_:_:_:_:)`](vvsincosf(_:_:_:_:).md) and [`vvsincos(_:_:_:_:)`](vvsincos(_:_:_:_:).md), which have two result arrays that the first two parameters point to.
- One or more parameters point to operand arrays that are the same length as the result array.
- The last parameter is the array length.

> **Note**:  Unless otherwise mentioned, vForce functions work in-place. That is, the input may exactly equal the output.

##### Using Vforce

The vForce library provides a high-performance alternative to `for` loops and `map(_:)` when applying operations on arrays of floating-point values.

For example, given an arbitrarily sized array, `x`, that contains single-precision values, the following code uses `map(_:)` to create a second array, `y`. On return, `y` contains the square root of each array element.

```swift
let n = 10_000

let x = (0..<n).map { _ in
    Float.random(in: 1 ... 10_000)
}

let y = x.map {
    return sqrt($0)
}
```

The equivalent functionality implemented in vForce runs significantly faster:

```swift
let y = [Float](unsafeUninitializedCapacity: n) { buffer, initializedCount in
    vForce.sqrt(x,
                result: &buffer)
    
    initializedCount = n
}
```

## Topics

### Swift Overlay
- [enum vForce](vforce.md)
  An enumeration that acts as a namespace for Swift overlays to vForce.
### Array-Oriented Arithmetic and Auxiliary Functions
- [static func ceil<U>(U) -> [Double]](vforce/ceil(_:)-9dsdt.md)
  Returns the ceiling of each element in a vector of double-precision values.
- [static func ceil<U>(U) -> [Float]](vforce/ceil(_:)-57grr.md)
  Returns the ceiling of each element in a vector of single-precision values.
- [static func ceil<U, V>(U, result: inout V)](vforce/ceil(_:result:)-4wev4.md)
  Calculates the ceiling of each element in a vector of double-precision values.
- [static func ceil<U, V>(U, result: inout V)](vforce/ceil(_:result:)-6zm3u.md)
  Calculates the ceiling of each element in a vector of single-precision values.
- [static func copysign<U, V>(magnitudes: U, signs: V) -> [Double]](vforce/copysign(magnitudes:signs:)-s0r3.md)
  Returns each single-precision element in the magnitudes vector, setting its sign to the corresponding elements in the signs vector.
- [static func copysign<U, V>(magnitudes: U, signs: V) -> [Float]](vforce/copysign(magnitudes:signs:)-3jhf0.md)
  Returns each single-precision element in the magnitudes vector, setting its sign to the corresponding elements in the signs vector.
- [static func copysign<T, U, V>(magnitudes: T, signs: U, result: inout V)](vforce/copysign(magnitudes:signs:result:)-3zoya.md)
  Calculates each double-precision element in the magnitudes vector, setting its sign to the corresponding elements in the signs vector.
- [static func copysign<T, U, V>(magnitudes: T, signs: U, result: inout V)](vforce/copysign(magnitudes:signs:result:)-5umya.md)
  Calculates each single-precision element in the magnitudes vector, setting its sign to the corresponding elements in the signs vector.
- [static func floor<U>(U) -> [Double]](vforce/floor(_:)-64hyu.md)
  Returns the floor of each element in a vector of double-precision values.
- [static func floor<U>(U) -> [Float]](vforce/floor(_:)-5awna.md)
  Returns the floor of each element in a vector of single-precision values.
- [static func floor<U, V>(U, result: inout V)](vforce/floor(_:result:)-61veb.md)
  Calculates the floor of each element in a vector of double-precision values.
- [static func floor<U, V>(U, result: inout V)](vforce/floor(_:result:)-4mf4q.md)
  Calculates the floor of each element in a vector of single-precision values.
- [static func nearestInteger<U>(U) -> [Double]](vforce/nearestinteger(_:)-5mppu.md)
  Returns the nearest integer to each element in a vector of double-precision values.
- [static func nearestInteger<U>(U) -> [Float]](vforce/nearestinteger(_:)-386dx.md)
  Returns the nearest integer to each element in a vector of single-precision values.
- [static func nearestInteger<U, V>(U, result: inout V)](vforce/nearestinteger(_:result:)-bbtt.md)
  Calculates the nearest integer to each element in a vector of double-precision values.
- [static func nearestInteger<U, V>(U, result: inout V)](vforce/nearestinteger(_:result:)-1izut.md)
  Calculates the nearest integer to each element in a vector of double-precision values.
- [static func reciprocal<U>(U) -> [Double]](vforce/reciprocal(_:)-555of.md)
  Returns the reciprocal of each element in a vector of double-precision values.
- [static func reciprocal<U>(U) -> [Float]](vforce/reciprocal(_:)-8lozf.md)
  Returns the reciprocal of each element in a vector of single-precision values.
- [static func reciprocal<U, V>(U, result: inout V)](vforce/reciprocal(_:result:)-pvu0.md)
  Calculates the reciprocal of each element in a vector of double-precision values.
- [static func reciprocal<U, V>(U, result: inout V)](vforce/reciprocal(_:result:)-7hu7a.md)
  Calculates the reciprocal of each element in a vector of single-precision values.
- [static func remainder<U, V>(dividends: U, divisors: V) -> [Double]](vforce/remainder(dividends:divisors:)-5rcri.md)
  Returns the remainder of the double-precision elements in `dividends` divided by the elements in `divisors`, using truncating division.
- [static func remainder<U, V>(dividends: U, divisors: V) -> [Float]](vforce/remainder(dividends:divisors:)-j4a5.md)
  Returns the remainder of the single-precision elements in `dividends` divided by the elements in `divisors`, using truncating division.
- [static func remainder<T, U, V>(dividends: T, divisors: U, result: inout V)](vforce/remainder(dividends:divisors:result:)-bj3f.md)
  Calculates the remainder of the double-precision elements in `dividends` divided by the elements in `divisors`, using truncating division.
- [static func remainder<T, U, V>(dividends: T, divisors: U, result: inout V)](vforce/remainder(dividends:divisors:result:)-31qe5.md)
  Calculates the remainder of the single-precision elements in `dividends` divided by the elements in `divisors`, using truncating division.
- [static func rsqrt<U>(U) -> [Double]](vforce/rsqrt(_:)-9gm1h.md)
  Returns the reciprocal square root of each element in a vector of double-precision values.
- [static func rsqrt<U>(U) -> [Float]](vforce/rsqrt(_:)-2xjyq.md)
  Returns the reciprocal square root of each element in a vector of single-precision values.
- [static func rsqrt<U, V>(U, result: inout V)](vforce/rsqrt(_:result:)-9vniv.md)
  Calculates the reciprocal square root of each element in a vector of double-precision values.
- [static func rsqrt<U, V>(U, result: inout V)](vforce/rsqrt(_:result:)-6o0ky.md)
  Calculates the reciprocal square root of each element in a vector of single-precision values.
- [static func sqrt<U>(U) -> [Double]](vforce/sqrt(_:)-7ze6m.md)
  Returns the square root of each element in a vector of double-precision values.
- [static func sqrt<U>(U) -> [Float]](vforce/sqrt(_:)-8wla9.md)
  Returns the square root each element in a vector of single-precision values.
- [static func sqrt<U, V>(U, result: inout V)](vforce/sqrt(_:result:)-2ixfw.md)
  Calculates the square root of each element in a vector of double-precision values.
- [static func sqrt<U, V>(U, result: inout V)](vforce/sqrt(_:result:)-63m91.md)
  Calculates the square root of each element in a vector of single-precision values.
- [static func trunc<U>(U) -> [Double]](vforce/trunc(_:)-11ss3.md)
  Returns the integer truncation of each element in a vector of double-precision values.
- [static func trunc<U>(U) -> [Float]](vforce/trunc(_:)-5wx8z.md)
  Returns the integer truncation of each element in a vector of single-precision values.
- [static func trunc<U, V>(U, result: inout V)](vforce/trunc(_:result:)-8luud.md)
  Calculates the integer truncation of each element in a vector of double-precision values.
- [static func trunc<U, V>(U, result: inout V)](vforce/trunc(_:result:)-4xeiu.md)
  Calculates the integer truncation of each element in a vector of single-precision values.
- [static func truncatingRemainder<U, V>(dividends: U, divisors: V) -> [Double]](vforce/truncatingremainder(dividends:divisors:)-11bh4.md)
  Returns the remainder of the double-precision elements in `dividends` divided by the elements in `divisors`, using truncating division.
- [static func truncatingRemainder<U, V>(dividends: U, divisors: V) -> [Float]](vforce/truncatingremainder(dividends:divisors:)-9ofow.md)
  Returns the remainder of the single-precision elements in `dividends` divided by the elements in `divisors`, using truncating division.
- [static func truncatingRemainder<T, U, V>(dividends: T, divisors: U, result: inout V)](vforce/truncatingremainder(dividends:divisors:result:)-6forr.md)
  Calculates the remainder of the double-precision elements in `dividends` divided by the elements in `divisors`, using truncating division.
- [static func truncatingRemainder<T, U, V>(dividends: T, divisors: U, result: inout V)](vforce/truncatingremainder(dividends:divisors:result:)-23mq2.md)
  Calculates the remainder of the single-precision elements in `dividends` divided by the elements in `divisors`, using truncating division.
- [func vvceil(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvceil(_:_:_:).md)
  Calculates the ceiling of each element in an array of double-precision values.
- [func vvceilf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvceilf(_:_:_:).md)
  Calculates the ceiling of each element in an array of single-precision values.
- [func vvfloor(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvfloor(_:_:_:).md)
  Calculates the floor of each element in an array of double-precision values.
- [func vvfloorf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvfloorf(_:_:_:).md)
  Calculates the floor of each element in an array of single-precision values.
- [func vvcopysign(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvcopysign(_:_:_:_:).md)
  Copies an array, setting the sign of each element based on a second array of double-precision values.
- [func vvcopysignf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvcopysignf(_:_:_:_:).md)
  Copies an array, setting the sign of each element based on a second array of single-precision values.
- [func vvdiv(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvdiv(_:_:_:_:).md)
  Divides each element in an array by the corresponding value in a second array of double-precision values.
- [func vvdivf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvdivf(_:_:_:_:).md)
  Divides each element in an array by the corresponding value in a second array of single-precision values.
- [func vvfabs(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvfabs(_:_:_:).md)
  Calculates the absolute value for each element in an array of double-precision values.
- [func vvfabsf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvfabsf(_:_:_:).md)
  Calculates the absolute value for each element in an array of single-precision values.
- [func vvfmod(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvfmod(_:_:_:_:).md)
  Calculates the modulus after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [func vvfmodf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvfmodf(_:_:_:_:).md)
  Calculates the modulus after dividing each element in an array by the corresponding element in a second array of single-precision values.
- [func vvremainder(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvremainder(_:_:_:_:).md)
  Calculates the remainder after dividing each element in an array by the corresponding element in a second array of double-precision values.
- [func vvremainderf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvremainderf(_:_:_:_:).md)
  Calculates the remainder after dividing each element in an array by the corresponding element in a second array of single-precision values.
- [func vvint(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvint(_:_:_:).md)
  Calculates the integer truncation for each element in an array of double-precision values.
- [func vvintf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvintf(_:_:_:).md)
  Calculates the integer truncation for each element in an array of single-precision values.
- [func vvnint(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvnint(_:_:_:).md)
  Calculates the nearest integer for each element in an array of double-precision values.
- [func vvnintf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvnintf(_:_:_:).md)
  Calculates the nearest integer for each element in an array of single-precision values.
- [func vvrsqrt(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvrsqrt(_:_:_:).md)
  Calculates the reciprocal square root of each element in an array of double-precision values.
- [func vvrsqrtf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvrsqrtf(_:_:_:).md)
  Calculates the reciprocal square root of each element in an array of single-precision values.
- [func vvsqrt(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvsqrt(_:_:_:).md)
  Calculates the square root of each element in an array of double-precision values.
- [func vvsqrtf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvsqrtf(_:_:_:).md)
  Calculates the square root of each element in an array of single-precision values.
- [func vvrec(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvrec(_:_:_:).md)
  Calculates the reciprocal of each element in an array of double-precision values.
- [func vvrecf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvrecf(_:_:_:).md)
  Calculates the reciprocal of each element in an array of single-precision values.
- [func vvnextafter(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvnextafter(_:_:_:_:).md)
  Calculates the next machine-representable value for each element in an array of double-precision values.
- [func vvnextafterf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvnextafterf(_:_:_:_:).md)
  Calculates the next machine-representable value for each element in an array of single-precision values.
### Array-Oriented Exponential and Logarithmic Functions
- [static func exp<U>(U) -> [Double]](vforce/exp(_:)-76nrd.md)
  Returns the , raised to the power of each element in a vector of double-precision values.
- [static func exp<U>(U) -> [Float]](vforce/exp(_:)-5iaun.md)
  Returns the , raised to the power of each element in a vector of single-precision values.
- [static func exp<U, V>(U, result: inout V)](vforce/exp(_:result:)-34nxw.md)
  Calculates the , raised to the power of each element in a vector of double-precision values.
- [static func exp<U, V>(U, result: inout V)](vforce/exp(_:result:)-4k85n.md)
  Calculates the , raised to the power of each element in a vector of single-precision values.
- [static func exp2<U>(U) -> [Double]](vforce/exp2(_:)-2m5q.md)
  Returns the 2, raised to the power of each element in a vector of double-precision values.
- [static func exp2<U>(U) -> [Float]](vforce/exp2(_:)-4mm9y.md)
  Returns the 2, raised to the power of each element in a vector of single-precision values.
- [static func exp2<U, V>(U, result: inout V)](vforce/exp2(_:result:)-6ru6m.md)
  Calculates the 2, raised to the power of each element in a vector of double-precision values.
- [static func exp2<U, V>(U, result: inout V)](vforce/exp2(_:result:)-8m564.md)
  Calculates the 2, raised to the power of each element in a vector of single-precision values.
- [static func expm1<U>(U) -> [Double]](vforce/expm1(_:)-xkzx.md)
  Returns the  for each element in a vector of double-precision values.
- [static func expm1<U>(U) -> [Float]](vforce/expm1(_:)-mfq5.md)
  Returns the  for each element in a vector of single-precision values.
- [static func expm1<U, V>(U, result: inout V)](vforce/expm1(_:result:)-4dpl4.md)
  Calculates the  for each element in a vector of double-precision values.
- [static func expm1<U, V>(U, result: inout V)](vforce/expm1(_:result:)-2yhs3.md)
  Calculates the  for each element in a vector of single-precision values.
- [static func log10<U>(U) -> [Double]](vforce/log10(_:)-9wr68.md)
  Returns the base 10 logarithm of each element in a vector of double-precision values.
- [static func log<U>(U) -> [Double]](vforce/log(_:)-2gh9a.md)
  Returns the natural logarithm for each element in a vector of double-precision values.
- [static func log<U>(U) -> [Float]](vforce/log(_:)-5ffby.md)
  Returns the natural logarithm for each element in a vector of single-precision values.
- [static func log<U, V>(U, result: inout V)](vforce/log(_:result:)-84hv7.md)
  Calculates the natural logarithm for each element in a vector of double-precision values.
- [static func log<U, V>(U, result: inout V)](vforce/log(_:result:)-4k52e.md)
  Calculates the natural logarithm for each element in a vector of single-precision values.
- [static func log1p<U>(U) -> [Double]](vforce/log1p(_:)-5admq.md)
  Returns  for each element in a vector of double-precision values.
- [static func log1p<U>(U) -> [Float]](vforce/log1p(_:)-3wn9e.md)
  Returns  for each element in a vector of single-precision values.
- [static func log1p<U, V>(U, result: inout V)](vforce/log1p(_:result:)-8kk0n.md)
  Calculates  for each element in a vector of double-precision values.
- [static func log1p<U, V>(U, result: inout V)](vforce/log1p(_:result:)-5ckl.md)
  Calculates  for each element in a vector of single-precision values.
- [static func log10<U>(U) -> [Float]](vforce/log10(_:)-81jwh.md)
  Returns the base 10 logarithm of each element in a vector of single-precision values.
- [static func log10<U, V>(U, result: inout V)](vforce/log10(_:result:)-3j9cp.md)
  Calculates the base 10 logarithm of each element in a vector of double-precision values.
- [static func log10<U, V>(U, result: inout V)](vforce/log10(_:result:)-35727.md)
  Calculates the base 10 logarithm of each element in a vector of single-precision values.
- [static func log2<U>(U) -> [Double]](vforce/log2(_:)-2gkui.md)
  Returns the base 2 logarithm of each element in a vector of double-precision values.
- [static func log2<U>(U) -> [Float]](vforce/log2(_:)-9b3yo.md)
  Returns the base 2 logarithm of each element in a vector of single-precision values.
- [static func log2<U, V>(U, result: inout V)](vforce/log2(_:result:)-5xk1k.md)
  Calculates the base 2 logarithm of each element in a vector of double-precision values.
- [static func log2<U, V>(U, result: inout V)](vforce/log2(_:result:)-2i9yi.md)
  Calculates the base 2 logarithm of each element in a vector of single-precision values.
- [static func logb<U>(U) -> [Double]](vforce/logb(_:)-6irl7.md)
  Returns the unbiased exponent of each element in a vector of double-precision values.
- [static func logb<U>(U) -> [Float]](vforce/logb(_:)-6hwhw.md)
  Returns the unbiased exponent of each element in a vector of double-precision values.
- [static func logb<U, V>(U, result: inout V)](vforce/logb(_:result:)-14tuo.md)
  Calculates the unbiased exponent of each element in a vector of double-precision values.
- [static func logb<U, V>(U, result: inout V)](vforce/logb(_:result:)-1m3o3.md)
  Calculates the unbiased exponent of each element in a vector of single-precision values.
- [func vvexp(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvexp(_:_:_:).md)
  Calculates  raised to the power of each element in an array of double-precision values.
- [func vvexpf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvexpf(_:_:_:).md)
  Calculates  raised to the power of each element in an array of single-precision values.
- [func vvexp2(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvexp2(_:_:_:).md)
  Calculates 2 raised to the power of each element in an array of double-precision values.
- [func vvexp2f(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvexp2f(_:_:_:).md)
  Calculates 2 raised to the power of each element in an array of single-precision values.
- [func vvexpm1(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvexpm1(_:_:_:).md)
  Calculates  for each element in an array of double-precision values.
- [func vvexpm1f(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvexpm1f(_:_:_:).md)
  Calculates  for each element in an array of single-precision values.
- [func vvlog(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvlog(_:_:_:).md)
  Calculates the natural logarithm for each element in an array of double-precision values.
- [func vvlogf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvlogf(_:_:_:).md)
  Calculates the natural logarithm for each element in an array of single-precision values.
- [func vvlog1p(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvlog1p(_:_:_:).md)
  Calculates  for each element in an array of double-precision values.
- [func vvlog1pf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvlog1pf(_:_:_:).md)
  Calculates  for each element in an array of single-precision values.
- [func vvlog2(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvlog2(_:_:_:).md)
  Calculates the base 2 logarithm of each element in an array of double-precision values.
- [func vvlog2f(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvlog2f(_:_:_:).md)
  Calculates the base 2 logarithm of each element in an array of single-precision values.
- [func vvlog10(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvlog10(_:_:_:).md)
  Calculates the base 10 logarithm of each element in an array of double-precision values.
- [func vvlog10f(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvlog10f(_:_:_:).md)
  Calculates the base 10 logarithm of each element in an array of single-precision values.
- [func vvlogb(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvlogb(_:_:_:).md)
  Calculates the unbiased exponent of each element in an array of double-precision values.
- [func vvlogbf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvlogbf(_:_:_:).md)
  Calculates the unbiased exponent of each element in an array of single-precision values.
### Array-Oriented Power Functions
- [static func pow<U, V>(bases: U, exponents: V) -> [Double]](vforce/pow(bases:exponents:)-94dha.md)
  Returns each double-precision element in the bases vector, raised to the power of the corresponding element in the exponents vector.
- [static func pow<U, V>(bases: U, exponents: V) -> [Float]](vforce/pow(bases:exponents:)-3gl7v.md)
  Returns each single-precision element in the bases vector, raised to the power of the corresponding element in the exponents vector.
- [static func pow<T, U, V>(bases: T, exponents: U, result: inout V)](vforce/pow(bases:exponents:result:)-4bso.md)
  Calculates each double-precision element in the bases vector, raised to the power of the corresponding element in the exponents vector.
- [static func pow<T, U, V>(bases: T, exponents: U, result: inout V)](vforce/pow(bases:exponents:result:)-6pffz.md)
  Calculates each single-precision element in the bases vector, raised to the power of the corresponding element in the exponents vector.
- [func vvpow(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvpow(_:_:_:_:).md)
  Raises each element in an array to the power of the corresponding element in a second array of double-precision values.
- [func vvpowf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvpowf(_:_:_:_:).md)
  Raises each element in an array to the power of the corresponding element in a second array of single-precision values.
### Array-Oriented Trigonometric Functions
- [static func acos<U>(U) -> [Double]](vforce/acos(_:)-8srk.md)
  Returns the arccosine of each element in a vector of double-precision values.
- [static func acos<U>(U) -> [Float]](vforce/acos(_:)-3hl5t.md)
  Returns the arccosine of each element in a vector of single-precision values.
- [static func acos<U, V>(U, result: inout V)](vforce/acos(_:result:)-3c9qz.md)
  Calculates the arccosine of each element in a vector of double-precision values.
- [static func acos<U, V>(U, result: inout V)](vforce/acos(_:result:)-6rc2f.md)
  Calculates the arccosine of each element in a vector of single-precision values.
- [static func asin<U>(U) -> [Double]](vforce/asin(_:)-454ds.md)
  Returns the arcsine of each element in a vector of double-precision values.
- [static func asin<U>(U) -> [Float]](vforce/asin(_:)-8vvt1.md)
  Returns the arcsine of each element in a vector of single-precision values.
- [static func asin<U, V>(U, result: inout V)](vforce/asin(_:result:)-94jmy.md)
  Calculates the arcsine of each element in a vector of double-precision values.
- [static func asin<U, V>(U, result: inout V)](vforce/asin(_:result:)-ooti.md)
  Calculates the arcsine of each element in a vector of single-precision values.
- [static func atan<U>(U) -> [Double]](vforce/atan(_:)-1ghr3.md)
  Returns the arctangent of each element in a vector of double-precision values.
- [static func atan<U>(U) -> [Float]](vforce/atan(_:)-5ejvk.md)
  Returns the arctangent of each element in a vector of single-precision values.
- [static func atan<U, V>(U, result: inout V)](vforce/atan(_:result:)-691jp.md)
  Calculates the arctangent of each element in a vector of double-precision values.
- [static func atan<U, V>(U, result: inout V)](vforce/atan(_:result:)-6bb8n.md)
  Calculates the arctangent of each element in a vector of single-precision values.
- [static func atan2<U, V>(x: U, y: V) -> [Double]](vforce/atan2(x:y:)-h54u.md)
  Returns the arctangent of each pair of elements in two vectors of double-precision values.
- [static func atan2<U, V>(x: U, y: V) -> [Float]](vforce/atan2(x:y:)-3lku3.md)
  Returns the arctangent of each pair of elements in two vectors of single-precision values.
- [static func atan2<T, U, V>(x: T, y: U, result: inout V)](vforce/atan2(x:y:result:)-184b6.md)
  Calculates the arctangent of each pair of elements in two vectors of double-precision values.
- [static func atan2<T, U, V>(x: T, y: U, result: inout V)](vforce/atan2(x:y:result:)-6j6xb.md)
  Calculates the arctangent of each pair of elements in two vectors of single-precision values.
- [static func cos<U>(U) -> [Double]](vforce/cos(_:)-5eeyc.md)
  Returns the cosine of each element in a vector of double-precision values.
- [static func cos<U>(U) -> [Float]](vforce/cos(_:)-3q2fu.md)
  Returns the cosine of each element in a vector of single-precision values.
- [static func cos<U, V>(U, result: inout V)](vforce/cos(_:result:)-95syy.md)
  Calculates the cosine of each element in a vector of double-precision values.
- [static func cos<U, V>(U, result: inout V)](vforce/cos(_:result:)-lrow.md)
  Calculates the cosine of each element in a vector of single-precision values.
- [static func cosPi<U>(U) -> [Double]](vforce/cospi(_:)-8ouii.md)
  Returns the cosine of pi, multiplied by each element in a vector of double-precision values.
- [static func cosPi<U>(U) -> [Float]](vforce/cospi(_:)-578sc.md)
  Returns the cosine of pi, multiplied by each element in a vector of single-precision values.
- [static func cosPi<U, V>(U, result: inout V)](vforce/cospi(_:result:)-4rha2.md)
  Calculates the cosine of pi, multiplied by each element in a vector of double-precision values.
- [static func cosPi<U, V>(U, result: inout V)](vforce/cospi(_:result:)-5ubws.md)
  Calculates the cosine of pi, multiplied by each element in a vector of single-precision values.
- [static func sin<U>(U) -> [Double]](vforce/sin(_:)-61sn.md)
  Returns the sine of each element in a vector of double-precision values.
- [static func sin<U>(U) -> [Float]](vforce/sin(_:)-6o1ao.md)
  Returns the sine of each element in a vector of single-precision values.
- [static func sin<U, V>(U, result: inout V)](vforce/sin(_:result:)-6xo5w.md)
  Calculates the sine of each element in a vector of double-precision values.
- [static func sin<U, V>(U, result: inout V)](vforce/sin(_:result:)-oida.md)
  Calculates the sine of each element in a vector of single-precision values.
- [static func sinPi<U>(U) -> [Double]](vforce/sinpi(_:)-1wh5u.md)
  Returns the sine of pi, multiplied by each element in a vector of double-precision values.
- [static func sinPi<U>(U) -> [Float]](vforce/sinpi(_:)-3a7fm.md)
  Returns the sine of pi, multiplied by each element in a vector of single-precision values.
- [static func sinPi<U, V>(U, result: inout V)](vforce/sinpi(_:result:)-88a6o.md)
  Calculates the sine of pi, multiplied by each element in a vector of double-precision values.
- [static func sinPi<U, V>(U, result: inout V)](vforce/sinpi(_:result:)-9p5xq.md)
  Calculates the sine of pi, multiplied by each element in a vector of single-precision values.
- [static func sincos<T, U, V>(T, sinResult: inout U, cosResult: inout V)](vforce/sincos(_:sinresult:cosresult:)-93te.md)
  Calculates the sine and cosine of each element in a vector of double-precision values.
- [static func sincos<T, U, V>(T, sinResult: inout U, cosResult: inout V)](vforce/sincos(_:sinresult:cosresult:)-tk1q.md)
  Calculates the sine and cosine of each element in a vector of double-precision values.
- [static func tan<U>(U) -> [Double]](vforce/tan(_:)-6n5qw.md)
  Returns the tangent of each element in a vector of double-precision values.
- [static func tan<U>(U) -> [Float]](vforce/tan(_:)-3i3c1.md)
  Returns the tangent of each element in a vector of single-precision values.
- [static func tan<U, V>(U, result: inout V)](vforce/tan(_:result:)-8bosl.md)
  Calculates the tangent of each element in a vector of double-precision values.
- [static func tan<U, V>(U, result: inout V)](vforce/tan(_:result:)-4wevz.md)
  Calculates the tangent of each element in a vector of single-precision values.
- [static func tanPi<U>(U) -> [Double]](vforce/tanpi(_:)-9lrix.md)
  Returns the tangent of pi, multiplied by each element in a vector of double-precision values.
- [static func tanPi<U>(U) -> [Float]](vforce/tanpi(_:)-4z418.md)
  Returns the tangent of pi, multiplied by each element in a vector of single-precision values.
- [static func tanPi<U, V>(U, result: inout V)](vforce/tanpi(_:result:)-9d72p.md)
  Calculates the tangent of pi, multiplied by each element in a vector of double-precision values.
- [static func tanPi<U, V>(U, result: inout V)](vforce/tanpi(_:result:)-1gp8g.md)
  Calculates the tangent of pi, multiplied by each element in a vector of single-precision values.
- [func vvsin(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvsin(_:_:_:).md)
  Calculates the sine of each element in an array of double-precision values.
- [func vvsinf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvsinf(_:_:_:).md)
  Calculates the sine of each element in an array of single-precision values.
- [func vvsinpi(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvsinpi(_:_:_:).md)
  Calculates the sine of pi multiplied by each element in an array of double-precision values.
- [func vvsinpif(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvsinpif(_:_:_:).md)
  Calculates the sine of pi multiplied by each element in an array of single-precision values.
- [func vvcos(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvcos(_:_:_:).md)
  Calculates the cosine of each element in an array of double-precision values.
- [func vvcosf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvcosf(_:_:_:).md)
  Calculates the cosine of each element in an array of single-precision values.
- [func vvcospi(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvcospi(_:_:_:).md)
  Calculates the cosine of pi multiplied by each element in an array of double-precision values.
- [func vvcospif(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvcospif(_:_:_:).md)
  Calculates the cosine of pi multiplied by each element in an array of single-precision values.
- [func vvcosisin(OpaquePointer, UnsafePointer<Double>, UnsafePointer<Int32>)](vvcosisin(_:_:_:).md)
  Calculates the cosine and sine of each element in an array of double-precision values.
- [func vvcosisinf(OpaquePointer, UnsafePointer<Float>, UnsafePointer<Int32>)](vvcosisinf(_:_:_:).md)
  Calculates the cosine and sine of each element in an array of single-precision values.
- [func vvsincos(UnsafeMutablePointer<Double>, UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvsincos(_:_:_:_:).md)
  Calculates the cosine and sine of each element in an array of double-precision values.
- [func vvsincosf(UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvsincosf(_:_:_:_:).md)
  Calculates the cosine and sine of each element in an array of single-precision values.
- [func vvtan(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvtan(_:_:_:).md)
  Calculates the tangent of each element in an array of double-precision values.
- [func vvtanf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvtanf(_:_:_:).md)
  Calculates the tangent of each element in an array of single-precision values.
- [func vvtanpi(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvtanpi(_:_:_:).md)
  Calculates the tangent of pi multiplied by each element in an array of double-precision values.
- [func vvtanpif(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvtanpif(_:_:_:).md)
  Calculates the tangent of pi multiplied by each element in an array of single-precision values.
- [func vvasin(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvasin(_:_:_:).md)
  Calculates the arcsine of each element in an array of double-precision values.
- [func vvasinf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvasinf(_:_:_:).md)
  Calculates the arcsine of each element in an array of single-precision values.
- [func vvacos(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvacos(_:_:_:).md)
  Calculates the arccosine of each element in an array of double-precision values.
- [func vvacosf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvacosf(_:_:_:).md)
  Calculates the arccosine of each element in an array of single-precision values.
- [func vvatan(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvatan(_:_:_:).md)
  Calculates the arctangent of each element in an array of double-precision values.
- [func vvatanf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvatanf(_:_:_:).md)
  Calculates the arctangent of each element in an array of single-precision values.
- [func vvatan2(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvatan2(_:_:_:_:).md)
  Calculates the arctangent of each pair of elements in two arrays of double-precision values.
- [func vvatan2f(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvatan2f(_:_:_:_:).md)
  Calculates the arctangent of each pair of elements in two arrays of single-precision values.
### Array-Oriented Hyperbolic Functions
- [static func acosh<U>(U) -> [Double]](vforce/acosh(_:)-1j3qt.md)
  Returns the inverse hyperbolic cosine of each element in a vector of double-precision values.
- [static func acosh<U>(U) -> [Float]](vforce/acosh(_:)-8zjay.md)
  Returns the inverse hyperbolic cosine of each element in a vector of single-precision values.
- [static func acosh<U, V>(U, result: inout V)](vforce/acosh(_:result:)-4cip0.md)
  Calculates the inverse hyperbolic cosine of each element in a vector of double-precision values.
- [static func acosh<U, V>(U, result: inout V)](vforce/acosh(_:result:)-2r23w.md)
  Calculates the inverse hyperbolic cosine of each element in a vector of single-precision values.
- [static func asinh<U>(U) -> [Double]](vforce/asinh(_:)-ue6b.md)
  Returns the inverse hyperbolic sine of each element in a vector of double-precision values.
- [static func asinh<U>(U) -> [Float]](vforce/asinh(_:)-284n7.md)
  Returns the inverse hyperbolic sine of each element in a vector of single-precision values.
- [static func asinh<U, V>(U, result: inout V)](vforce/asinh(_:result:)-7wn57.md)
  Calculates the inverse hyperbolic sine of each element in a vector of double-precision values.
- [static func asinh<U, V>(U, result: inout V)](vforce/asinh(_:result:)-17vv4.md)
  Calculates the inverse hyperbolic sine of each element in a vector of single-precision values.
- [static func atanh<U>(U) -> [Double]](vforce/atanh(_:)-922d.md)
  Returns the inverse hyperbolic tangent of each element in a vector of double-precision values.
- [static func atanh<U>(U) -> [Float]](vforce/atanh(_:)-2t372.md)
  Returns the inverse hyperbolic tangent of each element in a vector of single-precision values.
- [static func atanh<U, V>(U, result: inout V)](vforce/atanh(_:result:)-6waj3.md)
  Calculates the inverse hyperbolic tangent of each element in a vector of double-precision values.
- [static func atanh<U, V>(U, result: inout V)](vforce/atanh(_:result:)-596wg.md)
  Calculates the inverse hyperbolic tangent of each element in a vector of single-precision values.
- [static func cosh<U>(U) -> [Double]](vforce/cosh(_:)-4dmhm.md)
  Returns the hyperbolic cosine of each element in a vector of double-precision values.
- [static func cosh<U>(U) -> [Float]](vforce/cosh(_:)-5ax3f.md)
  Returns the hyperbolic cosine of each element in a vector of single-precision values.
- [static func cosh<U, V>(U, result: inout V)](vforce/cosh(_:result:)-4f7in.md)
  Calculates the hyperbolic cosine of each element in a vector of double-precision values.
- [static func cosh<U, V>(U, result: inout V)](vforce/cosh(_:result:)-3x3wu.md)
  Calculates the hyperbolic cosine of each element in a vector of single-precision values.
- [static func sinh<U>(U) -> [Double]](vforce/sinh(_:)-54hpe.md)
  Returns the hyperbolic sine of each element in a vector of double-precision values.
- [static func sinh<U>(U) -> [Float]](vforce/sinh(_:)-fwj2.md)
  Returns the hyperbolic sine of each element in a vector of single-precision values.
- [static func sinh<U, V>(U, result: inout V)](vforce/sinh(_:result:)-6xge8.md)
  Calculates the hyperbolic sine of each element in a vector of double-precision values.
- [static func sinh<U, V>(U, result: inout V)](vforce/sinh(_:result:)-1ag0e.md)
  Calculates the hyperbolic sine of each element in a vector of single-precision values.
- [static func tanh<U>(U) -> [Double]](vforce/tanh(_:)-89qjn.md)
  Returns the hyperbolic tangent of each element in a vector of double-precision values.
- [static func tanh<U>(U) -> [Float]](vforce/tanh(_:)-4h4en.md)
  Returns the hyperbolic tangent of each element in a vector of single-precision values.
- [static func tanh<U, V>(U, result: inout V)](vforce/tanh(_:result:)-3fuc9.md)
  Calculates the hyperbolic tangent of each element in a vector of double-precision values.
- [static func tanh<U, V>(U, result: inout V)](vforce/tanh(_:result:)-1fzsa.md)
  Calculates the hyperbolic tangent of each element in a vector of single-precision values.
- [func vvsinh(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvsinh(_:_:_:).md)
  Calculates the hyperbolic sine of each element in an array of double-precision values.
- [func vvsinhf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvsinhf(_:_:_:).md)
  Calculates the hyperbolic sine of each element in an array of single-precision values.
- [func vvcosh(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvcosh(_:_:_:).md)
  Calculates the hyperbolic cosine of each element in an array of double-precision values.
- [func vvcoshf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvcoshf(_:_:_:).md)
  Calculates the hyperbolic cosine of each element in an array of single-precision values.
- [func vvtanh(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvtanh(_:_:_:).md)
  Calculates the hyperbolic tangent of each element in an array of double-precision values.
- [func vvtanhf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvtanhf(_:_:_:).md)
  Calculates the hyperbolic tangent of each element in an array of single-precision values.
- [func vvasinh(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvasinh(_:_:_:).md)
  Calculates the inverse hyperbolic sine of each element in an array of double-precision values.
- [func vvasinhf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvasinhf(_:_:_:).md)
  Calculates the inverse hyperbolic sine of each element in an array of single-precision values.
- [func vvacosh(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvacosh(_:_:_:).md)
  Calculates the inverse hyperbolic cosine of each element in an array of double-precision values.
- [func vvacoshf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvacoshf(_:_:_:).md)
  Calculates the inverse hyperbolic cosine of each element in an array of single-precision values.
- [func vvatanh(UnsafeMutablePointer<Double>, UnsafePointer<Double>, UnsafePointer<Int32>)](vvatanh(_:_:_:).md)
  Calculates the inverse hyperbolic tangent of each element in an array of double-precision values.
- [func vvatanhf(UnsafeMutablePointer<Float>, UnsafePointer<Float>, UnsafePointer<Int32>)](vvatanhf(_:_:_:).md)
  Calculates the inverse hyperbolic tangent of each element in an array of single-precision values.
### Data Types
- [typealias COMPLEX](complex.md)
- [typealias DOUBLE_COMPLEX](double_complex.md)

## See Also

- [Working with Vectors](working-with-vectors.md)
  Use vectors to calculate geometric values, calculate dot products and cross products, and interpolate between values.
- [Working with Matrices](working-with-matrices.md)
  Solve simultaneous equations and transform points in space.
- [Working with Quaternions](working-with-quaternions.md)
  Rotate points around the surface of a sphere, and interpolate between them.
- [Rotating a cube by transforming its vertices](rotating-a-cube-by-transforming-its-vertices.md)
  Rotate a cube through a series of keyframes using quaternion interpolation to transition between them.
- [simd](simd-library.md)
  Perform computations on small vectors and matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vforce-library)*