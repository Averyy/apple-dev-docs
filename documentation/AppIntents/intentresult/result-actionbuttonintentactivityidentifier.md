# result(actionButtonIntent:activityIdentifier:)

**Framework**: App Intents  
**Kind**: method

Indicates the Intent finished performing with an `AppIntent` to continue with

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst ?+
- macOS 14.2+
- tvOS 17.2+
- visionOS ?+
- watchOS 10.2+

## Declaration

```swift
static func result<Intent>(actionButtonIntent: Intent, activityIdentifier: String) -> Self where Self == IntentResultContainer<Never, Never, Never, Never>, Intent : AppIntent
```

## Parameters

- `actionButtonIntent`: The   used perform next


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(actionbuttonintent:activityidentifier:))*