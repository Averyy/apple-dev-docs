# handle(cancelRide:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles the user canceling an unfinished ride.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func handle(cancelRide intent: INCancelRideIntent, completion: @escaping @Sendable (INCancelRideIntentResponse) -> Void)
```

```swift
func handle(cancelRide intent: INCancelRideIntent) async -> INCancelRideIntentResponse
```

```objc
- (void) handleCancelRide:(INCancelRideIntent *) intent completion:(void (^)(INCancelRideIntentResponse *response)) completion;
```

#### Discussion

In your implementation of this method, cancel the ride described by the `intent` parameter, create a response object with any cancellation information, and call the provided `completion` handler. If your app is currently providing live status updates for the ride, immediately deliver an updated [`INRideStatus`](../inridestatus.md) object back to SiriKit with the cancellation details. Specifically, change the phase of the ride to [`INRidePhase.completed`](../inridephase/completed.md) and set the [`completionStatus`](../inridestatus/completionstatus.md) property to an object that indicates the user canceled the ride. Make sure the rest of the information in the [`INRideStatus`](../inridestatus.md) object is still accurate, including the ride identifier and ride option.

## Parameters

- `intent`: The intent object containing details about the user’s request. The information in this object has already been confirmed by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INCancelRideIntentResponse`](../incancelrideintentresponse.md) object containing the reason for the cancellation and information about any fees that might still apply. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelrideintenthandling/handle(cancelride:completion:))*