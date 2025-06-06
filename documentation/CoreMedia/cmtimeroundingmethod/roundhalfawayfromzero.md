# CMTimeRoundingMethod.roundHalfAwayFromZero

**Framework**: Core Media  
**Kind**: case

Rounds half away from zero.

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
case roundHalfAwayFromZero
```

#### Discussion

This method rounds toward zero if the absolute value is less than `0.5`, and away from `0` if it’s greater than or equal to `0.5`.

This is the default rounding method.

## See Also

- [CMTimeRoundingMethod.roundAwayFromZero](cmtimeroundingmethod/roundawayfromzero.md)
  Rounds away from zero.
- [CMTimeRoundingMethod.roundTowardZero](cmtimeroundingmethod/roundtowardzero.md)
  Rounds toward zero.
- [CMTimeRoundingMethod.quickTime](cmtimeroundingmethod/quicktime.md)
  Rounds using the QuickTime method.
- [CMTimeRoundingMethod.roundTowardPositiveInfinity](cmtimeroundingmethod/roundtowardpositiveinfinity.md)
  Rounds toward positive infinity.
- [CMTimeRoundingMethod.roundTowardNegativeInfinity](cmtimeroundingmethod/roundtowardnegativeinfinity.md)
  Rounds toward negative infinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimeroundingmethod/roundhalfawayfromzero)*