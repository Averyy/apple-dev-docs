# result(opensIntent:content:)

**Framework**: App Intents  
**Kind**: method

Indicates the `AppIntent` finished performing

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst ?+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
static func result<Content>(opensIntent: some AppIntent, @ViewBuilder content: () -> Content) -> Self where Self == IntentResultContainer<Never, Never, _SnippetViewContainer, Never>, Content : View
```

## Parameters

- `opensIntent`: An   to shows the result of current intent
- `content`: A custom View to display the result


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(opensintent:content:)-965vk)*