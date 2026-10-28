# confirm(getAvailableRestaurantReservationBookingDefaults:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms whether you can return default values.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func confirm(getAvailableRestaurantReservationBookingDefaults intent: INGetAvailableRestaurantReservationBookingDefaultsIntent, completion: @escaping @Sendable (INGetAvailableRestaurantReservationBookingDefaultsIntentResponse) -> Void)
```

```swift
optional func confirm(getAvailableRestaurantReservationBookingDefaults intent: INGetAvailableRestaurantReservationBookingDefaultsIntent) async -> INGetAvailableRestaurantReservationBookingDefaultsIntentResponse
```

```objc
- (void) confirmGetAvailableRestaurantReservationBookingDefaults:(INGetAvailableRestaurantReservationBookingDefaultsIntent *) intent completion:(void (^)(INGetAvailableRestaurantReservationBookingDefaultsIntentResponse *response)) completion;
```

## Discussion

Implement this method to validate you can provide default restaurant information.

## Parameters

- `intent`: The intent object containing details about the request. The information in this object has already been resolved by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INGetAvailableRestaurantReservationBookingDefaultsIntentResponse`](../ingetavailablerestaurantreservationbookingdefaultsintentresponse.md) object containing the status of whether your app is able to return default values. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingdefaultsintenthandling/confirm(getavailablerestaurantreservationbookingdefaults:completion:))*