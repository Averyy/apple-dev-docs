# INRidePhase.unknown

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The state of the ride is unknown.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case unknown
```

```c
INRidePhaseUnknown
```

## Mentions

- [Providing Live Status Updates](../../SiriKit/providing-live-status-updates.md)

## Discussion

You may specify this state during the confirmation phase of a ride-booking request. Don’t specify this value during the handling of a request, where it is as an error.

## See Also

### Constants
- [INRidePhase.received](./received.md)
  You have received the booking request and are processing it, but have not yet confirmed the request or communicated the pickup information to the driver of the vehicle.
- [INRidePhase.confirmed](./confirmed.md)
  You have booked the ride and communicated the pickup information to the driver of the vehicle.
- [INRidePhase.ongoing](./ongoing.md)
  The driver has picked up the user’s party and is en route to the destination.
- [INRidePhase.completed](./completed.md)
  The driver has transited through all of the waypoints and is now at the ride’s destination.
- [INRidePhase.approachingPickup](./approachingpickup.md)
  The driver is approaching the pickup location.
- [INRidePhase.pickup](./pickup.md)
  The driver is at the pickup location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridephase/unknown)*