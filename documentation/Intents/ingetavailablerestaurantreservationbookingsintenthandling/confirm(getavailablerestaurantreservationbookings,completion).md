# confirm(getAvailableRestaurantReservationBookings:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms whether you can provide a set of potential reservation times.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func confirm(getAvailableRestaurantReservationBookings intent: INGetAvailableRestaurantReservationBookingsIntent, completion: @escaping @Sendable (INGetAvailableRestaurantReservationBookingsIntentResponse) -> Void)
```

```swift
optional func confirm(getAvailableRestaurantReservationBookings intent: INGetAvailableRestaurantReservationBookingsIntent) async -> INGetAvailableRestaurantReservationBookingsIntentResponse
```

```objc
- (void) confirmGetAvailableRestaurantReservationBookings:(INGetAvailableRestaurantReservationBookingsIntent *) intent completion:(void (^)(INGetAvailableRestaurantReservationBookingsIntentResponse *response)) completion;
```

## Discussion

Implement this method to validate that you can generate a set of potential reservation times. For example, you might use this method to verify the user’s account information. At some point in your implementation, execute the provided completion block with a response object indicating your app’s readiness to generate the reservation details.

## Parameters

- `intent`: The intent object containing details about the request. The information in this object has already been resolved by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INGetAvailableRestaurantReservationBookingsIntentResponse`](../ingetavailablerestaurantreservationbookingsintentresponse.md) object containing the status of whether your app is able to provide the potential reservation times. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintenthandling/confirm(getavailablerestaurantreservationbookings:completion:))*