# Vector distance and Pythagorean computation

**Framework**: Accelerate  
**Role**: API Collection

Calculate distance and hypotenuse of vectors.

## Topics

### Vector hypotenuse computation
- [static func hypot<U, V>(U, V) -> [Float]](./vdsp/hypot%28_,_%29-5grex.md)
  Returns the single-precision hypotenuses of right triangles with legs that are the lengths of corresponding elements of the two input vectors.
- [static func hypot<U, V>(U, V) -> [Double]](./vdsp/hypot%28_,_%29-7ku7m.md)
  Returns the double-precision hypotenuses of right triangles with legs that are the lengths of corresponding elements of the two input vectors.
- [static func hypot<T, U, V>(T, U, result: inout V)](./vdsp/hypot%28_,_,result%29-5d8pw.md)
  Calculates the single-precision hypotenuses of right triangles with legs that are the lengths of corresponding elements of the two input vectors.
- [static func hypot<T, U, V>(T, U, result: inout V)](./vdsp/hypot%28_,_,result%29-1z10j.md)
  Calculates the double-precision hypotenuses of right triangles with legs that are the lengths of corresponding elements of the two input vectors.
- [static func hypot<R, S, T, U>(x0: R, x1: S, y0: T, y1: U) -> [Float]](./vdsp/hypot%28x0,x1,y0,y1%29-15wy5.md)
  Returns the single-precision hypotenuses of right triangles with legs that are the differences of corresponding elements of two pairs of vectors.
- [static func hypot<R, S, T, U>(x0: R, x1: S, y0: T, y1: U) -> [Double]](./vdsp/hypot%28x0,x1,y0,y1%29-12d4r.md)
  Returns the double-precision hypotenuses of right triangles with legs that are the differences of corresponding elements of two pairs of vectors.
- [static func hypot<R, S, T, U, V>(x0: R, x1: S, y0: T, y1: U, result: inout V)](./vdsp/hypot%28x0,x1,y0,y1,result%29-7ksm.md)
  Calculates the single-precision hypotenuses of right triangles with legs that are the differences of corresponding elements of two pairs of vectors.
- [static func hypot<R, S, T, U, V>(x0: R, x1: S, y0: T, y1: U, result: inout V)](./vdsp/hypot%28x0,x1,y0,y1,result%29-4pizr.md)
  Calculates the double-precision hypotenuses of right triangles with legs that are the differences of corresponding elements of two pairs of vectors.
### Vector distance computation
- [static func distanceSquared<U, V>(U, V) -> Float](./vdsp/distancesquared%28_,_%29-2dvb6.md)
  Returns the single-precision distance squared between two points in n-dimensional space.
- [static func distanceSquared<U, V>(U, V) -> Double](./vdsp/distancesquared%28_,_%29-3oub3.md)
  Returns the double-precision distance squared between two points in n-dimensional space.

## See Also

### Vector geometry functions
- [Dot product calculation](./dot-product-calculation.md)
  Calculate the scalar product of two vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vector-distance-and-pythagorean-computation)*