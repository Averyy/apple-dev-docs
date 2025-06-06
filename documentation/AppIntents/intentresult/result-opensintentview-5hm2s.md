# result(opensIntent:view:)

**Framework**: App Intents  
**Kind**: method

Indicates the `AppIntent` finished performing

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
static func result<Content>(opensIntent: some AppIntent, view: Content = EmptyView()) -> Self where Self == IntentResultContainer<Never, Never, _SnippetViewContainer, Never>, Content : View
```

## Parameters

- `opensIntent`: An   to shows the result of current intent
- `view`: A custom View to display the result


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(opensintent:view:)-5hm2s)*