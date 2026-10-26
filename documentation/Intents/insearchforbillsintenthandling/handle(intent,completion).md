# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles searching for the specified bills.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
func handle(intent: INSearchForBillsIntent, completion: @escaping @Sendable (INSearchForBillsIntentResponse) -> Void)
```

```swift
func handle(intent: INSearchForBillsIntent) async -> INSearchForBillsIntentResponse
```

```objc
- (void) handleSearchForBills:(INSearchForBillsIntent *) intent completion:(void (^)(INSearchForBillsIntentResponse *response)) completion;
```

#### Discussion

Use the specified parameters to perform the search, then return the results in your response object. If you’re unable to perform the search, return a response object whose result code indicates the reason for the failure.

The response object you create should indicate the success or failure of the operation. Never create a response object using the [`INSearchForBillsIntentResponseCode.unspecified`](../insearchforbillsintentresponsecode/unspecified.md) or [`INSearchForBillsIntentResponseCode.ready`](../insearchforbillsintentresponsecode/ready.md) codes.

## Parameters

- `intent`: The intent object containing details about the user’s request. Your handler object has already resolved and confirmed the information in this object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INSearchForBillsIntentResponse`](../insearchforbillsintentresponse.md) object containing the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintenthandling/handle(intent:completion:))*