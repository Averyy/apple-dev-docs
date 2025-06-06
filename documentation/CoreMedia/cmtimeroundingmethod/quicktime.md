# CMTimeRoundingMethod.quickTime

**Framework**: Core Media  
**Kind**: case

Rounds using the QuickTime method.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case quickTime
```

#### Discussion

This method uses [`CMTimeRoundingMethod.roundTowardZero`](cmtimeroundingmethod/roundtowardzero.md) if converting from larger to smaller scale (more precision to less precision), but uses [`CMTimeRoundingMethod.roundAwayFromZero`](cmtimeroundingmethod/roundawayfromzero.md) if converting from smaller to larger scale (less precision to more precision).

This method never rounds a negative number down to `0`, but instead returns the smallest magnitude negative time (`-1 / newTimescale`).

## See Also

- [CMTimeRoundingMethod.roundHalfAwayFromZero](cmtimeroundingmethod/roundhalfawayfromzero.md)
  Rounds half away from zero.
- [CMTimeRoundingMethod.roundAwayFromZero](cmtimeroundingmethod/roundawayfromzero.md)
  Rounds away from zero.
- [CMTimeRoundingMethod.roundTowardZero](cmtimeroundingmethod/roundtowardzero.md)
  Rounds toward zero.
- [CMTimeRoundingMethod.roundTowardPositiveInfinity](cmtimeroundingmethod/roundtowardpositiveinfinity.md)
  Rounds toward positive infinity.
- [CMTimeRoundingMethod.roundTowardNegativeInfinity](cmtimeroundingmethod/roundtowardnegativeinfinity.md)
  Rounds toward negative infinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimeroundingmethod/quicktime)*