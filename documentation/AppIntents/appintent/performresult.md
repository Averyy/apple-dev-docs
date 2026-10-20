# PerformResult

**Framework**: App Intents  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
associatedtype PerformResult : IntentResult
```

## See Also

### Performing the action
- [func perform() async throws -> Self.PerformResult](./perform%28%29.md)
  Performs the intent’s action and returns a result, after resolving any parameters.
- [var systemContext: IntentSystemContext](./systemcontext.md)
  Contextual information that the system provides while it performs the app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/performresult)*