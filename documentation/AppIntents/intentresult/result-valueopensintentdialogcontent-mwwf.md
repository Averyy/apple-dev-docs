# result(value:opensIntent:dialog:content:)

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
static func result<Value, Content>(value: Value, opensIntent: some AppIntent, dialog: IntentDialog, @ViewBuilder content: () -> Content) -> Self where Self == IntentResultContainer<Value, Never, _SnippetViewContainer, IntentDialog>, Value : _IntentValue, Content : View
```

## Parameters

- `value`: The value produced by the 
- `opensIntent`: An   to shows the result of current intent
- `dialog`: A custom success dialog
- `content`: A custom View to display the result


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(value:opensintent:dialog:content:)-mwwf)*