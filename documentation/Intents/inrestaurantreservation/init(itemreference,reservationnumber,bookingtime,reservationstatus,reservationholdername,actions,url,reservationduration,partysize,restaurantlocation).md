# init(itemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:url:reservationDuration:partySize:restaurantLocation:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a restaurant reservation with the specified contents and attributes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.0+

## Declaration

```swift
@nonobjc
convenience init(itemReference: INSpeakableString, reservationNumber: String? = nil, bookingTime: Date? = nil, reservationStatus: INReservationStatus = .unknown, reservationHolderName: String? = nil, actions: [INReservationAction]? = nil, url: URL? = nil, reservationDuration: INDateComponentsRange, partySize: Int? = nil, restaurantLocation: CLPlacemark)
```

## Parameters

- `itemReference`: A unique identifier for the reservation.
- `reservationNumber`: The reservation number.
- `bookingTime`: The date and time the user made the reservation.
- `reservationStatus`: The current status of the reservation.
- `reservationHolderName`: The reservation holder’s name.
- `actions`: Available actions associated with the reservation, such as checking in when the user arrives at the restaurant.
- `url`: A webpage containing reservation information.
- `reservationDuration`: The date and time range that defines the start and end times for the restaurant reservation.
- `partySize`: The size of the party for the reservation.
- `restaurantLocation`: The name and location of the restaurant.

## See Also

### Creating a Restaurant Reservation
- [convenience init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, reservationDuration: INDateComponentsRange, partySize: Int?, restaurantLocation: CLPlacemark)](./init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,reservationduration,partysize,restaurantlocation%29.md)
  Creates a new restaurant reservation with the provided information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservation/init(itemreference:reservationnumber:bookingtime:reservationstatus:reservationholdername:actions:url:reservationduration:partysize:restaurantlocation:))*