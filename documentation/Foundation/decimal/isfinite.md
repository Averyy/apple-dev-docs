# isFinite

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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
- [var nextDown: Decimal](./nextdown.md)
  The greatest representable value that is less than this decimal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/decimal/isfinite)*