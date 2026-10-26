# rideOption

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

Information about the type of ride that you are offering to the user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var rideOption: INRideOption? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INRideOption * rideOption;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INRideOption * rideOption;
```

## Mentions

- [Providing Live Status Updates](../../SiriKit/providing-live-status-updates.md)

#### Discussion

Use this property to identify the type of ride that the user selected. An [`INRideOption`](../inrideoption.md) object contains pricing information, disclaimers, and information about the number of people that the ride can accommodate. Siri and Maps display this information to the user as needed.

The default value of this property is `nil`.

## See Also

### Accessing Ride Information
- [var vehicle: INRideVehicle?](./vehicle.md)
  The vehicle assigned to pick up the user.
- [var driver: INRideDriver?](./driver.md)
  The driver providing the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridestatus/rideoption)*