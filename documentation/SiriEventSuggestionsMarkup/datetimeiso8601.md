# dateTimeISO8601

**Framework**: Siri Event Suggestions Markup  
**Kind**: typealias

A time and date in the ISO-8601 format.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```swift
date-time dateTimeISO8601
```

#### Overview

Event start and end times must use the ISO-8601 format. Provide the most relevant time zone in each `dateTimeISO8601`. For example, a flight reservation from Indiana to California should provide the departure time in the local time zone at the airport in Indiana and the arrival time in California’s time zone.

## See Also

- [type @context](@context.md)
  The open standard reference for interpreting the markup contents.
- [type reservationId](reservationid.md)
  A stable, unique identifier for the reservation.
- [type reservationStatus](reservationstatus.md)
  A string indicating that the reservation has been confirmed or canceled.
- [type URL](url.md)
  The address of a webpage.
- [type telephone](telephone.md)
  A phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/datetimeiso8601)*