# confirm(cancelRide:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms that you can cancel the ride.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func confirm(cancelRide intent: INCancelRideIntent, completion: @escaping @Sendable (INCancelRideIntentResponse) -> Void)
```

```swift
optional func confirm(cancelRide intent: INCancelRideIntent) async -> INCancelRideIntentResponse
```

```objc
- (void) confirmCancelRide:(INCancelRideIntent *) intent completion:(void (^)(INCancelRideIntentResponse *response)) completion;
```

## Discussion

Implement this method to create a response object with information about whether you can cancel the ride. If your service charges fees for canceling a ride, include the fee information in your response object. Siri or Maps then presents the details of your response to the user.

If the code in your response is not [`INCancelRideIntentResponseCode.ready`](../incancelrideintentresponsecode/ready.md) or [`INCancelRideIntentResponseCode.success`](../incancelrideintentresponsecode/success.md), SiriKit aborts the handling of the intent object and falls back to other options. Specifically, if you supplied an [`NSUserActivity`](../../Foundation/nsuseractivity.md) object in the [`userActivityForCancelingInApplication`](../inridestatus/useractivityforcancelinginapplication.md) property of your [`INRideStatus`](../inridestatus.md) object when booking the ride, SiriKit delivers that user activity object to your app.

## Parameters

- `intent`: The intent object containing details about the user’s request.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INCancelRideIntentResponse`](../incancelrideintentresponse.md) object containing the status of whether your app is able to cancel the ride. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelrideintenthandling/confirm(cancelride:completion:))*