# handle(getUserCurrentRestaurantReservationBookings:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles fetching the user’s current reservations.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func handle(getUserCurrentRestaurantReservationBookings intent: INGetUserCurrentRestaurantReservationBookingsIntent, completion: @escaping @Sendable (INGetUserCurrentRestaurantReservationBookingsIntentResponse) -> Void)
```

```swift
func handle(getUserCurrentRestaurantReservationBookings intent: INGetUserCurrentRestaurantReservationBookingsIntent) async -> INGetUserCurrentRestaurantReservationBookingsIntentResponse
```

```objc
- (void) handleGetUserCurrentRestaurantReservationBookings:(INGetUserCurrentRestaurantReservationBookingsIntent *) intent completion:(void (^)(INGetUserCurrentRestaurantReservationBookingsIntentResponse *response)) completion;
```

#### Discussion

Your implementation of this method should fetch the user’s current reservations, using the information in the `intent` parameter to filter the search results. When done, execute the provided block with a response object that contains the appropriate set of reservations.

## Parameters

- `intent`: The intent object containing details about the request. The information in this object has already been resolved and confirmed.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INGetUserCurrentRestaurantReservationBookingsIntentResponse`](../ingetusercurrentrestaurantreservationbookingsintentresponse.md) object you create to report the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetusercurrentrestaurantreservationbookingsintenthandling/handle(getusercurrentrestaurantreservationbookings:completion:))*