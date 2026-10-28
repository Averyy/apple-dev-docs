# confirm(getRestaurantGuest:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms whether you can provide the guest information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func confirm(getRestaurantGuest guestIntent: INGetRestaurantGuestIntent, completion: @escaping @Sendable (INGetRestaurantGuestIntentResponse) -> Void)
```

```swift
optional func confirm(getRestaurantGuest guestIntent: INGetRestaurantGuestIntent) async -> INGetRestaurantGuestIntentResponse
```

```objc
- (void) confirmGetRestaurantGuest:(INGetRestaurantGuestIntent *) guestIntent completion:(void (^)(INGetRestaurantGuestIntentResponse *response)) completion;
```

## Discussion

Implement this method to validate that you can return the current user’s information. At some point in your implementation, execute the provided completion block with a response object.

## Parameters

- `guestIntent`: The intent object describing the request.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INGetRestaurantGuestIntentResponse`](../ingetrestaurantguestintentresponse.md) object containing the status of whether your app is able to return information about the current user. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetrestaurantguestintenthandling/confirm(getrestaurantguest:completion:))*