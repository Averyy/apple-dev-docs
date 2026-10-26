# driver

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The driver providing the ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var driver: INRideDriver? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INRideDriver * driver;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INRideDriver * driver;
```

#### Discussion

Use this property to specify information about the driver of the vehicle that is picking up the user. Siri displays the driver’s picture and telephone number to the user, who can use that identify and contact the driver.

The default value of this property is `nil`.

## See Also

### Accessing Ride Information
- [var vehicle: INRideVehicle?](./vehicle.md)
  The vehicle assigned to pick up the user.
- [var rideOption: INRideOption?](./rideoption.md)
  Information about the type of ride that you are offering to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridestatus/driver)*