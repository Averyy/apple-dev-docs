# result(value:dialog:content:)

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
static func result<Value, Content>(value: Value, dialog: IntentDialog, @ViewBuilder content: () -> Content) -> Self where Self == IntentResultContainer<Value, Never, _SnippetViewContainer, IntentDialog>, Value : _IntentValue, Content : View
```

## Parameters

- `value`: The value produced by the 
- `dialog`: A custom success dialog
- `content`: A custom View to display the result


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(value:dialog:content:))*