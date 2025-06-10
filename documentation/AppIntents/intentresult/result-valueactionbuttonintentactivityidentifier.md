# result(value:actionButtonIntent:activityIdentifier:)

**Framework**: App Intents  
**Kind**: method

Indicates the Intent finished performing with an `AppIntent` to continue with

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst ?+
- macOS 14.2+
- tvOS 17.2+
- visionOS ?+
- watchOS 10.2+

## Declaration

```swift
static func result<Value, Intent>(value: Value, actionButtonIntent: Intent, activityIdentifier: String) -> Self where Self == IntentResultContainer<Value, Never, Never, Never>, Value : _IntentValue, Intent : AppIntent
```

## Parameters

- `value`: The value produced by the 


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(value:actionbuttonintent:activityidentifier:))*