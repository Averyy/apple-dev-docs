# INCancelRideIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An intent requesting the cancellation of a previously booked ride.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INCancelRideIntent
```

```objc
@interface INCancelRideIntent : INIntent
```

#### Overview

When the user cancels a ride that was previously booked through Siri or Maps, SiriKit sends an [`INCancelRideIntent`](./incancelrideintent.md) object to your handler. SiriKit populates this intent object with the ride identifier that you provided when originally booking the ride. Upon receiving this intent, verify the ride information and cancel the ride accordingly.

To handle this intent, the handler object in your Intents extension must adopt the [`INCancelRideIntentHandling`](./incancelrideintenthandling.md) protocol. Your handler should confirm the request and create an [`INCancelRideIntentResponse`](./incancelrideintentresponse.md) object with the status of the ride.

SiriKit prefers sending this intent object to your extension over canceling a ride by other means. So when responding to an [`INRequestRideIntent`](./inrequestrideintent.md) object, you can continue to set the [`userActivityForCancelingInApplication`](./inridestatus/useractivityforcancelinginapplication.md) property of your response’s [`INRideStatus`](./inridestatus.md) object to allow cancellation of the ride in your app. SiriKit uses that [`NSUserActivity`](../Foundation/nsuseractivity.md) object only on systems where this intent is unavailable or not supported by your extension.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Maps |
| Always requires unlocked device | Yes |

## Topics

### Initializing an Intent Object
- [init(rideIdentifier: String)](./incancelrideintent/init%28rideidentifier%29.md)
  Initializes the intent object with the specified ride identifier.
### Identifying the Ride
- [var rideIdentifier: String](./incancelrideintent/rideidentifier.md)
  The unique identifier that you assigned to the ride.

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

### Cancel Ride
- [protocol INCancelRideIntentHandling](./incancelrideintenthandling.md)
  The handler interface for canceling a previously booked ride.
- [class INCancelRideIntentResponse](./incancelrideintentresponse.md)
  Your app’s response to a cancel ride intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelrideintent)*