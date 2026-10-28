# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms whether you can perform the search.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func confirm(intent: INSearchForBillsIntent, completion: @escaping @Sendable (INSearchForBillsIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INSearchForBillsIntent) async -> INSearchForBillsIntentResponse
```

```objc
- (void) confirmSearchForBills:(INSearchForBillsIntent *) intent completion:(void (^)(INSearchForBillsIntentResponse *response)) completion;
```

## Discussion

Implement this method to validate that you can perform the search using the given parameters, but don’t perform the search yet. If the search involves contacting a remote server, you should also validate that the server is available. At some point in your implementation, execute the provided completion block with a response object indicating your app’s readiness to perform the search.

## Parameters

- `intent`: The intent object containing details about the user’s request. Your handler object has already resolved the information in this object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. The handler has no return value and takes the following parameter:

  - **response**: The [`INSearchForBillsIntentResponse`](../insearchforbillsintentresponse.md) object containing the details to confirm with the user. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintenthandling/confirm(intent:completion:))*