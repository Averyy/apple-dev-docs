# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms the details of the user’s request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func confirm(intent: INGetRideStatusIntent, completion: @escaping @Sendable (INGetRideStatusIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INGetRideStatusIntent) async -> INGetRideStatusIntentResponse
```

```objc
- (void) confirmGetRideStatus:(INGetRideStatusIntent *) intent completion:(void (^)(INGetRideStatusIntentResponse *response)) completion;
```

## Discussion

Implement this method to verify that you are able to return the status for the ride. You might use this method to verify that your service is available and that the user has a valid account. Create a response object with an appropriate code indicating your app’s readiness and execute the provided `completion` block.

When configuring your response object, specify the details of an active ride using an [`INRideStatus`](../inridestatus.md) object. Specify as much information about the ride as you can. A ride status object includes information about the vehicle and driver that are picking up the user’s party, the pickup and drop off locations, the price of the ride, and the current status of the ride. If the user does not have an active ride, specify `nil` in the [`rideStatus`](../ingetridestatusintentresponse/ridestatus.md) property of the response object. For more information about configuring the ride status object, see [`INRideStatus`](../inridestatus.md).

Maps does not call this method. The Maps interface lets the user request ride status updates explicitly, making confirmation of those requests unnecessary.

## Parameters

- `intent`: The intent object for the user’s request. This object contains no additional information.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INGetRideStatusIntentResponse`](../ingetridestatusintentresponse.md) object containing the status of whether your app is able to return information about the ride. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetridestatusintenthandling/confirm(intent:completion:))*