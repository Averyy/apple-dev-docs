# init(restaurant:booking:partySize:bookingIdentifier:guest:status:dateStatusModified:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the reservation object with the specified information and status.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(restaurant: INRestaurant, booking bookingDate: Date, partySize: Int, bookingIdentifier: String, guest: INRestaurantGuest, status: INRestaurantReservationUserBookingStatus, dateStatusModified: Date)
```

```objc
- (instancetype) initWithRestaurant:(INRestaurant *) restaurant bookingDate:(NSDate *) bookingDate partySize:(NSUInteger) partySize bookingIdentifier:(NSString *) bookingIdentifier guest:(INRestaurantGuest *) guest status:(INRestaurantReservationUserBookingStatus) status dateStatusModified:(NSDate *) dateStatusModified;
```

#### Return Value

An initialized reservation object or `nil` if the object could not be created.

## Parameters

- `restaurant`: The restaurant at which the reservation was made.
- `bookingDate`: The date and time of the reservation.
- `partySize`: The number of guests in the party.
- `bookingIdentifier`: The unique identifier for the reservation in your system.
- `guest`: The guest whose name is associated with the reservation.
- `status`: A value indicating whether the reservation was confirmed, declined, or is still pending.
- `dateStatusModified`: The date when the reservation’s status last changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservationuserbooking/init(restaurant:booking:partysize:bookingidentifier:guest:status:datestatusmodified:))*