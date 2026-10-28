# isSubnormal

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether this decimal is subnormal.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isSubnormal: Bool { get }
```

## Discussion

A *subnormal* value is a nonzero number that has a lesser magnitude than the smallest normal number. Subnormal values do not use the full precision available to values of a type.

Zero is neither a normal nor a subnormal number. Subnormal numbers are often called *denormal* or *denormalized*—these are different names for the same concept.

## See Also

### Getting a decimal’s characteristics
- [var sign: FloatingPointSign](./sign.md)
  The sign of the decimal.
- [var exponent: Int](./exponent.md)
  The exponent of the decimal.
- [var significand: Decimal](./significand.md)
  The significand of the decimal.
- [var magnitude: Decimal](./magnitude.md)
  The magnitude of this decimal.
- [var floatingPointClass: FloatingPointClassification](./floatingpointclass.md)
  The IEEE 754 class of this type.
- [var isCanonical: Bool](./iscanonical.md)
  A Boolean value indicating whether the representation of this decimal is canonical.
- [var isFinite: Bool](./isfinite.md)
  A Boolean value indicating whether this decimal is zero, subnormal, or normal (not infinity or NaN).
- [var isInfinite: Bool](./isinfinite.md)
  A Boolean value indicating whether this decimal is infinity.
- [var isNaN: Bool](./isnan.md)
  A Boolean value indicating whether this decimal is NaN.
- [var isNormal: Bool](./isnormal.md)
  A Boolean value indicating whether this decimal is normal (not zero, subnormal, infinity, or NaN).
- [var isSignMinus: Bool](./issignminus.md)
  A Boolean value indicating whether this decimal has a negative sign.
- [var isSignaling: Bool](./issignaling.md)
  A Boolean value indicating whether this decimal is a signaling NaN.``
- [var isSignalingNaN: Bool](./issignalingnan.md)
  A Boolean value indicating whether this decimal is a signaling NaN.
- [var isZero: Bool](./iszero.md)
  A Boolean value indicating whether this value is zero.
- [var nextDown: Decimal](./nextdown.md)
  The greatest representable value that is less than this decimal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/issubnormal)*