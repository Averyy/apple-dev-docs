# rideOptionName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name of the ride option selected by the user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var rideOptionName: INSpeakableString? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INSpeakableString * rideOptionName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INSpeakableString * rideOptionName;
```

#### Discussion

If the user requested a specific type of ride, this property specifies the name of that ride. Map this string to the [`INRideOption`](../inrideoption.md) object that most closely represents your company’s available rides. You can then use the ride option information to select a vehicle to fulfill the ride request.

You can define the names of ride options using custom vocabulary terms. For information on how to configure ride option names in your global vocabulary file, see [Registering Custom Vocabulary with SiriKit](../../SiriKit/registering-custom-vocabulary-with-sirikit.md).

## See Also

### Getting the Ride Details
- [var partySize: Int?](./partysize-39k7z.md)
  The number of passengers that the ride must accommodate.
- [var pickupLocation: CLPlacemark?](./pickuplocation.md)
  The user’s starting location.
- [var scheduledPickupTime: INDateComponentsRange?](./scheduledpickuptime.md)
  The time at which to pick up the user.
- [var dropOffLocation: CLPlacemark?](./dropofflocation.md)
  The user’s destination.
- [partySize](./partysize-64kfc.md)
  The number of passengers that the ride must accommodate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestrideintent/rideoptionname)*