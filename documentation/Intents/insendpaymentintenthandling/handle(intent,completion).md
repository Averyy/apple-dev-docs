# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles transferring the money between accounts.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
func handle(intent: INSendPaymentIntent, completion: @escaping @Sendable (INSendPaymentIntentResponse) -> Void)
```

```swift
func handle(intent: INSendPaymentIntent) async -> INSendPaymentIntentResponse
```

```objc
- (void) handleSendPayment:(INSendPaymentIntent *) intent completion:(void (^)(INSendPaymentIntentResponse *response)) completion;
```

## Discussion

Your implementation of this method must transfer the specified money to the designated payee. The response object you provide should include the transaction details and indicate whether or not the transaction was successful.

You specify the transaction details using an [`INPaymentRecord`](../inpaymentrecord.md) object, which you include in your response object. For more information about configuring the response object, see [`INSendPaymentIntentResponse`](../insendpaymentintentresponse.md).

## Parameters

- `intent`: The intent object containing details about the user’s request. The information in this object has already been resolved and confirmed by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INSendPaymentIntentResponse`](../insendpaymentintentresponse.md) object containing the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendpaymentintenthandling/handle(intent:completion:))*