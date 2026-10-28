# CMTimeRoundingMethod.roundTowardPositiveInfinity

**Framework**: Core Media  
**Kind**: case  
**Role**: Case

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

```c
kCMTimeRoundingMethod_RoundTowardPositiveInfinity
```

## Discussion

This method rounds toward [`positiveInfinity`](../cmtime/positiveinfinity.md) if the fraction isn’t equal to `0`.

## See Also

### Rounding Methods
- [CMTimeRoundingMethod.roundHalfAwayFromZero](./roundhalfawayfromzero.md)
  Rounds half away from zero.
- [CMTimeRoundingMethod.roundAwayFromZero](./roundawayfromzero.md)
  Rounds away from zero.
- [CMTimeRoundingMethod.roundTowardZero](./roundtowardzero.md)
  Rounds toward zero.
- [CMTimeRoundingMethod.quickTime](./quicktime.md)
  Rounds using the QuickTime method.
- [CMTimeRoundingMethod.roundTowardNegativeInfinity](./roundtowardnegativeinfinity.md)
  Rounds toward negative infinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimeroundingmethod/roundtowardpositiveinfinity)*