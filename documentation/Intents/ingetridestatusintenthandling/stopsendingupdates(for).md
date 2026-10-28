# stopSendingUpdates(for:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Stops the delivery of status updates for the specified ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
func stopSendingUpdates(for intent: INGetRideStatusIntent)
```

```objc
- (void) stopSendingUpdatesForGetRideStatus:(INGetRideStatusIntent *) intent;
```

## Mentions

- [Providing Live Status Updates](../../SiriKit/providing-live-status-updates.md)

## Discussion

SiriKit asks you to stop delivering updates when the user no longer has any active rides. You define when a ride becomes inactive by setting the [`rideStatus`](../ingetridestatusintentresponse/ridestatus.md) property of your response object to `nil` when crafting your response. You can clear this property after ride completion or wait until after you have received payment and handled any feedback from the user. Until you do, continue to provide observer updates at regular intervals.

Your implementation of this method should remove any references to the previously registered observer object and cancel any timers or repeating tasks that you used to generate updates.

## Parameters

- `intent`: The intent object for which to return updates. Use the [`identifier`](../inintent/identifier.md) property of the intent to distinguish this request from others.

## See Also

### Providing Ride Status Updates
- [func startSendingUpdates(for: INGetRideStatusIntent, to: any INGetRideStatusIntentResponseObserver)](./startsendingupdates%28for,to%29.md)
  Start delivering regular updates about the specified ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetridestatusintenthandling/stopsendingupdates(for:))*