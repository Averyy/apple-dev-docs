# CMTimeRoundingMethod.roundTowardPositiveInfinity

**Framework**: Core Media  
**Kind**: case

Rounds toward positive infinity.

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
case roundTowardPositiveInfinity
```

#### Discussion

This method rounds toward [`positiveInfinity`](cmtime/positiveinfinity.md) if the fraction isn’t equal to `0`.

## See Also

- [CMTimeRoundingMethod.roundHalfAwayFromZero](cmtimeroundingmethod/roundhalfawayfromzero.md)
  Rounds half away from zero.
- [CMTimeRoundingMethod.roundAwayFromZero](cmtimeroundingmethod/roundawayfromzero.md)
  Rounds away from zero.
- [CMTimeRoundingMethod.roundTowardZero](cmtimeroundingmethod/roundtowardzero.md)
  Rounds toward zero.
- [CMTimeRoundingMethod.quickTime](cmtimeroundingmethod/quicktime.md)
  Rounds using the QuickTime method.
- [CMTimeRoundingMethod.roundTowardNegativeInfinity](cmtimeroundingmethod/roundtowardnegativeinfinity.md)
  Rounds toward negative infinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimeroundingmethod/roundtowardpositiveinfinity)*