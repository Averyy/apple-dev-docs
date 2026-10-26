# didUpdate(getRideStatus:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Call this method when you have updated information about the ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
func didUpdate(getRideStatus response: INGetRideStatusIntentResponse)
```

```objc
- (void) getRideStatusResponseDidUpdate:(INGetRideStatusIntentResponse *) response;
```

#### Discussion

Call this method to deliver updated status information back to SiriKit. When asked to deliver updates, you should do so frequently, calling this method no less than once every 20 seconds. The response object you create should contain the latest information about the user’s ride.

When the user’s ride finishes and you no longer want to provide status updates, set the [`rideStatus`](../ingetridestatusintentresponse/ridestatus.md) property of your response object to `nil`. You decide what constitutes the end of the ride. For example, you might end the ride when it reaches the [`INRidePhase.completed`](../inridephase/completed.md) phase or you might wait until after the user has settled payment and the user has had an opportunity to provide feedback.

## Parameters

- `response`: The response object containing updated information about the ride. Use this object to provide updated information about the booked ride.

## See Also

### Updating the Status of a Ride
- [Providing Live Status Updates](../../SiriKit/providing-live-status-updates.md)
  Provide regular updates to Maps about the status of a booked ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetridestatusintentresponseobserver/didupdate(getridestatus:))*