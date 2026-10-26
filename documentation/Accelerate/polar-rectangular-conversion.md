# Polar-rectangular conversion

**Framework**: Accelerate  
**Role**: API Collection

Convert each element of a vector between radius-angle and Cartesian pairs.

## Topics

### Converting polar coordinates to rectangular coordinates
- [static func polarToRectangular<U>(U) -> [Float]](./vdsp/polartorectangular%28_%29-8upqj.md)
  Returns single-precision rectangular coordinates converted from polar coordinates.
- [static func polarToRectangular<U>(U) -> [Double]](./vdsp/polartorectangular%28_%29-jgv8.md)
  Returns double-precision rectangular coordinates converted from polar coordinates.
- [static func convert<U, V>(polarCoordinates: U, toRectangularCoordinates: inout V)](./vdsp/convert%28polarcoordinates,torectangularcoordinates%29-3vpjf.md)
  Converts single-precision polar coordinates to rectangular coordinates.
- [static func convert<U, V>(polarCoordinates: U, toRectangularCoordinates: inout V)](./vdsp/convert%28polarcoordinates,torectangularcoordinates%29-22zz0.md)
  Converts double-precision polar coordinates to rectangular coordinates.
- [vDSP_rect](./vdsp_rect.md)
  Converts single-precision polar coordinates to rectangular coordinates, using the specified stride.
- [vDSP_rectD](./vdsp_rectd.md)
  Converts double-precision polar coordinates to rectangular coordinates, using the specified stride.
### Converting rectangular coordinates to polar coordinates
- [static func rectangularToPolar<U>(U) -> [Float]](./vdsp/rectangulartopolar%28_%29-5p4kg.md)
  Returns single-precision polar coordinates converted from rectangular coordinates.
- [static func rectangularToPolar<U>(U) -> [Double]](./vdsp/rectangulartopolar%28_%29-3txg1.md)
  Returns double-precision polar coordinates converted from rectangular coordinates.
- [static func convert<U, V>(rectangularCoordinates: U, toPolarCoordinates: inout V)](./vdsp/convert%28rectangularcoordinates,topolarcoordinates%29-1zi4t.md)
  Converts single-precision rectangular coordinates to polar coordinates.
- [static func convert<U, V>(rectangularCoordinates: U, toPolarCoordinates: inout V)](./vdsp/convert%28rectangularcoordinates,topolarcoordinates%29-84131.md)
  Converts double-precision rectangular coordinates to polar coordinates.
- [vDSP_polar](./vdsp_polar.md)
  Converts single-precision rectangular coordinates to polar coordinates, using the specified stride.
- [vDSP_polarD](./vdsp_polard.md)
  Converts double-precision rectangular coordinates to polar coordinates, using the specified stride.

## See Also

### Vector conversion functions
- [Conversion to decibel equivalents](./conversion-to-decibel-equivalents.md)
  Convert vectors that contain power or amplitude data to decibels.
- [Type conversion](./type-conversion.md)
  Perform element-wise floating-point to integer and integer to floating-point conversion.
- [Complex vector conversion](./complex-vector-conversion.md)
  Perform element-wise split-complex to interleaved and interleaved to split-complex conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/polar-rectangular-conversion)*