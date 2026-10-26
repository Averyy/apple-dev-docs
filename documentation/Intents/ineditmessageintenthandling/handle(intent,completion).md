# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func handle(intent: INEditMessageIntent, completion: @escaping @Sendable (INEditMessageIntentResponse) -> Void)
```

```swift
func handle(intent: INEditMessageIntent) async -> INEditMessageIntentResponse
```

```objc
- (void) handleEditMessage:(INEditMessageIntent *) intent completion:(void (^)(INEditMessageIntentResponse *response)) completion;
```

## Mentions

- [Improving interactions between Siri and your messaging app](../../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ineditmessageintenthandling/handle(intent:completion:))*