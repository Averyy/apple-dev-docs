# init(provider:busName:busNumber:tripDuration:departureBusStopLocation:departurePlatform:arrivalBusStopLocation:arrivalPlatform:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a bus trip with the specified contents and attributes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(provider: String?, busName: String?, busNumber: String?, tripDuration: INDateComponentsRange, departureBusStopLocation: CLPlacemark, departurePlatform: String?, arrivalBusStopLocation: CLPlacemark, arrivalPlatform: String?)
```

```objc
- (instancetype) initWithProvider:(NSString *) provider busName:(NSString *) busName busNumber:(NSString *) busNumber tripDuration:(INDateComponentsRange *) tripDuration departureBusStopLocation:(CLPlacemark *) departureBusStopLocation departurePlatform:(NSString *) departurePlatform arrivalBusStopLocation:(CLPlacemark *) arrivalBusStopLocation arrivalPlatform:(NSString *) arrivalPlatform;
```

## Return Value

A new [`INBusTrip`](../inbustrip.md) object or `nil` if the initializer can’t create one.

## Parameters

- `provider`: The operator of the bus line.
- `busName`: The name of the bus.
- `busNumber`: The bus number.
- `tripDuration`: The timespan of the bus trip from departure to arrival.
- `departureBusStopLocation`: The bus stop where the bus trip starts.
- `departurePlatform`: The platform from which the bus departs.
- `arrivalBusStopLocation`: The bus stop where the bus trip ends.
- `arrivalPlatform`: The platform at which the bus arrives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbustrip/init(provider:busname:busnumber:tripduration:departurebusstoplocation:departureplatform:arrivalbusstoplocation:arrivalplatform:))*