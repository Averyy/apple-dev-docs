# FloatingPointClassification

**Framework**: Swift  
**Kind**: enum

The IEEE 754 floating-point classes.

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
@frozen
enum FloatingPointClassification
```

## Topics

### Operators
- [static func == (FloatingPointClassification, FloatingPointClassification) -> Bool](floatingpointclassification/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [FloatingPointClassification.negativeInfinity](floatingpointclassification/negativeinfinity.md)
  A value equal to `-infinity`.
- [FloatingPointClassification.negativeNormal](floatingpointclassification/negativenormal.md)
  A negative value that uses the full precision of the floating-point type.
- [FloatingPointClassification.negativeSubnormal](floatingpointclassification/negativesubnormal.md)
  A negative, nonzero number that does not use the full precision of the floating-point type.
- [FloatingPointClassification.negativeZero](floatingpointclassification/negativezero.md)
  A value equal to zero with a negative sign.
- [FloatingPointClassification.positiveInfinity](floatingpointclassification/positiveinfinity.md)
  A value equal to `+infinity`.
- [FloatingPointClassification.positiveNormal](floatingpointclassification/positivenormal.md)
  A positive value that uses the full precision of the floating-point type.
- [FloatingPointClassification.positiveSubnormal](floatingpointclassification/positivesubnormal.md)
  A positive, nonzero number that does not use the full precision of the floating-point type.
- [FloatingPointClassification.positiveZero](floatingpointclassification/positivezero.md)
  A value equal to zero with a positive sign.
- [FloatingPointClassification.quietNaN](floatingpointclassification/quietnan.md)
  A silent NaN (“not a number”) value.
- [FloatingPointClassification.signalingNaN](floatingpointclassification/signalingnan.md)
  A signaling NaN (“not a number”).
### Instance Properties
- [var hashValue: Int](floatingpointclassification/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](floatingpointclassification/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](floatingpointclassification/equatable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)

## See Also

- [enum FloatingPointRoundingRule](floatingpointroundingrule.md)
  A rule for rounding a floating-point number.
- [enum FloatingPointSign](floatingpointsign.md)
  The sign of a floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floatingpointclassification)*