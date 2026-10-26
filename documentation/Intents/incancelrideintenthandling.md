# INCancelRideIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for canceling a previously booked ride.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
protocol INCancelRideIntentHandling : NSObjectProtocol
```

```objc
@protocol INCancelRideIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INCancelRideIntentHandling`](./incancelrideintenthandling.md) protocol to confirm and handle requests to cancel the user’s currently active ride. Adopt this protocol in an object of your Intents extension that is capable of canceling the ride with your service.

Users may cancel rides from Siri or Maps. When the user requests to cancel a booked ride, SiriKit may send an [`INGetRideStatusIntent`](./ingetridestatusintent.md) object to your extension first to verify that a ride is still active and to retrieve the associated ride identifier. It includes that ride identifier in the [`INCancelRideIntent`](./incancelrideintent.md) object that it sends to your Intents extension.

SiriKit prefers sending an [`INCancelRideIntent`](./incancelrideintent.md) object to your extension over canceling a ride by other means. So when responding to an [`INRequestRideIntent`](./inrequestrideintent.md) object, you can continue to set the [`userActivityForCancelingInApplication`](./inridestatus/useractivityforcancelinginapplication.md) property of your response’s [`INRideStatus`](./inridestatus.md) object to allow cancellation of the ride in your app. SiriKit uses that [`NSUserActivity`](../Foundation/nsuseractivity.md) object only on systems where the cancellation intent is unavailable or not supported by your extension.

## Topics

### Confirming the Response
- [func confirm(cancelRide: INCancelRideIntent, completion: (INCancelRideIntentResponse) -> Void)](./incancelrideintenthandling/confirm%28cancelride,completion%29.md)
  Confirms that you can cancel the ride.
### Handling the Intent
- [func handle(cancelRide: INCancelRideIntent, completion: (INCancelRideIntentResponse) -> Void)](./incancelrideintenthandling/handle%28cancelride,completion%29.md)
  Handles the user canceling an unfinished ride.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INRidesharingDomainHandling](./inridesharingdomainhandling.md)

## See Also

### Cancel Ride
- [class INCancelRideIntent](./incancelrideintent.md)
  An intent requesting the cancellation of a previously booked ride.
- [class INCancelRideIntentResponse](./incancelrideintentresponse.md)
  Your app’s response to a cancel ride intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelrideintenthandling)*