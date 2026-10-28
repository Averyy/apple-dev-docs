# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the message to the specified recipients.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
func handle(intent: INSendMessageIntent, completion: @escaping @Sendable (INSendMessageIntentResponse) -> Void)
```

```swift
func handle(intent: INSendMessageIntent) async -> INSendMessageIntentResponse
```

```objc
- (void) handleSendMessage:(INSendMessageIntent *) intent completion:(void (^)(INSendMessageIntentResponse *response)) completion;
```

## Discussion

Your implementation of this method must send the message to the designated recipients. The response object you provide should indicate the status of the message.

## Parameters

- `intent`: The intent object that contains details about the user’s request. The information in this object has already been resolved and confirmed by the user.
- `completion`: The handler block to execute with your response. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INSendMessageIntentResponse`](../insendmessageintentresponse.md) object containing the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintenthandling/handle(intent:completion:))*