# INBusTrip

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Information describing a bus trip.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class INBusTrip
```

```objc
@interface INBusTrip : NSObject
```

## Topics

### Creating a Bus Trip
- [init(provider: String?, busName: String?, busNumber: String?, tripDuration: INDateComponentsRange, departureBusStopLocation: CLPlacemark, departurePlatform: String?, arrivalBusStopLocation: CLPlacemark, arrivalPlatform: String?)](./inbustrip/init%28provider,busname,busnumber,tripduration,departurebusstoplocation,departureplatform,arrivalbusstoplocation,arrivalplatform%29.md)
  Creates a bus trip with the specified contents and attributes.
### Getting the Bus Trip Information
- [var arrivalBusStopLocation: CLPlacemark](./inbustrip/arrivalbusstoplocation.md)
  The bus stop where the trip ends.
- [var arrivalPlatform: String?](./inbustrip/arrivalplatform.md)
  The platform at which the bus arrives.
- [var busName: String?](./inbustrip/busname.md)
  The name of the bus.
- [var busNumber: String?](./inbustrip/busnumber.md)
  The number of the bus or route.
- [var departureBusStopLocation: CLPlacemark](./inbustrip/departurebusstoplocation.md)
  The bus stop where the bus trip starts.
- [var departurePlatform: String?](./inbustrip/departureplatform.md)
  The platform from which the bus departs.
- [var provider: String?](./inbustrip/provider.md)
  The business or other entity operating the bus.
- [var tripDuration: INDateComponentsRange](./inbustrip/tripduration.md)
  The timespan of the bus trip from departure to arrival.
### Initializers
- [init?(coder: NSCoder)](./inbustrip/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

### Getting the Bus Trip Reservation Information
- [var busTrip: INBusTrip](./inbusreservation/bustrip.md)
  Information describing a bus trip.
- [var reservedSeat: INSeat?](./inbusreservation/reservedseat.md)
  Seat information for the bus reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbustrip)*