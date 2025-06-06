# CPTripEstimateStyle

**Framework**: CarPlay  
**Kind**: enum

The set of display styles for trip estimates.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum CPTripEstimateStyle
```

## Topics

### Styles
- [CPTripEstimateStyle.light](cptripestimatestyle/light.md)
  The light trip estimate display style.
- [CPTripEstimateStyle.dark](cptripestimatestyle/dark.md)
  The dark trip estimate display style.
### Initializers
- [init?(rawValue: UInt)](cptripestimatestyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func updateEstimates(CPTravelEstimates, for: CPTrip)](cpmaptemplate/updateestimates(_:for:).md)
  Updates travel estimates, such as arrival time and the remaining time and distance for a trip.
- [func update(CPTravelEstimates, for: CPTrip, with: CPTimeRemainingColor)](cpmaptemplate/update(_:for:with:).md)
  Updates travel estimates, such as arrival time and the remaining time and distance for a trip, with the specified time-remaining color.
- [enum CPTimeRemainingColor](cptimeremainingcolor.md)
  The color the system uses when displaying the time remaining for a trip.
- [var tripEstimateStyle: CPTripEstimateStyle](cpmaptemplate/tripestimatestyle.md)
  The style that the map template uses when displaying trip estimates during active nagivation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptripestimatestyle)*