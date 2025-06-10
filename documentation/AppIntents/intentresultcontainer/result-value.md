# result(value:)

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
static func result<Value>(value: Value) -> Self where Self == IntentResultContainer<Value, Never, Never, Never>, Value : _IntentValue
```

## Parameters

- `value`: The value produced by the 


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresultcontainer/result(value:))*