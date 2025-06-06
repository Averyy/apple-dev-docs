# result(value:content:)

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
static func result<Value, Content>(value: Value, @ViewBuilder content: () -> Content) -> Self where Self == IntentResultContainer<Value, Never, _SnippetViewContainer, Never>, Value : _IntentValue, Content : View
```

## Parameters

- `value`: The value produced by the 
- `content`: A custom View to display the result


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(value:content:))*