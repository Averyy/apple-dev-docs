# CMTimeRoundingMethod.roundTowardNegativeInfinity

**Framework**: Core Media  
**Kind**: case

Rounds toward negative infinity.

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
case roundTowardNegativeInfinity
```

#### Discussion

This method rounds toward [`negativeInfinity`](cmtime/negativeinfinity.md) if the fraction isn’t equal to `0`.

## See Also

- [CMTimeRoundingMethod.roundHalfAwayFromZero](cmtimeroundingmethod/roundhalfawayfromzero.md)
  Rounds half away from zero.
- [CMTimeRoundingMethod.roundAwayFromZero](cmtimeroundingmethod/roundawayfromzero.md)
  Rounds away from zero.
- [CMTimeRoundingMethod.roundTowardZero](cmtimeroundingmethod/roundtowardzero.md)
  Rounds toward zero.
- [CMTimeRoundingMethod.quickTime](cmtimeroundingmethod/quicktime.md)
  Rounds using the QuickTime method.
- [CMTimeRoundingMethod.roundTowardPositiveInfinity](cmtimeroundingmethod/roundtowardpositiveinfinity.md)
  Rounds toward positive infinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimeroundingmethod/roundtowardnegativeinfinity)*