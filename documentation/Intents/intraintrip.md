# INTrainTrip

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The information that describes a train trip.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INTrainTrip
```

```objc
@interface INTrainTrip : NSObject
```

## Topics

### Creating a Train Trip
- [init(provider: String?, trainName: String?, trainNumber: String?, tripDuration: INDateComponentsRange, departureStationLocation: CLPlacemark, departurePlatform: String?, arrivalStationLocation: CLPlacemark, arrivalPlatform: String?)](./intraintrip/init%28provider,trainname,trainnumber,tripduration,departurestationlocation,departureplatform,arrivalstationlocation,arrivalplatform%29.md)
  Creates a new train trip with the specified contents and attributes.
### Getting the Train Trip Information
- [var provider: String?](./intraintrip/provider.md)
  The name for the train company.
- [var trainName: String?](./intraintrip/trainname.md)
  The name of the train.
- [var trainNumber: String?](./intraintrip/trainnumber.md)
  The unique identifier for the train.
- [var tripDuration: INDateComponentsRange](./intraintrip/tripduration.md)
  The date and time range for the departure and arrival of the train.
- [var departureStationLocation: CLPlacemark](./intraintrip/departurestationlocation.md)
  The station from which the train departs.
- [var departurePlatform: String?](./intraintrip/departureplatform.md)
  The platform from which the train departs.
- [var arrivalStationLocation: CLPlacemark](./intraintrip/arrivalstationlocation.md)
  The station at which the train arrives.
- [var arrivalPlatform: String?](./intraintrip/arrivalplatform.md)
  The platform at which the train arrives.
### Initializers
- [init?(coder: NSCoder)](./intraintrip/init%28coder%29.md)

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

### Getting the Train Reservation Information
- [var reservedSeat: INSeat?](./intrainreservation/reservedseat.md)
  The seat reserved for the user.
- [var trainTrip: INTrainTrip](./intrainreservation/traintrip.md)
  An object containing the detailed information about the train trip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intraintrip)*