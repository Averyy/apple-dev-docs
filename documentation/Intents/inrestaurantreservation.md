# INRestaurantReservation

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The information that describes a restaurant reservation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INRestaurantReservation
```

```objc
@interface INRestaurantReservation : INReservation
```

## Topics

### Creating a Restaurant Reservation
- [convenience init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, url: URL?, reservationDuration: INDateComponentsRange, partySize: Int?, restaurantLocation: CLPlacemark)](./inrestaurantreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,reservationduration,partysize,restaurantlocation%29.md)
  Creates a restaurant reservation with the specified contents and attributes.
- [convenience init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, reservationDuration: INDateComponentsRange, partySize: Int?, restaurantLocation: CLPlacemark)](./inrestaurantreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,reservationduration,partysize,restaurantlocation%29.md)
  Creates a new restaurant reservation with the provided information.
### Getting the Restaurant Reservation Information
- [var reservationDuration: INDateComponentsRange](./inrestaurantreservation/reservationduration.md)
  The date and time range that defines beginning and end of the restaurant reservation.
- [var restaurantLocation: CLPlacemark](./inrestaurantreservation/restaurantlocation.md)
  The name and location of the restaurant.
- [var partySize: Int?](./inrestaurantreservation/partysize-9ux0p.md)
  The number of people in the party.

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

### Food, Lodging, and Event Reservations
- [class INLodgingReservation](./inlodgingreservation.md)
  The information that describes a lodging reservation.
- [class INTicketedEventReservation](./inticketedeventreservation.md)
  The information that describes a ticketed event reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantreservation)*