# tripEstimateStyle

**Framework**: CarPlay  
**Kind**: property

The style that the map template uses when displaying trip estimates during active nagivation.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var tripEstimateStyle: CPTripEstimateStyle { get set }
```

#### Discussion

The default value is [`CPTripEstimateStyle.dark`](cptripestimatestyle/dark.md).

## See Also

- [func updateEstimates(CPTravelEstimates, for: CPTrip)](cpmaptemplate/updateestimates(_:for:).md)
  Updates travel estimates, such as arrival time and the remaining time and distance for a trip.
- [func update(CPTravelEstimates, for: CPTrip, with: CPTimeRemainingColor)](cpmaptemplate/update(_:for:with:).md)
  Updates travel estimates, such as arrival time and the remaining time and distance for a trip, with the specified time-remaining color.
- [enum CPTimeRemainingColor](cptimeremainingcolor.md)
  The color the system uses when displaying the time remaining for a trip.
- [enum CPTripEstimateStyle](cptripestimatestyle.md)
  The set of display styles for trip estimates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/tripestimatestyle)*