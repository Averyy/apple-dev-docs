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
optional func confirm(intent: INEditMessageIntent, completion: @escaping @Sendable (INEditMessageIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INEditMessageIntent) async -> INEditMessageIntentResponse
```

```objc
- (void) confirmEditMessage:(INEditMessageIntent *) intent completion:(void (^)(INEditMessageIntentResponse *response)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ineditmessageintenthandling/confirm(intent:completion:))*