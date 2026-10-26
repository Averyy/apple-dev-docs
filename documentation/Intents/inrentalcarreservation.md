# INRentalCarReservation

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The information that describes a rental car reservation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INRentalCarReservation
```

```objc
@interface INRentalCarReservation : INReservation
```

## Topics

### Creating a Rental Car Reservation
- [init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, url: URL?, rentalCar: INRentalCar, rentalDuration: INDateComponentsRange, pickupLocation: CLPlacemark?, dropOffLocation: CLPlacemark?)](./inrentalcarreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,rentalcar,rentalduration,pickuplocation,dropofflocation%29-44w7o.md)
  Creates a rental car reservation with the specified contents and attributes.
- [convenience init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, rentalCar: INRentalCar, rentalDuration: INDateComponentsRange, pickupLocation: CLPlacemark?, dropOffLocation: CLPlacemark?)](./inrentalcarreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,rentalcar,rentalduration,pickuplocation,dropofflocation%29.md)
  Creates a new rental car reservation with the specified contents and attributes.
### Getting the Rental Car Reservation Information
- [var rentalCar: INRentalCar](./inrentalcarreservation/rentalcar.md)
  An object containing detailed information about the rental car.
- [class INRentalCar](./inrentalcar.md)
  The information that describes a rental car.
- [var rentalDuration: INDateComponentsRange](./inrentalcarreservation/rentalduration.md)
  The date and time range that indicates the pickup and drop off times for the rental.
- [var pickupLocation: CLPlacemark?](./inrentalcarreservation/pickuplocation.md)
  The name and location where the user can pick up the car.
- [var dropOffLocation: CLPlacemark?](./inrentalcarreservation/dropofflocation.md)
  The name and location where the user can drop off the car.
### Initializers
- [init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, URL: URL?, rentalCar: INRentalCar, rentalDuration: INDateComponentsRange, pickupLocation: CLPlacemark?, dropOffLocation: CLPlacemark?)](./inrentalcarreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,rentalcar,rentalduration,pickuplocation,dropofflocation%29-4zr96.md)

## Relationships

### Inherits From
- [INReservation](./inreservation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Travel Reservations
- [class INFlightReservation](./inflightreservation.md)
  The information that describes a flight reservation.
- [class INTrainReservation](./intrainreservation.md)
  The information that describes a train reservation.
- [class INBoatReservation](./inboatreservation.md)
  The information that describes a boat reservation.
- [class INBusReservation](./inbusreservation.md)
  The information that describes a bus reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrentalcarreservation)*