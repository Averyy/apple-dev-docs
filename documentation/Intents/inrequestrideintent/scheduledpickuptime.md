# scheduledPickupTime

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The time at which to pick up the user.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var scheduledPickupTime: INDateComponentsRange? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INDateComponentsRange * scheduledPickupTime;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INDateComponentsRange * scheduledPickupTime;
```

#### Discussion

Use this property to schedule a vehicle to arrive at the specified time at the user’s location. Your handler for the [`INGetRideStatusIntent`](../ingetridestatusintent.md) object should also pick the most appropriate ride for the scheduled time.

## See Also

### Getting the Ride Details
- [var rideOptionName: INSpeakableString?](./rideoptionname.md)
  The name of the ride option selected by the user.
- [var partySize: Int?](./partysize-39k7z.md)
  The number of passengers that the ride must accommodate.
- [var pickupLocation: CLPlacemark?](./pickuplocation.md)
  The user’s starting location.
- [var dropOffLocation: CLPlacemark?](./dropofflocation.md)
  The user’s destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestrideintent/scheduledpickuptime)*