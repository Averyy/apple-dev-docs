# init(provider:boatName:boatNumber:tripDuration:departureBoatTerminalLocation:arrivalBoatTerminalLocation:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a boat trip with the specified contents and attributes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(provider: String?, boatName: String?, boatNumber: String?, tripDuration: INDateComponentsRange, departureBoatTerminalLocation: CLPlacemark, arrivalBoatTerminalLocation: CLPlacemark)
```

```objc
- (instancetype) initWithProvider:(NSString *) provider boatName:(NSString *) boatName boatNumber:(NSString *) boatNumber tripDuration:(INDateComponentsRange *) tripDuration departureBoatTerminalLocation:(CLPlacemark *) departureBoatTerminalLocation arrivalBoatTerminalLocation:(CLPlacemark *) arrivalBoatTerminalLocation;
```

## Return Value

A new [`INBoatTrip`](../inboattrip.md) object or `nil` if the initializer can’t create one.

## Parameters

- `provider`: The operator of the boat line.
- `boatName`: The name of the boat.
- `boatNumber`: The boat’s number.
- `tripDuration`: The timespan of the boat trip from departure to arrival.
- `departureBoatTerminalLocation`: The terminal where the boat trip starts.
- `arrivalBoatTerminalLocation`: The terminal where the boat trip ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inboattrip/init(provider:boatname:boatnumber:tripduration:departureboatterminallocation:arrivalboatterminallocation:))*