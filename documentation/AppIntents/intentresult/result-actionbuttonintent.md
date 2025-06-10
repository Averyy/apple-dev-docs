# result(actionButtonIntent:)

**Framework**: App Intents  
**Kind**: method

Indicates the Intent finished performing with an `AppIntent` to continue with

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static func result<Intent>(actionButtonIntent: Intent) -> Self where Self == IntentResultContainer<Never, Never, Never, Never>, Intent : AppIntent
```

## Mentions

- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)

## Parameters

- `actionButtonIntent`: The   used perform next


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(actionbuttonintent:))*