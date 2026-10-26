# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms that you can book the ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func confirm(intent: INRequestRideIntent, completion: @escaping @Sendable (INRequestRideIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INRequestRideIntent) async -> INRequestRideIntentResponse
```

```objc
- (void) confirmRequestRide:(INRequestRideIntent *) intent completion:(void (^)(INRequestRideIntentResponse *response)) completion;
```

#### Discussion

Implement this method to create a response object with the details that you intend to use when booking the ride. Although you are providing details about how you intend to book the ride, do not actually book the ride from this method. Siri or Maps will present the details of your response to the user. If the user changes any ride properties prior to confirmation, you may have to resolve those properties and confirm the updated request again before handling the booking.

Put as many details as possible in the [`INRideStatus`](../inridestatus.md) object you configure with your response object. For more information about configuring the ride status object, see [`INRideStatus`](../inridestatus.md).

Maps may update the pickup location for the ride either before or after calling this method based on user input. Always use the information in the intent parameter to generate your confirmation response.

## Parameters

- `intent`: The intent object containing details about the user’s request. The information in this object has already been resolved by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INRequestRideIntentResponse`](../inrequestrideintentresponse.md) object containing the status of whether your app is able to book the ride, along with the ride details you are planning to use during booking. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestrideintenthandling/confirm(intent:completion:))*