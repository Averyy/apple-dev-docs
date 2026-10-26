# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 16.2+
- iPadOS 16.2+
- Mac Catalyst 16.2+
- macOS 13.1+
- visionOS 1.0+
- watchOS 9.2+

## Declaration

```swift
func handle(intent: INHangUpCallIntent, completion: @escaping @Sendable (INHangUpCallIntentResponse) -> Void)
```

```swift
func handle(intent: INHangUpCallIntent) async -> INHangUpCallIntentResponse
```

```objc
- (void) handleHangUpCall:(INHangUpCallIntent *) intent completion:(void (^)(INHangUpCallIntentResponse *response)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inhangupcallintenthandling/handle(intent:completion:))*