# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms whether you can perform the search.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
optional func confirm(intent: INSearchForNotebookItemsIntent, completion: @escaping @Sendable (INSearchForNotebookItemsIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INSearchForNotebookItemsIntent) async -> INSearchForNotebookItemsIntentResponse
```

```objc
- (void) confirmSearchForNotebookItems:(INSearchForNotebookItemsIntent *) intent completion:(void (^)(INSearchForNotebookItemsIntentResponse *response)) completion;
```

#### Discussion

Implement this method to validate that you can perform the search based on the provided criteria, but do not perform the search yet. If performing the search involves contacting a remote server, validate that your server is available and ready to handle requests. At some point in your implementation, execute the provided completion block with a response object indicating your app’s readiness to perform the search.

## Parameters

- `intent`: The intent object containing details about the user’s request. The information in this object has already been resolved by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. The handler has no return value and takes the following parameter:

  - **response**: The [`INSearchForNotebookItemsIntentResponse`](../insearchfornotebookitemsintentresponse.md) object containing the details to confirm with the user. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintenthandling/confirm(intent:completion:))*