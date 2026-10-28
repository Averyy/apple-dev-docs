# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Performs the search and returns the results.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
func handle(intent: INSearchForMessagesIntent, completion: @escaping @Sendable (INSearchForMessagesIntentResponse) -> Void)
```

```swift
func handle(intent: INSearchForMessagesIntent) async -> INSearchForMessagesIntentResponse
```

```objc
- (void) handleSearchForMessages:(INSearchForMessagesIntent *) intent completion:(void (^)(INSearchForMessagesIntentResponse *response)) completion;
```

## Discussion

Your implementation of this method must perform the search and return the results as part of your response object. If you are unable to perform the search, return a response object whose result code indicates the reason for the failure.

> **Note**:  In watchOS, Siri does not display the search results itself. Instead, it launches your watchOS app to display the search results.

## Parameters

- `intent`: The intent object that contains details about the user’s request. The object’s informatin has already been resolved and confirmed by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INSearchForMessagesIntentResponse`](../insearchformessagesintentresponse.md) object that contains the status of the request. You also use this object to specify the messages that matched the search parameters. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintenthandling/handle(intent:completion:))*