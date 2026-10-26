# handle(getAvailableRestaurantReservationBookingDefaults:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles returning the default values to use when pre-fetching reservations.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func handle(getAvailableRestaurantReservationBookingDefaults intent: INGetAvailableRestaurantReservationBookingDefaultsIntent, completion: @escaping @Sendable (INGetAvailableRestaurantReservationBookingDefaultsIntentResponse) -> Void)
```

```swift
func handle(getAvailableRestaurantReservationBookingDefaults intent: INGetAvailableRestaurantReservationBookingDefaultsIntent) async -> INGetAvailableRestaurantReservationBookingDefaultsIntentResponse
```

```objc
- (void) handleGetAvailableRestaurantReservationBookingDefaults:(INGetAvailableRestaurantReservationBookingDefaultsIntent *) intent completion:(void (^)(INGetAvailableRestaurantReservationBookingDefaultsIntentResponse *response)) completion;
```

#### Discussion

Your implementation of this method should construct a response object containing the default values to use. Use the information in the `intent` parameter to fetch any restaurant-specific information. When done, execute the provided block with your response object.

## Parameters

- `intent`: The intent object containing details about the request. The information in this object has already been resolved and confirmed.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INGetAvailableRestaurantReservationBookingDefaultsIntentResponse`](../ingetavailablerestaurantreservationbookingdefaultsintentresponse.md) object you create to report the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingdefaultsintenthandling/handle(getavailablerestaurantreservationbookingdefaults:completion:))*