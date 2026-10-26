# INBoatTrip

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The information that describes a boat trip.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class INBoatTrip
```

```objc
@interface INBoatTrip : NSObject
```

## Topics

### Creating a Boat Trip
- [init(provider: String?, boatName: String?, boatNumber: String?, tripDuration: INDateComponentsRange, departureBoatTerminalLocation: CLPlacemark, arrivalBoatTerminalLocation: CLPlacemark)](./inboattrip/init%28provider,boatname,boatnumber,tripduration,departureboatterminallocation,arrivalboatterminallocation%29.md)
  Creates a boat trip with the specified contents and attributes.
### Getting the Boat Trip Information
- [var provider: String?](./inboattrip/provider.md)
  The operator of the boat line.
- [var boatName: String?](./inboattrip/boatname.md)
  The name of the boat.
- [var boatNumber: String?](./inboattrip/boatnumber.md)
  The number associated with the boat.
- [var tripDuration: INDateComponentsRange](./inboattrip/tripduration.md)
  The timespan of the boat trip from departure to arrival.
- [var departureBoatTerminalLocation: CLPlacemark](./inboattrip/departureboatterminallocation.md)
  The place where the boat trip starts.
- [var arrivalBoatTerminalLocation: CLPlacemark](./inboattrip/arrivalboatterminallocation.md)
  The place where the boat trip ends.
### Initializers
- [init?(coder: NSCoder)](./inboattrip/init%28coder%29.md)

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

### Getting the Boat Reservation Information
- [var boatTrip: INBoatTrip?](./inboatreservation/boattrip.md)
  Information describing a voyage.
- [var reservedSeat: INSeat?](./inboatreservation/reservedseat.md)
  The passenger’s seat on a boat reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inboattrip)*