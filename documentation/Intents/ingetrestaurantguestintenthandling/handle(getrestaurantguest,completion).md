# handle(getRestaurantGuest:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles returning the information about the user making the reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func handle(getRestaurantGuest intent: INGetRestaurantGuestIntent, completion: @escaping @Sendable (INGetRestaurantGuestIntentResponse) -> Void)
```

```swift
func handle(getRestaurantGuest intent: INGetRestaurantGuestIntent) async -> INGetRestaurantGuestIntentResponse
```

```objc
- (void) handleGetRestaurantGuest:(INGetRestaurantGuestIntent *) intent completion:(void (^)(INGetRestaurantGuestIntentResponse *response)) completion;
```

#### Discussion

In your implementation of this method, you should create an [`INRestaurantGuest`](../inrestaurantguest.md) object containing the current user’s information and assign it to your response object. You should also create an [`INRestaurantGuestDisplayPreferences`](../inrestaurantguestdisplaypreferences.md) object and specify the options for displaying the user’s information. When done, execute the provided block with your response object.

## Parameters

- `intent`: The intent object containing details about the request. The information in this object has already been confirmed.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INGetRestaurantGuestIntentResponse`](../ingetrestaurantguestintentresponse.md) object you create to report the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetrestaurantguestintenthandling/handle(getrestaurantguest:completion:))*