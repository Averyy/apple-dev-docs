# pow(bases:exponents:)

**Framework**: Accelerate  
**Kind**: method

Returns each double-precision element in the bases vector, raised to the power of the corresponding element in the exponents vector.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
static func pow<U, V>(bases: U, exponents: V) -> [Double] where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Double, V.Element == Double
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vforce/pow(bases:exponents:)-94dha)*