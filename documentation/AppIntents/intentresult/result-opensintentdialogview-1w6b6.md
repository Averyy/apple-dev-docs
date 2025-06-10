# result(opensIntent:dialog:view:)

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
static func result<Content>(opensIntent: some AppIntent, dialog: IntentDialog, view: Content = EmptyView()) -> Self where Self == IntentResultContainer<Never, Never, _SnippetViewContainer, IntentDialog>, Content : View
```

## Parameters

- `opensIntent`: An   to shows the result of current intent
- `dialog`: A custom success dialog
- `view`: A custom View to display the result


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(opensintent:dialog:view:)-1w6b6)*