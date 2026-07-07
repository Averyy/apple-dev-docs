# semanticContentSearch

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for visual search functionality.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var semanticContentSearch: some AssistantSchemas.Intent { get }
```

#### Overview

To integrate your app’s functionality with Visual Intelligence you use Swift macros that generate additional properties and add protocol conformance for your app intent implementation.

For more information about the `.visualIntelligence` app intent domain, see doc:Making-in-app-search-actions-available-to-siri-and-apple-intelligence. For general information about app intent domains, see doc:Integrating-actions-with-siri-and-apple-intelligence.

The following example shows an app intent that conforms to the `.visualIntelligence.semanticContentSearch` schema:

```swift
@AppIntent(schema: .visualIntelligence.semanticContentSearch)
struct SemanticContentSearchIntent: AppIntent {
    @Parameter var semanticContent: SemanticContentDescriptor

    func perform() async throws -> some IntentResult {
        return .result()
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/visualintelligenceintent/semanticcontentsearch)*