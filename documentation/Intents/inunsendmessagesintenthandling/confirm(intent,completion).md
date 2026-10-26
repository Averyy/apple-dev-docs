# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
optional func confirm(intent: INUnsendMessagesIntent, completion: @escaping @Sendable (INUnsendMessagesIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INUnsendMessagesIntent) async -> INUnsendMessagesIntentResponse
```

```objc
- (void) confirmUnsendMessages:(INUnsendMessagesIntent *) intent completion:(void (^)(INUnsendMessagesIntentResponse *response)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inunsendmessagesintenthandling/confirm(intent:completion:))*