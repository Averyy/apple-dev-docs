# search

**Framework**: App Intents  
**Kind**: property

The app intent conforms to the schema for searching in journal entries.

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

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app intent implementation. The following example shows an app intent that conforms to the `.journal.search` schema:

```swift
@AppIntent(schema: .journal.search)
struct SearchJournalEntriesIntent: ShowInAppSearchResultsIntent {
    static var searchScopes: [StringSearchScope] = [.general]

    @Parameter
    var criteria: StringSearchCriteria

    func perform() async throws -> some IntentResult {
        .result()
    }
}
```

For more information about the `.journal` app intent domain, see [`Making journaling actions available to Siri and Apple Intelligence`](making-journaling-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

## See Also

- [var createAudioEntry: some AssistantSchemas.Intent](assistantschemas/journalintent/createaudioentry.md)
  The app intent conforms to the schema for creating a voice journal entry.
- [var createEntry: some AssistantSchemas.Intent](assistantschemas/journalintent/createentry.md)
  The app intent conforms to the schema for creating a journal entry.
- [var deleteEntry: some AssistantSchemas.Intent](assistantschemas/journalintent/deleteentry.md)
  The app intent conforms to the schema for deleting a journal entry.
- [var updateEntry: some AssistantSchemas.Intent](assistantschemas/journalintent/updateentry.md)
  The app intent conforms to the schema for updating a journal entry.
- [AssistantSchemas.JournalIntent](assistantschemas/journalintent.md)
  Assistant schema conformance for app intents that offer journaling functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/journalintent/search)*