# floatingPointClass

**Framework**: Swift  
**Kind**: property

The classification of this value.

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
var floatingPointClass: FloatingPointClassification { get }
```

#### Discussion

A value’s `floatingPointClass` property describes its “class” as described by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## See Also

- [var isZero: Bool](float/iszero.md)
  A Boolean value indicating whether the instance is equal to zero.
- [var isFinite: Bool](float/isfinite.md)
  A Boolean value indicating whether this instance is finite.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/floatingpointclass)*