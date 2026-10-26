# partySize

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The number of passengers that the ride must accommodate.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * partySize;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * partySize;
```

#### Discussion

The party size includes the total number of passengers.

## See Also

### Getting the Ride Details
- [var rideOptionName: INSpeakableString?](./rideoptionname.md)
  The name of the ride option selected by the user.
- [var pickupLocation: CLPlacemark?](./pickuplocation.md)
  The user’s starting location.
- [var scheduledPickupTime: INDateComponentsRange?](./scheduledpickuptime.md)
  The time at which to pick up the user.
- [var dropOffLocation: CLPlacemark?](./dropofflocation.md)
  The user’s destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestrideintent/partysize-64kfc)*