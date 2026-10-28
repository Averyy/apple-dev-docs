# reservationNumber

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The reservation number.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var reservationNumber: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * reservationNumber;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * reservationNumber;
```

## Discussion

Provide your system’s reference number for the reservation. Use a consistent, unique identifier for each reservation. If you also provide reservation information with [Siri Event Suggestions Markup](../../SiriEventSuggestionsMarkup/SiriEventSuggestionsMarkup.md) on your website or in emails, use the same value for the [`reservationId`](../../SiriEventSuggestionsMarkup/reservationid.md) in the reservation markup.

For a multipart booking, such as round-trip travel, you may provide the same `reservationNumber` for each reservation.

## See Also

### Describing the Reservation
- [var reservationHolderName: String?](./reservationholdername.md)
  The reservation holder’s name.
- [var reservationStatus: INReservationStatus](./reservationstatus.md)
  The current status of the reservation.
- [var bookingTime: Date?](./bookingtime.md)
  The date and time the user booked the reservation.
- [var itemReference: INSpeakableString](./itemreference.md)
  A unique reference for the reservation.
- [var actions: [INReservationAction]?](./actions.md)
  An array containing actions the user can perform on the reservation.
- [var url: URL?](./url.md)
  A webpage the user can access to view reservation details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inreservation/reservationnumber)*