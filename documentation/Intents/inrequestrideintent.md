# INRequestRideIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to book the specified ride from your service.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INRequestRideIntent
```

```objc
@interface INRequestRideIntent : INIntent
```

## Overview

SiriKit creates an [`INRequestRideIntent`](./inrequestrideintent.md) object when the user asks to book a ride using your app. A ride request intent contains user-supplied information about the ride, such as its starting point and the number of people. Use this intent object to identify possible ride options for the user to choose from and to book the ride after the user confirms it.

To handle this intent, the handler object in your Intents extension must adopt the [`INRequestRideIntentHandling`](./inrequestrideintenthandling.md) protocol. Your handler should confirm the request and create an [`INRequestRideIntentResponse`](./inrequestrideintentresponse.md) object with information about whether your app successfully booked the ride.

When implementing ride-booking support, provide a GeoJSON file with the regions for which you are able to provide rides and upload that file as your app’s Routing App Coverage File in App Store Connect. When it needs to suggest apps capable of providing a ride, Maps uses your coverage information to determine whether it should suggest your app. If you do not provide a coverage file and your app is not installed on the user’s device, Maps does not suggest your app. For information about how to create and upload a Routing App Coverage File, see [iTunes Connect Developer Help](https://help.apple.com/itunes-connect/developer/#/dev4ba662442).

> **Note**:  When implementing ride-booking support, provide a GeoJSON file with the regions for which you’re able to provide rides and upload that file as your app’s Routing App Coverage File in App Store Connect. When it needs to suggest apps capable of providing a ride, Maps uses your coverage information to determine whether it should suggest your app. If you don’t provide a coverage file and your app isn’t installed on the user’s device, Maps doesn’t suggest your app. For information about how to create and upload a Routing App Coverage File, see [iTunes Connect Developer Help](https://help.apple.com/itunes-connect/developer/#/dev4ba662442).

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents, Maps |
| Always requires unlocked device | Yes |

## Topics

### Initializing the Intent Object
- [convenience init(pickupLocation: CLPlacemark?, dropOffLocation: CLPlacemark?, rideOptionName: INSpeakableString?, partySize: Int?, paymentMethod: INPaymentMethod?, scheduledPickupTime: INDateComponentsRange?)](./inrequestrideintent/init%28pickuplocation,dropofflocation,rideoptionname,partysize,paymentmethod,scheduledpickuptime%29.md)
  Initializes an intent object with the specified ride information.
- [- initWithPickupLocation:dropOffLocation:rideOptionName:partySize:paymentMethod:scheduledPickupTime:](./inrequestrideintent/initwithpickuplocation_dropofflocation_rideoptionname_partysize_paymentmethod_scheduledpickuptime_.md)
  Initializes an intent object with the specified ride information.
- [- initWithPickupLocation:dropOffLocation:rideOptionName:partySize:paymentMethod:](./inrequestrideintent/initwithpickuplocation_dropofflocation_rideoptionname_partysize_paymentmethod_.md)
  Initializes an intent object with the specified ride information.
### Getting the Ride Details
- [var rideOptionName: INSpeakableString?](./inrequestrideintent/rideoptionname.md)
  The name of the ride option selected by the user.
- [var partySize: Int?](./inrequestrideintent/partysize-39k7z.md)
  The number of passengers that the ride must accommodate.
- [var pickupLocation: CLPlacemark?](./inrequestrideintent/pickuplocation.md)
  The user’s starting location.
- [var scheduledPickupTime: INDateComponentsRange?](./inrequestrideintent/scheduledpickuptime.md)
  The time at which to pick up the user.
- [var dropOffLocation: CLPlacemark?](./inrequestrideintent/dropofflocation.md)
  The user’s destination.
- [partySize](./inrequestrideintent/partysize-64kfc.md)
  The number of passengers that the ride must accommodate.
### Getting the Payment Information
- [var paymentMethod: INPaymentMethod?](./inrequestrideintent/paymentmethod.md)
  The user’s requested payment method.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Request a Ride
- [protocol INRequestRideIntentHandling](./inrequestrideintenthandling.md)
  The handler interface for booking a ride for the user.
- [class INRequestRideIntentResponse](./inrequestrideintentresponse.md)
  Your app’s response to a request ride intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestrideintent)*