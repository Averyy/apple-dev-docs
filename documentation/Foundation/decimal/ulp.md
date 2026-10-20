# ulp

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The unit in the last place of the decimal.

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
var ulp: Decimal { get }
```

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
- [var isSubnormal: Bool](./issubnormal.md)
  A Boolean value indicating whether this decimal is subnormal.
- [var isZero: Bool](./iszero.md)
  A Boolean value indicating whether this value is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/ulp)*