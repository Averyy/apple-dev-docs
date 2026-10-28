# INRidePhase.confirmed

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You have booked the ride and communicated the pickup information to the driver of the vehicle.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case confirmed
```

```c
INRidePhaseConfirmed
```

## Discussion

The driver has confirmed receipt of the information and will pick up the user’s party at the estimated time.

## See Also

### Constants
- [INRidePhase.unknown](./unknown.md)
  The state of the ride is unknown.
- [INRidePhase.received](./received.md)
  You have received the booking request and are processing it, but have not yet confirmed the request or communicated the pickup information to the driver of the vehicle.
- [INRidePhase.ongoing](./ongoing.md)
  The driver has picked up the user’s party and is en route to the destination.
- [INRidePhase.completed](./completed.md)
  The driver has transited through all of the waypoints and is now at the ride’s destination.
- [INRidePhase.approachingPickup](./approachingpickup.md)
  The driver is approaching the pickup location.
- [INRidePhase.pickup](./pickup.md)
  The driver is at the pickup location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridephase/confirmed)*