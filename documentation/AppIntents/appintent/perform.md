# perform()

**Framework**: App Intents  
**Kind**: method  
**Required**: Yes

Performs the intent after resolving the provided parameters.

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
func perform() async throws -> Self.PerformResult
```

## Mentions

- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)
- [Creating your first app intent](creating-your-first-app-intent.md)
- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)

#### Discussion

In the body of this function, validate your parameters and provide the system with information about needed parameter values or user clarification.

## See Also

- [var systemContext: IntentSystemContext](appintent/systemcontext.md)
  Context information that’s available while the system performs the app intent’s action.
- [associatedtype PerformResult : IntentResult](appintent/performresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/perform())*