# init(itemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:rentalCar:rentalDuration:pickupLocation:dropOffLocation:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a new rental car reservation with the specified contents and attributes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
convenience init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, rentalCar: INRentalCar, rentalDuration: INDateComponentsRange, pickupLocation: CLPlacemark?, dropOffLocation: CLPlacemark?)
```

```objc
- (instancetype) initWithItemReference:(INSpeakableString *) itemReference reservationNumber:(NSString *) reservationNumber bookingTime:(NSDate *) bookingTime reservationStatus:(INReservationStatus) reservationStatus reservationHolderName:(NSString *) reservationHolderName actions:(NSArray<INReservationAction *> *) actions rentalCar:(INRentalCar *) rentalCar rentalDuration:(INDateComponentsRange *) rentalDuration pickupLocation:(CLPlacemark *) pickupLocation dropOffLocation:(CLPlacemark *) dropOffLocation;
```

#### Return Value

A new [`INRentalCarReservation`](../inrentalcarreservation.md) object or `nil` if unable to create one.

## Parameters

- `itemReference`: A unique value for the reservation item.
- `reservationNumber`: The reservation or booking number provided by the app.
- `bookingTime`: The date and time the user made the reservation.
- `reservationStatus`: The current status of the reservation.
- `reservationHolderName`: The reservation holder’s name.
- `actions`: The available actions for the reservation. For example, checking in for the reservation from your phone.
- `rentalCar`: The rental car object that provides detailed information on the rental car.
- `rentalDuration`: The date and time range that determines the pickup and drop off times for the rental.
- `pickupLocation`: The name and location of the place where the user can pick up the car.
- `dropOffLocation`: The name and location of the place where the user can drop off the car.

## See Also

### Creating a Rental Car Reservation
- [init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, url: URL?, rentalCar: INRentalCar, rentalDuration: INDateComponentsRange, pickupLocation: CLPlacemark?, dropOffLocation: CLPlacemark?)](./init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,rentalcar,rentalduration,pickuplocation,dropofflocation%29-44w7o.md)
  Creates a rental car reservation with the specified contents and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrentalcarreservation/init(itemreference:reservationnumber:bookingtime:reservationstatus:reservationholdername:actions:rentalcar:rentalduration:pickuplocation:dropofflocation:))*