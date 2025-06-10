# updateEstimates(_:for:)

**Framework**: CarPlay  
**Kind**: method

Updates the travel estimates for the specified maneuver.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func updateEstimates(_ estimates: CPTravelEstimates, for maneuver: CPManeuver)
```

## Parameters

- `estimates`: The updated travel estimates.
- `maneuver`: The maneuver to update.

## See Also

- [class CPTravelEstimates](cptravelestimates.md)
  An object that describes the time and distance remaining for a maneuver in a navigation session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationsession/updateestimates(_:for:))*