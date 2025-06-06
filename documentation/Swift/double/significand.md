# significand

**Framework**: Swift  
**Kind**: property

The significand of the floating-point value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var significand: Double { get }
```

#### Discussion

The magnitude of a floating-point value `x` of type `F` can be calculated by using the following formula, where `**` is exponentiation:

```swift
x.significand * (F.radix ** x.exponent)
```

In the next example, `y` has a value of `21.5`, which is encoded as `1.34375 * 2 ** 4`. The significand of `y` is therefore 1.34375.

```swift
let y: Double = 21.5
// y.significand == 1.34375
// y.exponent == 4
// Double.radix == 2
```

If a type’s radix is 2, then for finite nonzero numbers, the significand is in the range `1.0 ..< 2.0`. For other values of `x`, `x.significand` is defined as follows:

- If `x` is zero, then `x.significand` is 0.0.
- If `x` is infinite, then `x.significand` is infinity.
- If `x` is NaN, then `x.significand` is NaN.

> **Note**: The significand is frequently also called the , but significand is the preferred terminology in the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933), to allay confusion with the use of mantissa for the fractional part of a logarithm.

The significand is frequently also called the , but significand is the preferred terminology in the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933), to allay confusion with the use of mantissa for the fractional part of a logarithm.

## See Also

- [var ulp: Double](double/ulp.md)
  The unit in the last place of this value.
- [var exponent: Int](double/exponent-swift.property.md)
  The exponent of the floating-point value.
- [var nextUp: Double](double/nextup.md)
  The least representable value that compares greater than this value.
- [var nextDown: Self](double/nextdown.md)
  The greatest representable value that compares less than this value.
- [var binade: Double](double/binade.md)
  The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/significand)*