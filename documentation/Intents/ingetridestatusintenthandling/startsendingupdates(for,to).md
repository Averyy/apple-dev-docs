# startSendingUpdates(for:to:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Start delivering regular updates about the specified ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
func startSendingUpdates(for intent: INGetRideStatusIntent, to observer: any INGetRideStatusIntentResponseObserver)
```

```objc
- (void) startSendingUpdatesForGetRideStatus:(INGetRideStatusIntent *) intent toObserver:(id<INGetRideStatusIntentResponseObserver>) observer;
```

## Mentions

- [Providing Live Status Updates](../../SiriKit/providing-live-status-updates.md)

## Discussion

The system calls this method when it wants you to provide periodic status updates on a previously booked ride. Your implementation should store a reference to the provided observer object and schedule a repeating task to send updates to that observer. SiriKit expects you to send updates fairly frequently, with a minimum update rate of once every 10 seconds. You should continue delivering updates until the system calls the [`stopSendingUpdates(for:)`](./stopsendingupdates%28for%29.md) method.

This method gets called on an arbitrary thread of your Intents extension. If you generate updates using a timer, set up your timer on your extension’s main thread rather than on the current thread.

## Parameters

- `intent`: The intent object indicating the ride for which to return updates. Use the [`identifier`](../inintent/identifier.md) property of the intent to distinguish this request from others.
- `observer`: The observer object to notify with the results. Store a reference to this object and call its methods when you have a status update to deliver. For more information about the methods to call, see [`INGetRideStatusIntentResponseObserver`](../ingetridestatusintentresponseobserver.md).

## See Also

### Providing Ride Status Updates
- [func stopSendingUpdates(for: INGetRideStatusIntent)](./stopsendingupdates%28for%29.md)
  Stops the delivery of status updates for the specified ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetridestatusintenthandling/startsendingupdates(for:to:))*