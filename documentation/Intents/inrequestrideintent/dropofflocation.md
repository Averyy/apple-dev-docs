# dropOffLocation

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user’s destination.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var dropOffLocation: CLPlacemark? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) CLPlacemark * dropOffLocation;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) CLPlacemark * dropOffLocation;
```

## Discussion

When booking the ride, you can communicate this information to the driver.

## See Also

### Getting the Ride Details
- [var rideOptionName: INSpeakableString?](./rideoptionname.md)
  The name of the ride option selected by the user.
- [var partySize: Int?](./partysize-39k7z.md)
  The number of passengers that the ride must accommodate.
- [var pickupLocation: CLPlacemark?](./pickuplocation.md)
  The user’s starting location.
- [var scheduledPickupTime: INDateComponentsRange?](./scheduledpickuptime.md)
  The time at which to pick up the user.
- [partySize](./partysize-64kfc.md)
  The number of passengers that the ride must accommodate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestrideintent/dropofflocation)*