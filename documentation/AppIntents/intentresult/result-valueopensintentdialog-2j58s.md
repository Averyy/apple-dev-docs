# result(value:opensIntent:dialog:)

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
static func result<Value, OpensAppIntent>(value: Value, opensIntent: OpensAppIntent, dialog: IntentDialog) -> Self where Self == IntentResultContainer<Value, OpensAppIntent, Never, IntentDialog>, Value : _IntentValue, OpensAppIntent : AppIntent
```

## Parameters

- `value`: The value produced by the 
- `opensIntent`: An   to shows the result of current intent
- `dialog`: A custom success dialog


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(value:opensintent:dialog:)-2j58s)*