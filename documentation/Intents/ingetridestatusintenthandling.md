# INGetRideStatusIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The handler interface for fetching the status of the user’s current ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
protocol INGetRideStatusIntentHandling : NSObjectProtocol
```

```objc
@protocol INGetRideStatusIntentHandling <NSObject>
```

## Mentions

- [Providing Live Status Updates](../SiriKit/providing-live-status-updates.md)

#### Overview

Use the methods of the [`INGetRideStatusIntentHandling`](./ingetridestatusintenthandling.md) protocol to confirm and handle requests to get the status of the user’s currently booked ride. Adopt this protocol in an object of your Intents extension that is capable of retrieving the ride details from your service.

SiriKit may deliver an [`INGetRideStatusIntent`](./ingetridestatusintent.md) object to your handler object at any time, including when the user asks explicitly for the status of that ride. The specified intent object contains no additional information. Your app must know which ride is currently active. Use the methods of this protocol to handle the request and provide an appropriate response.

Maps does not require you to confirm the contents of a get ride status intent before handling it. User interactions drive the selection of data in Maps, ensuring that the data Maps places into an intent object is already valid.

##### Updating the Ride Status Periodically

After returning your response, SiriKit may call the [`startSendingUpdates(for:to:)`](./ingetridestatusintenthandling/startsendingupdates%28for,to%29.md) method to ask for further updates as the ride status changes. Implement that method and use it to begin the delivery of regular updates. Continue providing updates until SiriKit calls the [`stopSendingUpdates(for:)`](./ingetridestatusintenthandling/stopsendingupdates%28for%29.md) method.

After it starts observing the status of a ride, SiriKit keeps your Intents extension alive so that it can provide frequent updates. Always deliver an update at least once every 20 seconds; otherwise, provide updates with the same frequency that you use for updating your own app. Always provide updates when the ride phase or completion status changes. For example, provide an update when your vehicle is approaching the pickup location or arrives at it. SiriKit uses the updates to refresh any map interfaces displaying the location of your vehicle to the user.

Use the methods of the observer object to deliver your updates back to SiriKit. For more information about providing updates to the observer, see [`INGetRideStatusIntentResponseObserver`](./ingetridestatusintentresponseobserver.md).

## Topics

### Confirming the Response
- [func confirm(intent: INGetRideStatusIntent, completion: (INGetRideStatusIntentResponse) -> Void)](./ingetridestatusintenthandling/confirm%28intent,completion%29.md)
  Confirms the details of the user’s request.
### Handling the Intent
- [func handle(intent: INGetRideStatusIntent, completion: (INGetRideStatusIntentResponse) -> Void)](./ingetridestatusintenthandling/handle%28intent,completion%29.md)
  Handles providing the current status of the user’s ride.
### Providing Ride Status Updates
- [func startSendingUpdates(for: INGetRideStatusIntent, to: any INGetRideStatusIntentResponseObserver)](./ingetridestatusintenthandling/startsendingupdates%28for,to%29.md)
  Start delivering regular updates about the specified ride.
- [func stopSendingUpdates(for: INGetRideStatusIntent)](./ingetridestatusintenthandling/stopsendingupdates%28for%29.md)
  Stops the delivery of status updates for the specified ride.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INRidesharingDomainHandling](./inridesharingdomainhandling.md)

## See Also

### Get the Ride Status
- [class INGetRideStatusIntent](./ingetridestatusintent.md)
  A request for the current status of a previously booked ride.
- [class INGetRideStatusIntentResponse](./ingetridestatusintentresponse.md)
  Your app’s response to a get ride status intent.
- [protocol INGetRideStatusIntentResponseObserver](./ingetridestatusintentresponseobserver.md)
  An interface for providing updated status for an active ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetridestatusintenthandling)*