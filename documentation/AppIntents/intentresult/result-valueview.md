# result(value:view:)

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
static func result<Value, Content>(value: Value, view: Content = EmptyView()) -> Self where Self == IntentResultContainer<Value, Never, _SnippetViewContainer, Never>, Value : _IntentValue, Content : View
```

## Parameters

- `value`: The value produced by the 
- `view`: A custom View to display the result


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(value:view:))*