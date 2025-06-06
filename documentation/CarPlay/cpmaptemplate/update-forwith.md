# update(_:for:with:)

**Framework**: CarPlay  
**Kind**: method

Updates travel estimates, such as arrival time and the remaining time and distance for a trip, with the specified time-remaining color.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func update(_ estimates: CPTravelEstimates, for trip: CPTrip, with timeRemainingColor: CPTimeRemainingColor)
```

## Parameters

- `estimates`: The updated travel estimates.
- `trip`: A trip preview or the active trip.
- `timeRemainingColor`: The time-remaining color.

## See Also

- [func updateEstimates(CPTravelEstimates, for: CPTrip)](cpmaptemplate/updateestimates(_:for:).md)
  Updates travel estimates, such as arrival time and the remaining time and distance for a trip.
- [enum CPTimeRemainingColor](cptimeremainingcolor.md)
  The color the system uses when displaying the time remaining for a trip.
- [var tripEstimateStyle: CPTripEstimateStyle](cpmaptemplate/tripestimatestyle.md)
  The style that the map template uses when displaying trip estimates during active nagivation.
- [enum CPTripEstimateStyle](cptripestimatestyle.md)
  The set of display styles for trip estimates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/update(_:for:with:))*