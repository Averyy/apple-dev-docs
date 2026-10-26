# INGetRideStatusIntentResponseObserver

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface for providing updated status for an active ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
protocol INGetRideStatusIntentResponseObserver : NSObjectProtocol
```

```objc
@protocol INGetRideStatusIntentResponseObserver <NSObject>
```

#### Overview

The [`INGetRideStatusIntentResponseObserver`](./ingetridestatusintentresponseobserver.md) protocol defines methods that provide SiriKit with an updated status for an active ride request. You do not implement the methods of this protocol in your own objects. Instead, the system provides an object that adopts this protocol. You call its [`didUpdate(getRideStatus:)`](./ingetridestatusintentresponseobserver/didupdate%28getridestatus%29.md) method to deliver updated information about the status of a booked ride.

When the system initiates a request for status updates, it passes an object that adopts this protocol to the [`startSendingUpdates(for:to:)`](./ingetridestatusintenthandling/startsendingupdates%28for,to%29.md) method of your ride status handler object—your custom object that adopts the [`INGetRideStatusIntentHandling`](./ingetridestatusintenthandling.md) protocol. Your handler must store a reference to this object and use it to deliver regular updates about the status of the ride.

For more information about providing status updates for a ride, see [`INGetRideStatusIntentHandling`](./ingetridestatusintenthandling.md).

## Topics

### Updating the Status of a Ride
- [Providing Live Status Updates](../SiriKit/providing-live-status-updates.md)
  Provide regular updates to Maps about the status of a booked ride.
- [func didUpdate(getRideStatus: INGetRideStatusIntentResponse)](./ingetridestatusintentresponseobserver/didupdate%28getridestatus%29.md)
  Call this method when you have updated information about the ride.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Get the Ride Status
- [protocol INGetRideStatusIntentHandling](./ingetridestatusintenthandling.md)
  The handler interface for fetching the status of the user’s current ride.
- [class INGetRideStatusIntent](./ingetridestatusintent.md)
  A request for the current status of a previously booked ride.
- [class INGetRideStatusIntentResponse](./ingetridestatusintentresponse.md)
  Your app’s response to a get ride status intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetridestatusintentresponseobserver)*