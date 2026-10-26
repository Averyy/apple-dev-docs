# init(itemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:url:lodgingBusinessLocation:reservationDuration:numberOfAdults:numberOfChildren:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a lodging reservation with the specified contents and attributes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.0+

## Declaration

```swift
@nonobjc
convenience init(itemReference: INSpeakableString, reservationNumber: String? = nil, bookingTime: Date? = nil, reservationStatus: INReservationStatus = .unknown, reservationHolderName: String? = nil, actions: [INReservationAction]? = nil, url: URL? = nil, lodgingBusinessLocation: CLPlacemark, reservationDuration: INDateComponentsRange, numberOfAdults: Int? = nil, numberOfChildren: Int? = nil)
```

## Parameters

- `itemReference`: A unique identifier for the reservation.
- `reservationNumber`: The reservation number.
- `bookingTime`: The date and time the user made the reservation.
- `reservationStatus`: The current status of the reservation.
- `reservationHolderName`: The reservation holder’s name.
- `actions`: Available actions associated with the reservation.
- `url`: A webpage containing reservation information.
- `lodgingBusinessLocation`: The name and location of the lodging establishment.
- `reservationDuration`: The date and time range that defines the beginning and end of the reservation.
- `numberOfAdults`: The number of adults staying in the lodging.
- `numberOfChildren`: The number of children staying in the lodging.

## See Also

### Creating a Lodging Reservation
- [convenience init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, lodgingBusinessLocation: CLPlacemark, reservationDuration: INDateComponentsRange, numberOfAdults: Int?, numberOfChildren: Int?)](./init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,lodgingbusinesslocation,reservationduration,numberofadults,numberofchildren%29.md)
  Creates a new lodging reservation with the provided information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlodgingreservation/init(itemreference:reservationnumber:bookingtime:reservationstatus:reservationholdername:actions:url:lodgingbusinesslocation:reservationduration:numberofadults:numberofchildren:))*