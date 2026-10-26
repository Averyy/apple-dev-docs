# url

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A webpage the user can access to view reservation details.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var url: URL? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSURL * URL;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSURL * URL;
```

#### Discussion

Provide a URL in your reservations so that the user can access reservation details from a device on which your app is unavailable.

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
- [var itemReference: INSpeakableString](./itemreference.md)
  A unique reference for the reservation.
- [var actions: [INReservationAction]?](./actions.md)
  An array containing actions the user can perform on the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inreservation/url)*