# search

**Framework**: App Intents  
**Kind**: property

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var search: some AssistantSchemas.Intent { get }
```

## Mentions

- [Making in-app search actions available to Siri and Apple Intelligence](making-in-app-search-actions-available-to-siri-and-apple-intelligence.md)

#### Overview

To integrate your app’s functionality with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance for your app intent implementation.

For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

The following example shows an app intent that conforms to the `system.search` schema:

```swift
@AppIntent(schema: .system.search)
struct ShowInAppSearchResultsIntent: ShowInAppSearchResultsIntent {
    static var searchScopes: [StringSearchScope] = [.general]var criteria: String

func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

## See Also

- [AssistantSchemas.SystemIntent](assistantschemas/systemintent.md)
  Assistant schema conformance for types you use for system functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/systemintent/search)*