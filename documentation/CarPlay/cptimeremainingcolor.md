# CPTimeRemainingColor

**Framework**: CarPlay  
**Kind**: enum

The color the system uses when displaying the time remaining for a trip.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum CPTimeRemainingColor
```

#### Overview

The system determines the shade of each color based on the [`tripEstimateStyle`](cpmaptemplate/tripestimatestyle.md) for the map template.

## Topics

### Colors
- [CPTimeRemainingColor.default](cptimeremainingcolor/default.md)
  The system default color.
- [CPTimeRemainingColor.green](cptimeremainingcolor/green.md)
  A shade of green.
- [CPTimeRemainingColor.orange](cptimeremainingcolor/orange.md)
  A shade of orange.
- [CPTimeRemainingColor.red](cptimeremainingcolor/red.md)
  A shade of red.
### Initializers
- [init?(rawValue: UInt)](cptimeremainingcolor/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func updateEstimates(CPTravelEstimates, for: CPTrip)](cpmaptemplate/updateestimates(_:for:).md)
  Updates travel estimates, such as arrival time and the remaining time and distance for a trip.
- [func update(CPTravelEstimates, for: CPTrip, with: CPTimeRemainingColor)](cpmaptemplate/update(_:for:with:).md)
  Updates travel estimates, such as arrival time and the remaining time and distance for a trip, with the specified time-remaining color.
- [var tripEstimateStyle: CPTripEstimateStyle](cpmaptemplate/tripestimatestyle.md)
  The style that the map template uses when displaying trip estimates during active nagivation.
- [enum CPTripEstimateStyle](cptripestimatestyle.md)
  The set of display styles for trip estimates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptimeremainingcolor)*