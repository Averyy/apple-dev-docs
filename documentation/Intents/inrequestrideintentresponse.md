# INRequestRideIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a request ride intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INRequestRideIntentResponse
```

```objc
@interface INRequestRideIntentResponse : INIntentResponse
```

## Overview

An [`INRequestRideIntentResponse`](./inrequestrideintentresponse.md) object contains your app’s response to a ride-booking request. After creating your response object, assign an appropriate object to the [`rideStatus`](./inrequestrideintentresponse/ridestatus.md) property. The ride status object provides the details about how you handled the ride, including details about selected vehicle type, pricing, driver information, pickup time, pickup location, drop-off location, and so on. Siri and Maps display your response information to the user during the confirmation and booking phases.

Siri and Maps expect your response to contain a valid [`INRideStatus`](./inridestatus.md) object with information about the ride. Specifically, your status object must include a valid [`INRideOption`](./inrideoption.md) object and you should always specify an activity object in the [`userActivityForCancelingInApplication`](./inridestatus/useractivityforcancelinginapplication.md) property of your status object. When handling the intent, the [`INRequestRideIntentResponseCode.unspecified`](./inrequestrideintentresponsecode/unspecified.md) and [`INRequestRideIntentResponseCode.ready`](./inrequestrideintentresponsecode/ready.md) codes generate an error and should not be used.

You create an [`INRequestRideIntentResponse`](./inrequestrideintentresponse.md) object in the [`confirm(intent:completion:)`](./inrequestrideintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./inrequestrideintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INRequestRideIntentHandling`](./inrequestrideintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INRequestRideIntentResponseCode, userActivity: NSUserActivity?)](./inrequestrideintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INRequestRideIntentResponseCode](./inrequestrideintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INRequestRideIntentResponseCode](./inrequestrideintentresponsecode.md)
  Constants indicating the state of the response.
### Accessing the Response Parameters
- [var rideStatus: INRideStatus?](./inrequestrideintentresponse/ridestatus.md)
  The current status of the ride.

## Relationships

### Inherits From
- [INIntentResponse](./inintentresponse.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Request a Ride
- [protocol INRequestRideIntentHandling](./inrequestrideintenthandling.md)
  The handler interface for booking a ride for the user.
- [class INRequestRideIntent](./inrequestrideintent.md)
  A request to book the specified ride from your service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestrideintentresponse)*