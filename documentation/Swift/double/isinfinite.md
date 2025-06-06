# isInfinite

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether the instance is infinite.

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
var isInfinite: Bool { get }
```

#### Discussion

For NaN, both `isFinite` and `isInfinite` are false.

## See Also

- [var isZero: Bool](double/iszero.md)
  A Boolean value indicating whether the instance is equal to zero.
- [var isFinite: Bool](double/isfinite.md)
  A Boolean value indicating whether this instance is finite.
- [var isNaN: Bool](double/isnan.md)
  A Boolean value indicating whether the instance is NaN (“not a number”).
- [var isSignalingNaN: Bool](double/issignalingnan.md)
  A Boolean value indicating whether the instance is a signaling NaN.
- [var isNormal: Bool](double/isnormal.md)
  A Boolean value indicating whether this instance is normal.
- [var isSubnormal: Bool](double/issubnormal.md)
  A Boolean value indicating whether the instance is subnormal.
- [var isCanonical: Bool](double/iscanonical.md)
  A Boolean value indicating whether the instance’s representation is in its canonical form.
- [var floatingPointClass: FloatingPointClassification](double/floatingpointclass.md)
  The classification of this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/isinfinite)*