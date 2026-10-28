# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms the transaction details and validates the transaciton.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func confirm(intent: INTransferMoneyIntent, completion: @escaping @Sendable (INTransferMoneyIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INTransferMoneyIntent) async -> INTransferMoneyIntentResponse
```

```objc
- (void) confirmTransferMoney:(INTransferMoneyIntent *) intent completion:(void (^)(INTransferMoneyIntentResponse *response)) completion;
```

## Discussion

Implement this method to resolve the transaction details. Use this method to validate that scheduling payment for the specified bill is possible. You might use this method to validate the following information:

- The user logged in to your app, and is able to transfer money between accounts.
- The user’s accounts are valid and the source account contains sufficient funds.

At some point in your implementation, execute the provided handler block with a response object containing the transaction details. Siri displays this information to the user during the confirmation process. For more information about creating the response object, see [`INTransferMoneyIntentResponse`](../intransfermoneyintentresponse.md).

## Parameters

- `intent`: The intent object containing details about the user’s request. Your handler object has already resolved the properties of this object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. The handler has no return value and takes the following parameter:

  - **response**: The [`INTransferMoneyIntentResponse`](../intransfermoneyintentresponse.md) object containing the details to confirm with the user. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintenthandling/confirm(intent:completion:))*