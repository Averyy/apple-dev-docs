# bookingTime

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The date and time the user booked the reservation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var bookingTime: Date? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSDate * bookingTime;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSDate * bookingTime;
```

## See Also

### Describing the Reservation
- [var reservationHolderName: String?](./reservationholdername.md)
  The reservation holder’s name.
- [var reservationNumber: String?](./reservationnumber.md)
  The reservation number.
- [var reservationStatus: INReservationStatus](./reservationstatus.md)
  The current status of the reservation.
- [var itemReference: INSpeakableString](./itemreference.md)
  A unique reference for the reservation.
- [var actions: [INReservationAction]?](./actions.md)
  An array containing actions the user can perform on the reservation.
- [var url: URL?](./url.md)
  A webpage the user can access to view reservation details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inreservation/bookingtime)*