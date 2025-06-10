# result(content:)

**Framework**: App Intents  
**Kind**: method

Indicates the `AppIntent` finished performing

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
static func result<Content>(@ViewBuilder content: () -> Content) -> Self where Self == IntentResultContainer<Never, Never, _SnippetViewContainer, Never>, Content : View
```

## Parameters

- `content`: A custom View to display the result


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(content:))*