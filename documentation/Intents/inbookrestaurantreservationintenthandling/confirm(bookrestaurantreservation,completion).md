# confirm(bookRestaurantReservation:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms whether you can complete the reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func confirm(bookRestaurantReservation intent: INBookRestaurantReservationIntent, completion: @escaping @Sendable (INBookRestaurantReservationIntentResponse) -> Void)
```

```swift
optional func confirm(bookRestaurantReservation intent: INBookRestaurantReservationIntent) async -> INBookRestaurantReservationIntentResponse
```

```objc
- (void) confirmBookRestaurantReservation:(INBookRestaurantReservationIntent *) intent completion:(void (^)(INBookRestaurantReservationIntentResponse *response)) completion;
```

#### Discussion

Implement this method to validate that you can complete the reservation. For example, you might use this method to verify the user’s account information and that your service is available. At some point in your implementation, execute the provided completion block with a response object indicating your app’s readiness to complete the reservation.

## Parameters

- `intent`: The intent object containing details about the request. The information in this object has already been resolved by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The[`INBookRestaurantReservationIntentResponse`](../inbookrestaurantreservationintentresponse.md) object containing the status of whether your app is able to complete the reservation. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintenthandling/confirm(bookrestaurantreservation:completion:))*