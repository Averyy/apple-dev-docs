# isFinite

**Framework**: Foundation  
**Kind**: property

A Boolean value indicating whether this decimal is zero, subnormal, or normal (not infinity or NaN).

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
var isFinite: Bool { get }
```

## See Also

- [var sign: FloatingPointSign](decimal/sign.md)
  The sign of the decimal.
- [var exponent: Int](decimal/exponent.md)
  The exponent of the decimal.
- [var significand: Decimal](decimal/significand.md)
  The significand of the decimal.
- [var floatingPointClass: FloatingPointClassification](decimal/floatingpointclass.md)
  The IEEE 754 class of this type.
- [var isCanonical: Bool](decimal/iscanonical.md)
  A Boolean value indicating whether the representation of this decimal is canonical.
- [var isInfinite: Bool](decimal/isinfinite.md)
  A Boolean value indicating whether this decimal is infinity.
- [var isNaN: Bool](decimal/isnan.md)
  A Boolean value indicating whether this decimal is NaN.
- [var isNormal: Bool](decimal/isnormal.md)
  A Boolean value indicating whether this decimal is normal (not zero, subnormal, infinity, or NaN).
- [var isSignMinus: Bool](decimal/issignminus.md)
  A Boolean value indicating whether this decimal has a negative sign.
- [var isSignaling: Bool](decimal/issignaling.md)
  A Boolean value indicating whether this decimal is a signaling NaN.``
- [var isSignalingNaN: Bool](decimal/issignalingnan.md)
  A Boolean value indicating whether this decimal is a signaling NaN.
- [var isSubnormal: Bool](decimal/issubnormal.md)
  A Boolean value indicating whether this decimal is subnormal.
- [var isZero: Bool](decimal/iszero.md)
  A Boolean value indicating whether this value is zero.
- [var nextDown: Decimal](decimal/nextdown.md)
  The greatest representable value that is less than this decimal.
- [var nextUp: Decimal](decimal/nextup.md)
  The least representable value that is greater than this decimal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/isfinite)*