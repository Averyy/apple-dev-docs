# updateEstimates(_:for:)

**Framework**: CarPlay  
**Kind**: method

Updates travel estimates, such as arrival time and the remaining time and distance for a trip.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func updateEstimates(_ estimates: CPTravelEstimates, for trip: CPTrip)
```

#### Discussion

The updated trip uses the default time-remaining color. To change the color, use the [`update(_:for:with:)`](cpmaptemplate/update(_:for:with:).md) method instead of calling this method.

## Parameters

- `estimates`: The updated travel estimates.
- `trip`: A trip preview or the active trip.

## See Also

- [func update(CPTravelEstimates, for: CPTrip, with: CPTimeRemainingColor)](cpmaptemplate/update(_:for:with:).md)
  Updates travel estimates, such as arrival time and the remaining time and distance for a trip, with the specified time-remaining color.
- [enum CPTimeRemainingColor](cptimeremainingcolor.md)
  The color the system uses when displaying the time remaining for a trip.
- [var tripEstimateStyle: CPTripEstimateStyle](cpmaptemplate/tripestimatestyle.md)
  The style that the map template uses when displaying trip estimates during active nagivation.
- [enum CPTripEstimateStyle](cptripestimatestyle.md)
  The set of display styles for trip estimates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/updateestimates(_:for:))*