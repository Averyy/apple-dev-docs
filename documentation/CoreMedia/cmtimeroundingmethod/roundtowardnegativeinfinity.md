# CMTimeRoundingMethod.roundTowardNegativeInfinity

**Framework**: Core Media  
**Kind**: case  
**Role**: Case

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

```c
kCMTimeRoundingMethod_RoundTowardNegativeInfinity
```

## Discussion

This method rounds toward [`negativeInfinity`](../cmtime/negativeinfinity.md) if the fraction isn’t equal to `0`.

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
- [CMTimeRoundingMethod.roundTowardPositiveInfinity](./roundtowardpositiveinfinity.md)
  Rounds toward positive infinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimeroundingmethod/roundtowardnegativeinfinity)*