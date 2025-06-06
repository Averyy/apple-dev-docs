# result(value:opensIntent:)

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
static func result<Value, OpensAppIntent>(value: Value, opensIntent: OpensAppIntent) -> Self where Self == IntentResultContainer<Value, OpensAppIntent, Never, Never>, Value : _IntentValue, OpensAppIntent : AppIntent
```

## Parameters

- `value`: The value produced by the 
- `opensIntent`: An   to shows the result of current intent


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(value:opensintent:)-1mbbt)*