# result(value:opensIntent:view:)

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
static func result<Value, Content>(value: Value, opensIntent: some AppIntent, view: Content = EmptyView()) -> Self where Self == IntentResultContainer<Value, Never, _SnippetViewContainer, Never>, Value : _IntentValue, Content : View
```

## Parameters

- `value`: The value produced by the 
- `opensIntent`: An   to shows the result of current intent
- `view`: A custom View to display the result


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(value:opensintent:view:)-12wbo)*