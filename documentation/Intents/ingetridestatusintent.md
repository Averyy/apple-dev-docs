# INGetRideStatusIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request for the current status of a previously booked ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INGetRideStatusIntent
```

```objc
@interface INGetRideStatusIntent : INIntent
```

#### Overview

When there’s a request for the status of a booked ride, SiriKit sends an [`INGetRideStatusIntent`](./ingetridestatusintent.md) object to your handler object. Upon receiving this intent, fetch the ride status and return it in your response object. The intent object has no additional parameters.

To handle this intent, the handler object in your Intents extension must adopt the [`INGetRideStatusIntentHandling`](./ingetridestatusintenthandling.md) protocol. Your handler should confirm the request and create an [`INGetRideStatusIntentResponse`](./ingetridestatusintentresponse.md) object with the status of the ride.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents, Maps |
| Always requires unlocked device | No |

Apps can optionally ask the user to unlock the device before handling this intent. To require unlocking of the device, include the name of this class in the `IntentsRestrictedWhileLocked` key of your Intents extension’s `Info.plist` file.

## Topics

### Initializing an Intent Object
- [init()](./ingetridestatusintent/init%28%29.md)
  Initializes the get ride status intent object.

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

### Get the Ride Status
- [protocol INGetRideStatusIntentHandling](./ingetridestatusintenthandling.md)
  The handler interface for fetching the status of the user’s current ride.
- [class INGetRideStatusIntentResponse](./ingetridestatusintentresponse.md)
  Your app’s response to a get ride status intent.
- [protocol INGetRideStatusIntentResponseObserver](./ingetridestatusintentresponseobserver.md)
  An interface for providing updated status for an active ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetridestatusintent)*