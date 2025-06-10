# result(opensIntent:)

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
static func result<OpensAppIntent>(opensIntent: OpensAppIntent) -> Self where Self == IntentResultContainer<Never, OpensAppIntent, Never, Never>, OpensAppIntent : AppIntent
```

## Parameters

- `opensIntent`: An   to shows the result of current intent


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresultcontainer/result(opensintent:)-2an32)*