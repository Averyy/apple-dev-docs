# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms the details of the request to share the user’s focus status.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
optional func confirm(intent: INShareFocusStatusIntent, completion: @escaping @Sendable (INShareFocusStatusIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INShareFocusStatusIntent) async -> INShareFocusStatusIntentResponse
```

```objc
- (void) confirmShareFocusStatus:(INShareFocusStatusIntent *) intent completion:(void (^)(INShareFocusStatusIntentResponse *response)) completion;
```

## Parameters

- `intent`: The [`INShareFocusStatusIntent`](../insharefocusstatusintent.md) that contains details about the request.
- `completion`: The handler block to execute with your response. Execute this handler in your implementation of this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INShareFocusStatusIntentResponse`](../insharefocusstatusintentresponse.md) that contains the response code indicating whether your app can share the user’s focus status.

## See Also

### Processing the Intent
- [func handle(intent: INShareFocusStatusIntent, completion: (INShareFocusStatusIntentResponse) -> Void)](./handle%28intent,completion%29.md)
  Handles the intent that shares the user’s focus status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insharefocusstatusintenthandling/confirm(intent:completion:))*