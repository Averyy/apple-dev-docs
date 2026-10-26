# reservationHolderName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The reservation holder’s name.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var reservationHolderName: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * reservationHolderName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * reservationHolderName;
```

## See Also

### Describing the Reservation
- [var reservationNumber: String?](./reservationnumber.md)
  The reservation number.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inreservation/reservationholdername)*