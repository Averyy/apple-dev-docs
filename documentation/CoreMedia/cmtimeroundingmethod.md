# CMTimeRoundingMethod

**Framework**: Core Media  
**Kind**: enum

An enumeration of rounding methods to use when performing time calculations.

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
enum CMTimeRoundingMethod
```

## Topics

### Default Rounding Method
- [static var `default`: CMTimeRoundingMethod](cmtimeroundingmethod/default.md)
  The default rounding method.
### Rounding Methods
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
- [CMTimeRoundingMethod.roundTowardNegativeInfinity](cmtimeroundingmethod/roundtowardnegativeinfinity.md)
  Rounds toward negative infinity.
### Initializers
- [init?(rawValue: UInt32)](cmtimeroundingmethod/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func CMTimeConvertScale(CMTime, timescale: Int32, method: CMTimeRoundingMethod) -> CMTime](cmtimeconvertscale(_:timescale:method:).md)
  Converts the source time to a new timescale using the specified rounding method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimeroundingmethod)*