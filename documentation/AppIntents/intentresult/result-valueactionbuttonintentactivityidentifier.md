# result(value:actionButtonIntent:activityIdentifier:)

**Framework**: App Intents  
**Kind**: method

Creates a result container with a value, a follow-on intent, and an identifier.

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

- `value`: The value produced by the `AppIntent`
- `actionButtonIntent`: A follow-on intent that can run next.
- `activityIdentifier`: An identifier for the follow-on intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(value:actionbuttonintent:activityidentifier:))*