# INGetRideStatusIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a get ride status intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INGetRideStatusIntentResponse
```

```objc
@interface INGetRideStatusIntentResponse : INIntentResponse
```

## Overview

An [`INGetRideStatusIntentResponse`](./ingetridestatusintentresponse.md) object contains your app’s response to a request for the status of the user’s current ride. SiriKit can ask for the status of a ride at any time, but often this occurs in response to a direct request from the user. Use your response object to provide current details about the user’s ride, including the estimated pickup time, the pickup location, the drop-off location, the vehicle type, the driver, and so on.

You create an [`INGetRideStatusIntentResponse`](./ingetridestatusintentresponse.md) object in the [`confirm(intent:completion:)`](./ingetridestatusintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./ingetridestatusintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INGetRideStatusIntentHandling`](./ingetridestatusintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INGetRideStatusIntentResponseCode, userActivity: NSUserActivity?)](./ingetridestatusintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INGetRideStatusIntentResponseCode](./ingetridestatusintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INGetRideStatusIntentResponseCode](./ingetridestatusintentresponsecode.md)
  Constants indicating the state of the response.
### Getting the Ride Status Information
- [var rideStatus: INRideStatus?](./ingetridestatusintentresponse/ridestatus.md)
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

### Get the Ride Status
- [protocol INGetRideStatusIntentHandling](./ingetridestatusintenthandling.md)
  The handler interface for fetching the status of the user’s current ride.
- [class INGetRideStatusIntent](./ingetridestatusintent.md)
  A request for the current status of a previously booked ride.
- [protocol INGetRideStatusIntentResponseObserver](./ingetridestatusintentresponseobserver.md)
  An interface for providing updated status for an active ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetridestatusintentresponse)*