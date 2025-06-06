# isFinite

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether this instance is finite.

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
var isFinite: Bool { get }
```

#### Discussion

All values other than NaN and infinity are considered finite, whether normal or subnormal.  For NaN, both `isFinite` and `isInfinite` are false.

## See Also

- [var isZero: Bool](float/iszero.md)
  A Boolean value indicating whether the instance is equal to zero.
- [var isInfinite: Bool](float/isinfinite.md)
  A Boolean value indicating whether the instance is infinite.
- [var isNaN: Bool](float/isnan.md)
  A Boolean value indicating whether the instance is NaN (“not a number”).
- [var isSignalingNaN: Bool](float/issignalingnan.md)
  A Boolean value indicating whether the instance is a signaling NaN.
- [var isNormal: Bool](float/isnormal.md)
  A Boolean value indicating whether this instance is normal.
- [var isSubnormal: Bool](float/issubnormal.md)
  A Boolean value indicating whether the instance is subnormal.
- [var isCanonical: Bool](float/iscanonical.md)
  A Boolean value indicating whether the instance’s representation is in its canonical form.
- [var floatingPointClass: FloatingPointClassification](float/floatingpointclass.md)
  The classification of this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/isfinite)*