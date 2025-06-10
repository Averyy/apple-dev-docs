# result(value:actionButtonIntent:dialog:)

**Framework**: App Intents  
**Kind**: method

Indicates the Intent finished performing with an `AppIntent` to continue with

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
static func result<Value, Intent>(value: Value, actionButtonIntent: Intent, dialog: IntentDialog) -> Self where Self == IntentResultContainer<Value, Never, Never, IntentDialog>, Value : _IntentValue, Intent : AppIntent
```

## Parameters

- `value`: The value produced by the 
- `actionButtonIntent`: The   used perform next
- `dialog`: A custom success dialog


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresultcontainer/result(value:actionbuttonintent:dialog:))*