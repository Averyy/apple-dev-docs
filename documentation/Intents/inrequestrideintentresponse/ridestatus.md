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

You must assign a value to this property for any newly booked rides. The contents of this object convey important information to the user about the status and details of the ride. Siri and Maps display much of this information to the user. If you were unable to book the ride, you may leave this property set to `nil`.

The default value of this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestrideintentresponse/ridestatus)*