# result(opensIntent:dialog:)

**Framework**: App Intents  
**Kind**: method

Indicates the `AppIntent` finished performing

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
static func result<OpensAppIntent>(opensIntent: OpensAppIntent, dialog: IntentDialog) -> Self where Self == IntentResultContainer<Never, OpensAppIntent, Never, IntentDialog>, OpensAppIntent : AppIntent
```

## Parameters

- `opensIntent`: An   to shows the result of current intent
- `dialog`: A custom success dialog


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresultcontainer/result(opensintent:dialog:)-6wf55)*