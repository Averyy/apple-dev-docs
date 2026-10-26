# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.2+
- iPadOS 16.2+
- Mac Catalyst 16.2+
- macOS 13.1+
- visionOS 1.0+
- watchOS 9.2+

## Declaration

```swift
optional func confirm(intent: INAnswerCallIntent, completion: @escaping @Sendable (INAnswerCallIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INAnswerCallIntent) async -> INAnswerCallIntentResponse
```

```objc
- (void) confirmAnswerCall:(INAnswerCallIntent *) intent completion:(void (^)(INAnswerCallIntentResponse *response)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inanswercallintenthandling/confirm(intent:completion:))*