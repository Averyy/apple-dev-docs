# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms that you can perform the search.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func confirm(intent: INSearchCallHistoryIntent, completion: @escaping @Sendable (INSearchCallHistoryIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INSearchCallHistoryIntent) async -> INSearchCallHistoryIntentResponse
```

```objc
- (void) confirmSearchCallHistory:(INSearchCallHistoryIntent *) intent completion:(void (^)(INSearchCallHistoryIntentResponse *response)) completion;
```

#### Discussion

Implement this method to validate that you’re able to perform the search using the specified criteria. You might use this method to validate that you’ve access to the user’s call history and that there are records to search.

## Parameters

- `intent`: The intent object containing details about the user’s request. Your handler has already resolved the information in this object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. The handler has no return value and takes the following parameter:

  - **response**: The [`INSearchCallHistoryIntentResponse`](../insearchcallhistoryintentresponse.md) object containing the status of whether your app is able to perform the search. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintenthandling/confirm(intent:completion:))*