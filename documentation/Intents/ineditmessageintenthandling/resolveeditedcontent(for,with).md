# resolveEditedContent(for:with:)

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
optional func resolveEditedContent(for intent: INEditMessageIntent, with completion: @escaping @Sendable (INStringResolutionResult) -> Void)
```

```swift
optional func resolveEditedContent(for intent: INEditMessageIntent) async -> INStringResolutionResult
```

```objc
- (void) resolveEditedContentForEditMessage:(INEditMessageIntent *) intent withCompletion:(void (^)(INStringResolutionResult *resolutionResult)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ineditmessageintenthandling/resolveeditedcontent(for:with:))*