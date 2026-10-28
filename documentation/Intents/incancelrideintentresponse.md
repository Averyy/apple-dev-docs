# INCancelRideIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a cancel ride intent.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INCancelRideIntentResponse
```

```objc
@interface INCancelRideIntentResponse : INIntentResponse
```

## Overview

An [`INCancelRideIntentResponse`](./incancelrideintentresponse.md) object contains your app’s response to the cancellation of a ride. After creating the response object, specify any cancellation-related fees using the properties of this object. Siri and Maps display your response information to the user during the confirmation phase.

You create an [`INCancelRideIntentResponse`](./incancelrideintentresponse.md) object in the [`confirm(cancelRide:completion:)`](./incancelrideintenthandling/confirm%28cancelride,completion%29.md) and [`handle(cancelRide:completion:)`](./incancelrideintenthandling/handle%28cancelride,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INCancelRideIntentHandling`](./incancelrideintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INCancelRideIntentResponseCode, userActivity: NSUserActivity?)](./incancelrideintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INCancelRideIntentResponseCode](./incancelrideintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INCancelRideIntentResponseCode](./incancelrideintentresponsecode.md)
  Constants indicating the state of the response.
### Specifying Cancellation Fees
- [var cancellationFee: INCurrencyAmount?](./incancelrideintentresponse/cancellationfee.md)
  The cancellation fee charged by your service.
- [var cancellationFeeThreshold: DateComponents?](./incancelrideintentresponse/cancellationfeethreshold.md)
  The amount of time that must elapse before cancellation fees apply.

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

### Cancel Ride
- [protocol INCancelRideIntentHandling](./incancelrideintenthandling.md)
  The handler interface for canceling a previously booked ride.
- [class INCancelRideIntent](./incancelrideintent.md)
  An intent requesting the cancellation of a previously booked ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelrideintentresponse)*