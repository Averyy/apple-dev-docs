# rideStatus

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The current status of the ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var rideStatus: INRideStatus? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INRideStatus * rideStatus;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INRideStatus * rideStatus;
```

## Discussion

Siri uses the information in this object to communicate the ride status to the user. Always provide as much information as you can for the current ride. If the user does not have an active ride, set this property to `nil`.

The default value of this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetridestatusintentresponse/ridestatus)*