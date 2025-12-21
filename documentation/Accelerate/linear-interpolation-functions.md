# Linear interpolation functions

**Framework**: Accelerate

Compute the linear average between two vectors or between the neighboring elements in one vector.

## Topics

### Vector-to-Vector Linear Interpolation
- [static func linearInterpolate<T, U>(T, U, using: Double) -> [Double]](vdsp/linearinterpolate(_:_:using:)-3j5d2.md)
  Returns the linear interpolation between the supplied double-precision vectors.
- [static func linearInterpolate<T, U>(T, U, using: Float) -> [Float]](vdsp/linearinterpolate(_:_:using:)-71as1.md)
  Returns the linear interpolation between the supplied single-precision vectors.
- [static func linearInterpolate<T, U, V>(T, U, using: Double, result: inout V)](vdsp/linearinterpolate(_:_:using:result:)-6o7a9.md)
  Calculates the linear interpolation between the supplied double-precision vectors.
- [static func linearInterpolate<T, U, V>(T, U, using: Float, result: inout V)](vdsp/linearinterpolate(_:_:using:result:)-55avl.md)
  Calculates the linear interpolation between the supplied single-precision vectors.
### Single-Vector Linear Interpolation
- [Using linear interpolation to construct new data points](using-linear-interpolation-to-construct-new-data-points.md)
  Fill the gaps in arrays of numerical data using linear interpolation.
- [static func linearInterpolate<T, U>(elementsOf: T, using: U) -> [Double]](vdsp/linearinterpolate(elementsof:using:)-5i3jc.md)
  Returns the interpolation between the neighboring elements of a double-precision vector.
- [static func linearInterpolate<T, U>(elementsOf: T, using: U) -> [Float]](vdsp/linearinterpolate(elementsof:using:)-49r3c.md)
  Returns the interpolation between the neighboring elements of a single-precision vector.
- [static func linearInterpolate<T, U, V>(elementsOf: T, using: U, result: inout V)](vdsp/linearinterpolate(elementsof:using:result:)-4n3lr.md)
  Calculates the interpolation between the neighboring elements of a double-precision vector.
- [static func linearInterpolate<T, U, V>(elementsOf: T, using: U, result: inout V)](vdsp/linearinterpolate(elementsof:using:result:)-9y61c.md)
  Calculates the interpolation between the neighboring elements of a single-precision vector.

## See Also

- [Quadratic interpolation functions](quadratic-interpolation-functions.md)
  Compute the quadratic interpolation between the neighboring elements in a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/linear-interpolation-functions)*