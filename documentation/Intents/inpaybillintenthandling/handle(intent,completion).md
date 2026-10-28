# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles scheduling payment of the bill.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
func handle(intent: INPayBillIntent, completion: @escaping @Sendable (INPayBillIntentResponse) -> Void)
```

```swift
func handle(intent: INPayBillIntent) async -> INPayBillIntentResponse
```

```objc
- (void) handlePayBill:(INPayBillIntent *) intent completion:(void (^)(INPayBillIntentResponse *response)) completion;
```

## Discussion

Your implementation of this method must schedule payment of the specified bill using the information in the intent object. The response object you provide should include the transaction details and indicate whether or not scheduling of the transaction was successful.

When configuring your response object, you specify the bill details and the user account to transfer the money from. You also specify the scheduled transaction date for the payment. The successful scheduling of a payment means that your service has recorded the transaction details and scheduled the payment for the specified date.

## Parameters

- `intent`: The intent object containing details about the user’s request. Your handler object has already resolved and confirmed the information in this object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INPayBillIntentResponse`](../inpaybillintentresponse.md) object containing the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintenthandling/handle(intent:completion:))*