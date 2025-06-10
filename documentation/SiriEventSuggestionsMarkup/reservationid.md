# reservationId

**Framework**: Siri Event Suggestions Markup  
**Kind**: typealias

A stable, unique identifier for the reservation.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```swift
string reservationId
```

## Mentions

- [Checking Your Reservation Markup](checking-your-reservation-markup.md)

#### Discussion

Use a consistent, unique identifier for each reservation. If you also provide reservation information with doc://com.apple.documentation/documentation/sirikit/siri_event_suggestions in your app, use a single, consistent value for that [`reservationNumber`](https://developer.apple.com/documentation/Intents/INReservation/reservationNumber) and this `reservationId`.

## See Also

- [type @context](@context.md)
  The open standard reference for interpreting the markup contents.
- [type dateTimeISO8601](datetimeiso8601.md)
  A time and date in the ISO-8601 format.
- [type reservationStatus](reservationstatus.md)
  A string indicating that the reservation has been confirmed or canceled.
- [type URL](url.md)
  The address of a webpage.
- [type telephone](telephone.md)
  A phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/reservationid)*