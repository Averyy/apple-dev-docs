# init(itemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:reservationDuration:partySize:restaurantLocation:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a new restaurant reservation with the provided information.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- watchOS 6.0+

## Declaration

```swift
@nonobjc
convenience init(itemReference: INSpeakableString, reservationNumber: String? = nil, bookingTime: Date? = nil, reservationStatus: INReservationStatus = .unknown, reservationHolderName: String? = nil, actions: [INReservationAction]? = nil, reservationDuration: INDateComponentsRange, partySize: Int? = nil, restaurantLocation: CLPlacemark)
```

## Parameters

- `itemReference`: A unique value for the reservation item.
- `reservationNumber`: The reservation or booking number provided by the app.
- `bookingTime`: The date and time the user made the reservation.
- `reservationStatus`: The current status of the reservation.
- `reservationHolderName`: The reservation holder’s name.
- `actions`: The available actions for the reservation. For example, checking in for the reservation from your phone.
- `reservationDuration`: The date and time range that defines the start and end times for the restaurant reservation.
- `partySize`: The size of the party for the reservation.
- `restaurantLocation`: The name and location of the restaurant.

## See Also

### Creating a Restaurant Reservation
- [convenience init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, url: URL?, reservationDuration: INDateComponentsRange, partySize: Int?, restaurantLocation: CLPlacemark)](./init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,reservationduration,partysize,restaurantlocation%29.md)
  Creates a restaurant reservation with the specified contents and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservation/init(itemreference:reservationnumber:bookingtime:reservationstatus:reservationholdername:actions:reservationduration:partysize:restaurantlocation:))*