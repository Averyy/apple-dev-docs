# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles searching the user’s call history.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
func handle(intent: INSearchCallHistoryIntent, completion: @escaping @Sendable (INSearchCallHistoryIntentResponse) -> Void)
```

```swift
func handle(intent: INSearchCallHistoryIntent) async -> INSearchCallHistoryIntentResponse
```

```objc
- (void) handleSearchCallHistory:(INSearchCallHistoryIntent *) intent completion:(void (^)(INSearchCallHistoryIntentResponse *response)) completion;
```

## Discussion

Implement this method to search the user’s call history for entries matching the specified parameters. If the search yields results, make a note of those results and prepare to have your app display them. For example, you could include the results in the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object that you create with your response object.

At the end of your implementation, execute the block in the completion parameter, passing it a response object that encapsulates whether the search was successful.

## Parameters

- `intent`: The intent object containing details about the user’s request. The user has already resolved and confirmed the information in this object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INSearchCallHistoryIntentResponse`](../insearchcallhistoryintentresponse.md) object containing the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchcallhistoryintenthandling/handle(intent:completion:))*