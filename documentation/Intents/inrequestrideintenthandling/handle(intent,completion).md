# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles the booking of the ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
func handle(intent: INRequestRideIntent, completion: @escaping @Sendable (INRequestRideIntentResponse) -> Void)
```

```swift
func handle(intent: INRequestRideIntent) async -> INRequestRideIntentResponse
```

```objc
- (void) handleRequestRide:(INRequestRideIntent *) intent completion:(void (^)(INRequestRideIntentResponse *response)) completion;
```

#### Discussion

Your implementation of this method must book the requested ride using the data in the `intent` parameter, configure a response object with the details of the booking, and call the provided `completion` block. When configuring your response object, use the [`rideStatus`](../inrequestrideintentresponse/ridestatus.md) property to specify an [`INRideStatus`](../inridestatus.md) object with the details of the ride. A ride status object contains information about the vehicle and driver that are picking up the user’s party, the pickup and drop-off locations, the price of the ride, and whether the booking request was successful. For more information about configuring this object, see [`INRideStatus`](../inridestatus.md).

## Parameters

- `intent`: The intent object containing details about the user’s request. The information in this object has already been resolved and confirmed by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INRequestRideIntentResponse`](../inrequestrideintentresponse.md) object containing the details of the booked ride. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestrideintenthandling/handle(intent:completion:))*