# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms whether you can perform the search.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func confirm(intent: INSearchForMessagesIntent, completion: @escaping @Sendable (INSearchForMessagesIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INSearchForMessagesIntent) async -> INSearchForMessagesIntentResponse
```

```objc
- (void) confirmSearchForMessages:(INSearchForMessagesIntent *) intent completion:(void (^)(INSearchForMessagesIntentResponse *response)) completion;
```

#### Discussion

This method validates you can perform the search using the given parameters. If the search involves contacting a remote server, you should also validate that the server is available. At some point in your implementation, execute the provided completion block with a response object indicating your app’s readiness to perform the search.

## Parameters

- `intent`: The intent object that contains details about the user’s request. The information in this object has already been resolved by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INSearchForMessagesIntentResponse`](../insearchformessagesintentresponse.md) object that contains the details to confirm with the user. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintenthandling/confirm(intent:completion:))*