# init(itemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:lodgingBusinessLocation:reservationDuration:numberOfAdults:numberOfChildren:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a new lodging reservation with the provided information.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- watchOS 6.0+

## Declaration

```swift
@nonobjc
convenience init(itemReference: INSpeakableString, reservationNumber: String? = nil, bookingTime: Date? = nil, reservationStatus: INReservationStatus = .unknown, reservationHolderName: String? = nil, actions: [INReservationAction]? = nil, lodgingBusinessLocation: CLPlacemark, reservationDuration: INDateComponentsRange, numberOfAdults: Int? = nil, numberOfChildren: Int? = nil)
```

## Parameters

- `itemReference`: A unique value for the reservation item.
- `reservationNumber`: The reservation or booking number provided by the app.
- `bookingTime`: The date and time the user made the reservation.
- `reservationStatus`: The current status of the reservation.
- `reservationHolderName`: The name of the person the reservation is under.
- `actions`: The available actions for the reservation. For example, checking in for the reservation from your phone.
- `lodgingBusinessLocation`: The name and location of the lodging establishment.
- `reservationDuration`: The date and time range that indicates the start and end times for the reservation.
- `numberOfAdults`: The number of adults staying in the lodging.
- `numberOfChildren`: The number of children staying in the lodging.

## See Also

### Creating a Lodging Reservation
- [convenience init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, url: URL?, lodgingBusinessLocation: CLPlacemark, reservationDuration: INDateComponentsRange, numberOfAdults: Int?, numberOfChildren: Int?)](./init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,lodgingbusinesslocation,reservationduration,numberofadults,numberofchildren%29.md)
  Creates a lodging reservation with the specified contents and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlodgingreservation/init(itemreference:reservationnumber:bookingtime:reservationstatus:reservationholdername:actions:lodgingbusinesslocation:reservationduration:numberofadults:numberofchildren:))*