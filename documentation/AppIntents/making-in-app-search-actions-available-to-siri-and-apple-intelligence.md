# Making in-app search actions available to Siri and Apple Intelligence

**Framework**: App Intents

Create app intents and entities to integrate your app’s search functionality with Siri and Apple Intelligence.

#### Overview

To integrate your in-app search with Siri and Apple Intelligence, you use Swift macros that generate additional properties and add protocol conformance to your [`ShowInAppSearchResultsIntent`](showinappsearchresultsintent.md) implementation.

> **Note**: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

Use the [`AssistantIntent(schema:)`](assistantintent(schema:).md) macro and provide the assistant schema that consists of the `.system` domain and the [`search`](assistantschemas/systemintent/search.md) schema:

```swift
import AppIntents
import Foundation

@AssistantIntent(schema: .system.search)
struct ExampleSearchIntent: ShowInAppSearchResultsIntent {
    static var searchScopes: [StringSearchScope] = [.general]
    var criteria: StringSearchCriteria
    
    func perform() async throws -> some IntentResult {
        let searchString = criteria.term
        print("Searching for \(searchString)")
        // ...
        // Code that navigates to your app's search and enters the search string into a search field.
        // ...
        return .result()
    }
}
```

To learn more about assistant schemas, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

## See Also

- [AssistantSchemas.SystemIntent](assistantschemas/systemintent.md)
  Assistant schema conformance for app intents that match system-provided intents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/making-in-app-search-actions-available-to-siri-and-apple-intelligence)*