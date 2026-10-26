# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles the scheduling of the transfer.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
func handle(intent: INTransferMoneyIntent, completion: @escaping @Sendable (INTransferMoneyIntentResponse) -> Void)
```

```swift
func handle(intent: INTransferMoneyIntent) async -> INTransferMoneyIntentResponse
```

```objc
- (void) handleTransferMoney:(INTransferMoneyIntent *) intent completion:(void (^)(INTransferMoneyIntentResponse *response)) completion;
```

#### Discussion

Your implementation of this method must schedule the transfer using the information provided by the intent object. The response you object that you provide should include the transaction details and the success or failure of the operation. The successful scheduling of a transfer means that your service has recorded the transaction details and can perform the transfer on the specified date.

## Parameters

- `intent`: The intent object containing details about the user’s request. Your handler has already resolved and confirmed the information in this object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INTransferMoneyIntentResponse`](../intransfermoneyintentresponse.md) object containing the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintenthandling/handle(intent:completion:))*