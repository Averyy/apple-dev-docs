# itemReference

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A unique reference for the reservation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var itemReference: INSpeakableString { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) INSpeakableString * itemReference;
```

*macOS*

```objc
@property (atomic, copy, readonly) INSpeakableString * itemReference;
```

#### Discussion

Provide information that identifies this specific reservation. The [`vocabularyIdentifier`](../inspeakable/vocabularyidentifier.md) should be specific enough that your app can use it to retrieve and display this reservation’s info later. The [`spokenPhrase`](../inspeakable/spokenphrase.md) should describe the event to the user. For example, a restaurant reservation might use a phrase like `“Table for 2 at McNeil’s on February 11”` or `“7pm at McNeil’s”`. For a multi-part reservation, such as a round-trip ticket, provide an `itemReference` that is specific to this portion of the overall reservation.

## See Also

### Describing the Reservation
- [var reservationHolderName: String?](./reservationholdername.md)
  The reservation holder’s name.
- [var reservationNumber: String?](./reservationnumber.md)
  The reservation number.
- [var reservationStatus: INReservationStatus](./reservationstatus.md)
  The current status of the reservation.
- [var bookingTime: Date?](./bookingtime.md)
  The date and time the user booked the reservation.
- [var actions: [INReservationAction]?](./actions.md)
  An array containing actions the user can perform on the reservation.
- [var url: URL?](./url.md)
  A webpage the user can access to view reservation details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inreservation/itemreference)*