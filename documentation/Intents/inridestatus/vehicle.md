# vehicle

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The vehicle assigned to pick up the user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var vehicle: INRideVehicle? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INRideVehicle * vehicle;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INRideVehicle * vehicle;
```

## Discussion

Use this property to specify information about the vehicle assigned to pick up the user. Siri and Maps display vehicle information to the user so that the user can identify the vehicle when it arrives.

The default value of this property is `nil`.

## See Also

### Accessing Ride Information
- [var driver: INRideDriver?](./driver.md)
  The driver providing the ride.
- [var rideOption: INRideOption?](./rideoption.md)
  Information about the type of ride that you are offering to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridestatus/vehicle)*