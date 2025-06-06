# result(dialog:view:)

**Framework**: App Intents  
**Kind**: method

Indicates the `AppIntent` finished performing

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func result<Content>(dialog: IntentDialog, view: Content = EmptyView()) -> Self where Self == IntentResultContainer<Never, Never, _SnippetViewContainer, IntentDialog>, Content : View
```

## Parameters

- `dialog`: A custom success dialog
- `view`: A custom View to display the result


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(dialog:view:))*