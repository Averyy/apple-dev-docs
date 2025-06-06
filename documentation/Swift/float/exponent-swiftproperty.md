# exponent

**Framework**: Swift  
**Kind**: property

The exponent of the floating-point value.

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
var exponent: Int { get }
```

#### Discussion

The  of a floating-point value is the integer part of the logarithm of the value’s magnitude. For a value `x` of a floating-point type `F`, the magnitude can be calculated as the following, where `**` is exponentiation:

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

The `exponent` property has the following edge cases:

- If `x` is zero, then `x.exponent` is `Int.min`.
- If `x` is +/-infinity or NaN, then `x.exponent` is `Int.max`

This property implements the `logB` operation defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## See Also

- [var ulp: Float](float/ulp.md)
  The unit in the last place of this value.
- [var significand: Float](float/significand.md)
  The significand of the floating-point value.
- [var nextUp: Float](float/nextup.md)
  The least representable value that compares greater than this value.
- [var nextDown: Self](float/nextdown.md)
  The greatest representable value that compares less than this value.
- [var binade: Float](float/binade.md)
  The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/exponent-swift.property)*