# INRidePhase

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the current ride status.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INRidePhase
```

```c
enum INRidePhase : NSInteger;
```

## Topics

### Constants
- [INRidePhase.unknown](./inridephase/unknown.md)
  The state of the ride is unknown.
- [INRidePhase.received](./inridephase/received.md)
  You have received the booking request and are processing it, but have not yet confirmed the request or communicated the pickup information to the driver of the vehicle.
- [INRidePhase.confirmed](./inridephase/confirmed.md)
  You have booked the ride and communicated the pickup information to the driver of the vehicle.
- [INRidePhase.ongoing](./inridephase/ongoing.md)
  The driver has picked up the user’s party and is en route to the destination.
- [INRidePhase.completed](./inridephase/completed.md)
  The driver has transited through all of the waypoints and is now at the ride’s destination.
- [INRidePhase.approachingPickup](./inridephase/approachingpickup.md)
  The driver is approaching the pickup location.
- [INRidePhase.pickup](./inridephase/pickup.md)
  The driver is at the pickup location.
### Initializers
- [init?(rawValue: Int)](./inridephase/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Specifying the Ride Status
- [var phase: INRidePhase](./inridestatus/phase.md)
  The current status of the ride.
- [var completionStatus: INRideCompletionStatus?](./inridestatus/completionstatus.md)
  Information about how the ride ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridephase)*