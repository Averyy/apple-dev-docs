# vvpowf(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Raises each element in an array to the power of the corresponding element in a second array of single-precision values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vvpowf(_: UnsafeMutablePointer<Float>, _: UnsafePointer<Float>, _: UnsafePointer<Float>, _: UnsafePointer<Int32>)
```

#### Discussion

##### Parameters

The following code shows an example of using [`vvpowf(_:_:_:_:)`](vvpowf(_:_:_:_:).md):

The following special values of `x` and `y` produce the given value of `z`:

| x (base) | y (exponent) | z (result) |
| --- | --- | --- |
| `odd integer, <0` | `+/-0` | `+/-inf` |
| `odd integer, >0` | `+/-0` | `+/-0` |
| `otherwise, <0` | `+/-0` | `+inf` |
| `otherwise, >0` | `+/-0` | `+0` |
| `+/-inf` | `-1` | `1` |
| `NaN` | `+1` | `1` |
| `+/-0` | `NaN` | `1` |
| `-inf` | `|x|<1` | `+inf` |
| `-inf` | `|x|>1` | `+0` |
| `+inf` | `|x|<1` | `+0` |
| `+inf` | `|x|>1` | `+inf` |
| `odd integer, <0` | `-inf` | `-0` |
| `odd integer, >0` | `-inf` | `-inf` |
| `otherwise, <0` | `-inf` | `+0` |
| `otherwise, >0` | `-inf` | `+inf` |
| `<0` | `+inf` | `+0` |
| `>0` | `+inf` | `+inf` |
| `non-integer` | `<0` | `NaN` |

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vvpowf(_:_:_:_:))*