# updateEstimates(_:for:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Updates travel estimates, such as arrival time and the remaining time and distance for a trip.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func updateEstimates(_ estimates: CPTravelEstimates, for trip: CPTrip)
```

```objc
- (void) updateTravelEstimates:(CPTravelEstimates *) estimates forTrip:(CPTrip *) trip;
```

## Discussion

The updated trip uses the default time-remaining color. To change the color, use the [`update(_:for:with:)`](./update%28_,for,with%29.md) method instead of calling this method.

## Parameters

- `estimates`: The updated travel estimates.
- `trip`: A trip preview or the active trip.

## See Also

### Providing Trip Estimates
- [func update(CPTravelEstimates, for: CPTrip, with: CPTimeRemainingColor)](./update%28_,for,with%29.md)
  Updates travel estimates, such as arrival time and the remaining time and distance for a trip, with the specified time-remaining color.
- [enum CPTimeRemainingColor](../cptimeremainingcolor.md)
  The color the system uses when displaying the time remaining for a trip.
- [var tripEstimateStyle: CPTripEstimateStyle](./tripestimatestyle.md)
  The style that the map template uses when displaying trip estimates during active nagivation.
- [enum CPTripEstimateStyle](../cptripestimatestyle.md)
  The set of display styles for trip estimates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/updateestimates(_:for:))*