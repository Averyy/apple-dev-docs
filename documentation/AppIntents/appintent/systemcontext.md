# systemContext

**Framework**: App Intents  
**Kind**: property

Contextual information that the system provides while it performs the app intent.

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
var systemContext: IntentSystemContext { get }
```

#### Discussion

Access information the system provides to your app intent while it performs its action in its [`perform()`](appintent/perform().md) implementation. The available information varies by platform. For example, in watchOS, the intent system context includes a precise timestamp when a person starts the app intent’s action using the Action button on Apple Watch Ultra.

## See Also

- [func perform() async throws -> Self.PerformResult](appintent/perform.md)
  Performs the intent’s action and returns a result, after resolving any parameters.
- [associatedtype PerformResult : IntentResult](appintent/performresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/systemcontext)*