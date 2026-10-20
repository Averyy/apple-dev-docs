# Conversion to decibel equivalents

**Framework**: Accelerate  
**Role**: API Collection

Convert vectors that contain power or amplitude data to decibels.

## Topics

### Converting single-precision power or amplitude values to decibel values
- [static func amplitudeToDecibels<U>(U, zeroReference: Float) -> [Float]](./vdsp/amplitudetodecibels%28_,zeroreference%29-88bpy.md)
  Returns single-precision amplitude values converted to decibels.
- [static func powerToDecibels<U>(U, zeroReference: Float) -> [Float]](./vdsp/powertodecibels%28_,zeroreference%29-861j5.md)
  Returns single-precision power values converted to decibel values.
- [static func convert<U, V>(amplitude: U, toDecibels: inout V, zeroReference: Float)](./vdsp/convert%28amplitude,todecibels,zeroreference%29-83uy1.md)
  Converts single-precision amplitude values to decibel values.
- [static func convert<U, V>(power: U, toDecibels: inout V, zeroReference: Float)](./vdsp/convert%28power,todecibels,zeroreference%29-5u3vs.md)
  Converts single-precision power values to decibel values.
### Converting double-precision power or amplitude values to decibel values
- [static func amplitudeToDecibels<U>(U, zeroReference: Double) -> [Double]](./vdsp/amplitudetodecibels%28_,zeroreference%29-2cgik.md)
  Returns double-precision amplitude values converted to decibel values.
- [static func powerToDecibels<U>(U, zeroReference: Double) -> [Double]](./vdsp/powertodecibels%28_,zeroreference%29-4b0qz.md)
  Returns double-precision power values converted to decibel values.
- [static func convert<U, V>(amplitude: U, toDecibels: inout V, zeroReference: Double)](./vdsp/convert%28amplitude,todecibels,zeroreference%29-4io4p.md)
  Converts double-precision amplitude values to decibel values.
- [static func convert<U, V>(power: U, toDecibels: inout V, zeroReference: Double)](./vdsp/convert%28power,todecibels,zeroreference%29-3aiv4.md)
  Converts double-precision power values to decibel values.

## See Also

### Vector conversion functions
- [Type conversion](./type-conversion.md)
  Perform element-wise floating-point to integer and integer to floating-point conversion.
- [Complex vector conversion](./complex-vector-conversion.md)
  Perform element-wise split-complex to interleaved and interleaved to split-complex conversion.
- [Polar-rectangular conversion](./polar-rectangular-conversion.md)
  Convert each element of a vector between radius-angle and Cartesian pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/conversion-to-decibel-equivalents)*