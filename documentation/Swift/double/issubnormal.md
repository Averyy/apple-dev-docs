# isSubnormal

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether the instance is subnormal.

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
var isSubnormal: Bool { get }
```

#### Discussion

A  value is a nonzero number that has a lesser magnitude than the smallest normal number. Subnormal values don’t use the full precision available to values of a type.

Zero is neither a normal nor a subnormal number. Subnormal numbers are often called  or —these are different names for the same concept.

## See Also

- [var isZero: Bool](double/iszero.md)
  A Boolean value indicating whether the instance is equal to zero.
- [var isFinite: Bool](double/isfinite.md)
  A Boolean value indicating whether this instance is finite.
- [var isInfinite: Bool](double/isinfinite.md)
  A Boolean value indicating whether the instance is infinite.
- [var isNaN: Bool](double/isnan.md)
  A Boolean value indicating whether the instance is NaN (“not a number”).
- [var isSignalingNaN: Bool](double/issignalingnan.md)
  A Boolean value indicating whether the instance is a signaling NaN.
- [var isNormal: Bool](double/isnormal.md)
  A Boolean value indicating whether this instance is normal.
- [var isCanonical: Bool](double/iscanonical.md)
  A Boolean value indicating whether the instance’s representation is in its canonical form.
- [var floatingPointClass: FloatingPointClassification](double/floatingpointclass.md)
  The classification of this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/issubnormal)*