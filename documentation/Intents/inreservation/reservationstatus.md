# reservationStatus

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The current status of the reservation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var reservationStatus: INReservationStatus { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INReservationStatus reservationStatus;
```

*macOS*

```objc
@property (atomic, assign, readonly) INReservationStatus reservationStatus;
```

## See Also

### Describing the Reservation
- [var reservationHolderName: String?](./reservationholdername.md)
  The reservation holder’s name.
- [var reservationNumber: String?](./reservationnumber.md)
  The reservation number.
- [var bookingTime: Date?](./bookingtime.md)
  The date and time the user booked the reservation.
- [var itemReference: INSpeakableString](./itemreference.md)
  A unique reference for the reservation.
- [var actions: [INReservationAction]?](./actions.md)
  An array containing actions the user can perform on the reservation.
- [var url: URL?](./url.md)
  A webpage the user can access to view reservation details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inreservation/reservationstatus)*