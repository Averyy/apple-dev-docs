# INLodgingReservation

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The information that describes a lodging reservation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INLodgingReservation
```

```objc
@interface INLodgingReservation : INReservation
```

## Topics

### Creating a Lodging Reservation
- [convenience init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, url: URL?, lodgingBusinessLocation: CLPlacemark, reservationDuration: INDateComponentsRange, numberOfAdults: Int?, numberOfChildren: Int?)](./inlodgingreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,url,lodgingbusinesslocation,reservationduration,numberofadults,numberofchildren%29.md)
  Creates a lodging reservation with the specified contents and attributes.
- [convenience init(itemReference: INSpeakableString, reservationNumber: String?, bookingTime: Date?, reservationStatus: INReservationStatus, reservationHolderName: String?, actions: [INReservationAction]?, lodgingBusinessLocation: CLPlacemark, reservationDuration: INDateComponentsRange, numberOfAdults: Int?, numberOfChildren: Int?)](./inlodgingreservation/init%28itemreference,reservationnumber,bookingtime,reservationstatus,reservationholdername,actions,lodgingbusinesslocation,reservationduration,numberofadults,numberofchildren%29.md)
  Creates a new lodging reservation with the provided information.
- [- initWithItemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:URL:lodgingBusinessLocation:reservationDuration:numberOfAdults:numberOfChildren:](./inlodgingreservation/initwithitemreference_reservationnumber_bookingtime_reservationstatus_reservationholdername_actions_url_lodgingbusinesslocation_reservationduration_numberofadults_numberofchildren_.md)
  Creates a lodging reservation with the specified contents and attributes.
- [- initWithItemReference:reservationNumber:bookingTime:reservationStatus:reservationHolderName:actions:lodgingBusinessLocation:reservationDuration:numberOfAdults:numberOfChildren:](./inlodgingreservation/initwithitemreference_reservationnumber_bookingtime_reservationstatus_reservationholdername_actions_lodgingbusinesslocation_reservationduration_numberofadults_numberofchildren_.md)
  Creates a new lodging reservation with the provided information.
### Getting the Lodging Reservation Information
- [var lodgingBusinessLocation: CLPlacemark](./inlodgingreservation/lodgingbusinesslocation.md)
  The name and location of the lodging establishment.
- [var reservationDuration: INDateComponentsRange](./inlodgingreservation/reservationduration.md)
  The date and time range that indicates the beginning and end of the reservation.
- [var numberOfAdults: Int?](./inlodgingreservation/numberofadults-6fsnq.md)
  The number of adults staying at the lodging location.
- [var numberOfChildren: Int?](./inlodgingreservation/numberofchildren-1dm3g.md)
  The number of children staying at the lodging location.
- [numberOfAdults](./inlodgingreservation/numberofadults-9r4iw.md)
  The number of adults staying at the lodging location.
- [numberOfChildren](./inlodgingreservation/numberofchildren-2n3e2.md)
  The number of children staying at the lodging location.

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
- [class INRestaurantReservation](./inrestaurantreservation.md)
  The information that describes a restaurant reservation.
- [class INTicketedEventReservation](./inticketedeventreservation.md)
  The information that describes a ticketed event reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlodgingreservation)*